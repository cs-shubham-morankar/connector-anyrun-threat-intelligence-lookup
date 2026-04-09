"""
Copyright start
MIT License
Copyright (c) 2026 Fortinet Inc
Copyright end
"""

import traceback
from connectors.core.connector import ConnectorError, get_logger
from anyrun import RunTimeException
from anyrun.connectors.threat_intelligence.lookup_connector import LookupConnector
from .constants import VERSION

logger = get_logger('anyrun-threat-intelligence-lookup')


def exceptions_handler(function):
    """ Handles errors in functions """

    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except RunTimeException as error:
            logger.exception(str(error))
            raise ConnectorError(f'ANY.RUN Exception: {str(error)}')
        except Exception:
            error = traceback.format_exc()
            logger.exception(error)
            raise ConnectorError(f'Unspecified Exception: {error}')

    return wrapper


@exceptions_handler
def get_intelligence(config, params) -> dict:
    """ Requests information from ANY.RUN TI Lookup """
    token = config.get('api_key')
    verify_ssl = config.get('verify_ssl')

    with LookupConnector(api_key=token, integration=VERSION, verify_ssl=verify_ssl) as connector:
        return connector.get_intelligence(**params)


@exceptions_handler
def _check_health(config) -> dict:
    """ Checks connection to ANY.RUN """
    token = config.get('api_key')
    verify_ssl = config.get('verify_ssl')

    with LookupConnector(api_key=token, integration=VERSION, verify_ssl=verify_ssl) as connector:
        return connector.check_authorization()


operations = {
    'get_intelligence': get_intelligence
}
