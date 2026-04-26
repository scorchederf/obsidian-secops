---
mitre_id: "T1597"
mitre_name: "Search Closed Sources"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--a51eb150-93b1-484b-a503-e51453b127a4"
mitre_created: "2020-10-02T17:01:42.558Z"
mitre_modified: "2025-10-24T17:49:11.164Z"
mitre_version: "1.1"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1597/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "PRE"
mitre_tactic_ids:
  - "TA0043"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Adversaries may search and gather information about victims from closed (e.g., paid, private, or otherwise not freely available) sources that can be used during targeting. Information about victims may be available for purchase from reputable private sources and databases, such as paid subscriptions to feeds of technical/threat intelligence data. Adversaries may also purchase information from less-reputable sources such as dark web or cybercrime blackmarkets.(Citation: ZDNET Selling Data)

Adversaries may search in different closed databases depending on what information they seek to gather. Information from these sources may reveal opportunities for other forms of reconnaissance (ex: [[T1598-phishing_for_information|T1598: Phishing for Information]] or [[T1593-search_open_websites_domains|T1593: Search Open Websites/Domains]]), establishing operational resources (ex: [[T1587-develop_capabilities|T1587: Develop Capabilities]] or [[T1588-obtain_capabilities|T1588: Obtain Capabilities]]), and/or initial access (ex: [[T1133-external_remote_services|T1133: External Remote Services]] or [[T1078-valid_accounts|T1078: Valid Accounts]]).

## Workspace

- [[workspaces/attack/techniques/T1597-search_closed_sources-note|Open workspace note]]

![[workspaces/attack/techniques/T1597-search_closed_sources-note]]

## Tactics

- [[TA0043-reconnaissance|TA0043: Reconnaissance]]

## Subtechniques

### T1597.001: Threat Intel Vendors

^t1597001-threat-intel-vendors

Adversaries may search private data from threat intelligence vendors for information that can be used during targeting. Threat intelligence vendors may offer paid feeds or portals that offer more data than what is publicly reported. Although sensitive details (such as customer names and other identifiers) may be redacted, this information may contain trends regarding breaches such as target industries, attribution claims, and successful TTPs/countermeasures.(Citation: D3Secutrity CTI Feeds)

Adversaries may search in private threat intelligence vendor data to gather actionable information. If a threat actor is searching for information on their own activities, that falls under [[T1681-search_threat_vendor_data|T1681: Search Threat Vendor Data]]. Information reported by vendors may also reveal opportunities other forms of reconnaissance (ex: [[T1593-search_open_websites_domains|T1593: Search Open Websites/Domains]]), establishing operational resources (ex: [[T1587-develop_capabilities|T1587: Develop Capabilities]] or [[T1588-obtain_capabilities|T1588: Obtain Capabilities]]), and/or initial access (ex: [[T1190-exploit_public-facing_application|T1190: Exploit Public-Facing Application]] or [[T1133-external_remote_services|T1133: External Remote Services]]).

### T1597.002: Purchase Technical Data

^t1597002-purchase-technical-data

Adversaries may purchase technical information about victims that can be used during targeting. Information about victims may be available for purchase within reputable private sources and databases, such as paid subscriptions to feeds of scan databases or other data aggregation services. Adversaries may also purchase information from less-reputable sources such as dark web or cybercrime blackmarkets.

Adversaries may purchase information about their already identified targets, or use purchased data to discover opportunities for successful breaches. Threat actors may gather various technical details from purchased data, including but not limited to employee contact information, credentials, or specifics regarding a victim’s infrastructure.(Citation: ZDNET Selling Data) Information from these sources may reveal opportunities for other forms of reconnaissance (ex: [[T1598-phishing_for_information|T1598: Phishing for Information]] or [[T1593-search_open_websites_domains|T1593: Search Open Websites/Domains]]), establishing operational resources (ex: [[T1587-develop_capabilities|T1587: Develop Capabilities]] or [[T1588-obtain_capabilities|T1588: Obtain Capabilities]]), and/or initial access (ex: [[T1133-external_remote_services|T1133: External Remote Services]] or [[T1078-valid_accounts|T1078: Valid Accounts]]).

## Mitigations

- [[M1056-pre-compromise|M1056: Pre-compromise]]

## Platforms

- PRE

