---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-DNR"
d3fend_name: "Decoy Network Resource"
d3fend_ontology_id: "d3f:DecoyNetworkResource"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3ADecoyNetworkResource/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-25 20:43:29"
build_source: "script"
attack_technique_ids:
  - "T1037"
  - "T1037.003"
  - "T1039"
  - "T1070"
  - "T1070.005"
  - "T1074"
  - "T1074.002"
  - "T1080"
  - "T1213"
  - "T1213.001"
  - "T1213.002"
  - "T1491"
  - "T1491.002"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Deploying a network resource for the purposes of deceiving an adversary.

## Workspace

- [[workspaces/defend/techniques/D3-DNR-decoy_network_resource-note|Open workspace note]]

![[workspaces/defend/techniques/D3-DNR-decoy_network_resource-note]]

## Parent Technique

- [[D3-DO-decoy_object|D3-DO: Decoy Object]]

## Related ATT&CK Techniques

- [[T1037-boot_or_logon_initialization_scripts|T1037: Boot or Logon Initialization Scripts]]
- [[T1037-boot_or_logon_initialization_scripts#^t1037003-network-logon-script|T1037.003: Network Logon Script]]
- [[T1039-data_from_network_shared_drive|T1039: Data from Network Shared Drive]]
- [[T1070-indicator_removal|T1070: Indicator Removal]]
- [[T1070-indicator_removal#^t1070005-network-share-connection-removal|T1070.005: Network Share Connection Removal]]
- [[T1074-data_staged|T1074: Data Staged]]
- [[T1074-data_staged#^t1074002-remote-data-staging|T1074.002: Remote Data Staging]]
- [[T1080-taint_shared_content|T1080: Taint Shared Content]]
- [[T1213-data_from_information_repositories|T1213: Data from Information Repositories]]
- [[T1213-data_from_information_repositories#^t1213001-confluence|T1213.001: Confluence]]
- [[T1213-data_from_information_repositories#^t1213002-sharepoint|T1213.002: Sharepoint]]
- [[T1491-defacement|T1491: Defacement]]
- [[T1491-defacement#^t1491002-external-defacement|T1491.002: External Defacement]]

## Knowledge Base Article

## How it works
Decoy network resources are deployed to web application servers, network file shares, or other network based sharing services.

A "honeypot" may serve a variety of decoy network resources.

## Considerations

* Developing a deployment and placement strategy for the decoy network resource.
* Personnel responsible for creation of decoy networks should consider the potential for resource exhaustion through denial of service attacks.

## Examples
* Honeypots are typically used to mimic a known system with fake vulnerabilities. This may attract attackers to the honeypot.
* Decoy accounts are also used to scan for attempted logins. The decoy accounts can provide security analysts with the attacker's potential intents and strategies.
* Tarpits are used to monitor unallocated IP space for unauthorized network activity.

## Ontology Relationships

- [[D3-DO-decoy_object|D3-DO: Decoy Object]]

