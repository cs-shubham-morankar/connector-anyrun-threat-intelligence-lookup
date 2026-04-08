 ## About the connector

ANY.RUN empowers SOC teams to cut MTTD/MTTR with fast IOC enrichment using Threat Intelligence Lookup.
Add the ANY.RUN Threat Intelligence Lookup connector as a step in FortiSOAR™ playbooks and perform automated operations to achieve: 
- **Confident response**: Query IOCs/IOAs/IOBs for full context based on live attack data from 15K+ SOCs. Accelerate incident mitigation with actionable intel and reduce MTTR by up to 21 minutes. Use obtained data for incident response, to create new rules, train models, update playbooks, etc.

### Version information

- Connector Version: 1.0.0 
- FortiSOAR™ Version Tested on: 7.6.4-5623 
- Authored By: ANY.RUN 

## Release Notes for version 1.0.0

- Connector: ANY.RUN Threat Intelligence Lookup. TI Lookup is a searchable database of IOCs, IOAs, IOBs, and events for threat hunting and a service for browsing malicious files by their content.
- Playbooks: This playbooks automatically enriches your IOCs using ANY.RUN's Threat Intelligence Lookup, providing fresh, actionable context from sandbox analyses of the latest malware & phishing attacks across 15,000+ organizations:

  - File/Domain/IP/URL > ANY.RUN Threat Intelligence > Enrichment
  - File > ANY.RUN Threat Intelligence > Enrichment
  - File Hash > ANY.RUN Threat Intelligence > Enrichment
  - IP > ANY.RUN Threat Intelligence > Enrichment 
  - Domain > ANY.RUN Threat Intelligence > Enrichment
  - URL > ANY.RUN Threat Intelligence > Enrichment

  

## Installing the connector

Use the Content Hub to install the connector. For the detailed procedure to install a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector)

You can also use the following `yum` command as a root user to install connectors from an SSH session:

```

yum install cyops-connector-anyrun-ti-lookup

```

## Prerequisites to configuring the connector

- Credentials are required to access the ANY.RUN Threat Intelligence Lookup. Ensure you have an ANY.RUN account with API access. For more information about the products, click [ANY.RUN Threat Intelligence Lookup](https://any.run/threat-intelligence-lookup/?utm_source=anyrungithub&utm_medium=documentation&utm_campaign=fortisoar&utm_content=linktolookuplanding).
- The FortiSOAR™ server should have outbound connectivity to port 443 on the ANY.RUN Threat Intelligence Lookup.


## Configuring the connector

For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)

### Configuration parameters

In FortiSOAR™, on the Connectors page, click the **ANY.RUN Threat Intelligence Lookup** connector row (if you are in the **Grid** view on the Connectors page) and in the **Configurations** tab enter the required configuration details: 

| Parameter | Description |
|--|--|
| API Key | ANY.RUN API Key in format:`"NS9sY..FwvfR"`to access the ANY.RUN APIs  |
| Verify SSL | Specifies whether the SSL certificate for the server is to be verified or not. By default, this option is set as True. |

### Generate API Key

- Follow [ANY.RUN](https://app.any.run/?utm_source=anyrungithub&utm_medium=documentation&utm_campaign=fortisoar&utm_content=linktoservice)
- Profile > [2] API and Limits > [3] Generate > [4] Copy

![ANYRUN_API_TOKEN.png](images/ANYRUN_API_TOKEN.png) 


## Actions supported by the connector

The following automated operations can be included in playbooks, and you can also use the annotations to access operations from FortiSOAR™:

| Function | Description | Annotation and Category |
|--|--|--|
| Threat Intelligence IOC Lookup | Perform threat intelligence using specified IOC.  This action requires ANY.RUN TI License. For more information about available parameters refer to official [documentation](https://any.run/api-documentation/?utm_source=anyrungithub&utm_medium=documentation&utm_campaign=fortisoar&utm_content=linktodocs)  | `get_intelligence` (Investigation)  |


### Operation: Threat Intelligence IOC Lookup

#### Input parameters

| Parameter | Description |
|--|--|
| Query | Query with necessary filters. Supports condition concatenation with AND, OR, NOT and Parentheses ().  |
| Lookup Depth | Specify the number of days from the current date for which you want to lookup.  |

#### Output

The output contains the following populated JSON schema: 

```
{
  "error": "",
  "data": {
    "query": "string",
    "results": "string"
  }
}
```


## Included playbooks

The `Sample - ANY.RUN Threat Intelligence Lookup - 1.0.0` playbook collection comes bundled with the ANY.RUN Threat Intelligence Lookup connector. 
  - File/Domain/IP/URL > ANY.RUN Threat Intelligence > Enrichment
  - File > ANY.RUN Threat Intelligence > Enrichment
  - File Hash > ANY.RUN Threat Intelligence > Enrichment
  - IP > ANY.RUN Threat Intelligence > Enrichment 
  - Domain > ANY.RUN Threat Intelligence > Enrichment
  - URL > ANY.RUN Threat Intelligence > Enrichment

These playbooks contain steps using which you can perform all supported actions, and you can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR™ after importing the ANY.RUN Threat Intelligence Lookup connector. 

### File/Domain/IP/URL > ANY.RUN Threat Intelligence > Enrichment

This workflow automatically enriches your IOCs using ANY.RUN's Threat Intelligence Lookup, providing fresh, actionable context from sandbox analyses of the latest malware & phishing attacks across 15,000+ organizations.

The playbook lets you pull behavioral details, TTPs, attack patterns, OS events, threat classifications, entity relationships, and metadata (threat level, OS, submission country) directly into your FortiSOAR indicator fields. 

As a result, you get greater incident clarity from precise attack context, broader threat insight through IOC/IOA/IOB relationships, and enhanced threat hunting as enriched IOCs reveal hidden threats. 

To use this playbook, you need a TI Lookup Premium subscription.

This playbook has a manual trigger type and supports the following indicator types:
  - *File*
  - *FileHash-MD5*
  - *FileHash-SHA256*
  - *FileHash-SHA1*
  - *IP Address*
  - *Domain*
  - *URL*

For more information about ANY.RUN's Threat Intelligence Lookup and query syntax, click [here](https://intelligence.any.run/analysis/lookup/?utm_source=anyrungithub&utm_medium=documentation&utm_campaign=fortisoar&utm_content=linktolookup)

## Pluggable Enrichment

`Sample - ANY.RUN Threat Intelligence Lookup - 1.0.0` playbook collection contains pluggable enrichment playbooks that are used to provide verdicts for various indicator types. The indicator can be of any of the following types: File, File Hash, Domain, IP Address, or URL. The pluggable enrichment playbooks are in the format: *<indicator type>* > ANY.RUN Threat Intelligence > Enrichment format. For example, *URL > ANY.RUN Threat Intelligence > Enrichment*. 

When using these playbooks, indicators are automatically enriched upon creation in the FortiSOAR.
By default, these playbooks are disabled. After activating this playbooks, you need to update the global variables. To do this, simply run the "Reset Enrichment Global Variables" playbook in your FortiSOAR.

The ANY.RUN Threat Intelligence integration API response returns the verdict, enrichment_summary and other variables as listed in the following table:

| Variable Name | Description | Return Value |
|--|--|--|
| verdict | This connector returns a high-reliability value called *verdict*. Use this verdict to find the reputation of the various types of indicators.  | if the value in vars.threatlevel == 2 the verdict returned is *Malicious* <br> if the value in vars.threatlevel == 1 the verdict returned is *Suspicious* <br> if the value in vars.threatlevel == 3 the verdict returned is *Good* <br> For any other value, return the verdict as *No Reputation Available*  |
| cti_name | The name of the connector is called the CTI (Cyber Threat Intelligence) name  | ANY.RUN Threat Intelligence |
| cti_score | The verdict value returned by the integration API  | Returns the value contained in *vars.threat_level* |
| source_data | The source_data response returned by the integration API  | A JSON response object containing the source data of the threat intelligence integration |
| enrichment_summary | The contents that are added, in the HTML format, in the *Description* field of the specified FortiSOAR indicator record.  | The following image displays a sample of the populated Description field in a FortiSOAR indicator record: ![sample.png](images/sample.png)  | 


**Note**: If you plan to use any of the sample playbooks, clone them and move them to a different collection, since the sample playbook collection gets deleted during connector upgrade and deletion. 

## Support
For details on how you can make ANY.RUN's solutions a part of your infrastructure, [contact us](https://app.any.run/contact-us/?utm_source=anyrungithub&utm_campaign=fortisoar&utm_medium=documentation&utm_content=contact_us).
For technical assistance, reach out to <support@any.run>.