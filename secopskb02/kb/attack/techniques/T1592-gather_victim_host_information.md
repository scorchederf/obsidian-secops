---
mitre_id: "T1592"
mitre_name: "Gather Victim Host Information"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--09312b1a-c3c6-4b45-9844-3ccc78e5d82f"
mitre_created: "2020-10-02T16:39:33.966Z"
mitre_modified: "2025-10-24T17:48:21.583Z"
mitre_version: "1.2"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1592/"
framework: "attack"
generated: "true"
build_date: "2026-04-25 20:43:29"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Adversaries may gather information about the victim's hosts that can be used during targeting. Information about hosts may include a variety of details, including administrative data (ex: name, assigned IP, functionality, etc.) as well as specifics regarding its configuration (ex: operating system, language, etc.).

Adversaries may gather this information in various ways, such as direct collection actions via [[T1595-active_scanning|T1595: Active Scanning]] or [[T1598-phishing_for_information|T1598: Phishing for Information]]. Adversaries may also compromise sites then include malicious content designed to collect host information from visitors.(Citation: ATT ScanBox) Information about hosts may also be exposed to adversaries via online or other accessible data sets (ex: [[T1593-search_open_websites_domains#^t1593001-social-media|T1593.001: Social Media]] or [[T1594-search_victim-owned_websites|T1594: Search Victim-Owned Websites]]). Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [[T1593-search_open_websites_domains|T1593: Search Open Websites/Domains]] or [[T1596-search_open_technical_databases|T1596: Search Open Technical Databases]]), establishing operational resources (ex: [[T1587-develop_capabilities|T1587: Develop Capabilities]] or [[T1588-obtain_capabilities|T1588: Obtain Capabilities]]), and/or initial access (ex: [[T1195-supply_chain_compromise|T1195: Supply Chain Compromise]] or [[T1133-external_remote_services|T1133: External Remote Services]]).

Adversaries may also gather victim host information via User-Agent HTTP headers, which are sent to a server to identify the application, operating system, vendor, and/or version of the requesting user agent. This can be used to inform the adversary’s follow-on action. For example, adversaries may check user agents for the requesting operating system, then only serve malware for target operating systems while ignoring others.(Citation: TrellixQakbot)

## Workspace

- [[workspaces/attack/techniques/T1592-gather_victim_host_information-note|Open workspace note]]

![[workspaces/attack/techniques/T1592-gather_victim_host_information-note]]

## Tactics

- [[TA0043-reconnaissance|TA0043: Reconnaissance]]

## Subtechniques

### T1592.001: Hardware

^t1592001-hardware

Adversaries may gather information about the victim's host hardware that can be used during targeting. Information about hardware infrastructure may include a variety of details such as types and versions on specific hosts, as well as the presence of additional components that might be indicative of added defensive protections (ex: card/biometric readers, dedicated encryption hardware, etc.).

Adversaries may gather this information in various ways, such as direct collection actions via [[T1595-active_scanning|T1595: Active Scanning]] (ex: hostnames, server banners, user agent strings) or [[T1598-phishing_for_information|T1598: Phishing for Information]]. Adversaries may also compromise sites then include malicious content designed to collect host information from visitors.(Citation: ATT ScanBox) Information about the hardware infrastructure may also be exposed to adversaries via online or other accessible data sets (ex: job postings, network maps, assessment reports, resumes, or purchase invoices). Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [[T1593-search_open_websites_domains|T1593: Search Open Websites/Domains]] or [[T1596-search_open_technical_databases|T1596: Search Open Technical Databases]]), establishing operational resources (ex: [[T1587-develop_capabilities|T1587: Develop Capabilities]] or [[T1588-obtain_capabilities|T1588: Obtain Capabilities]]), and/or initial access (ex: [[T1195-supply_chain_compromise#^t1195003-compromise-hardware-supply-chain|T1195.003: Compromise Hardware Supply Chain]] or [[T1200-hardware_additions|T1200: Hardware Additions]]).

### T1592.002: Software

^t1592002-software

Adversaries may gather information about the victim's host software that can be used during targeting. Information about installed software may include a variety of details such as types and versions on specific hosts, as well as the presence of additional components that might be indicative of added defensive protections (ex: antivirus, SIEMs, etc.).

Adversaries may gather this information in various ways, such as direct collection actions via [[T1595-active_scanning|T1595: Active Scanning]] (ex: listening ports, server banners, user agent strings) or [[T1598-phishing_for_information|T1598: Phishing for Information]]. Adversaries may also compromise sites then include malicious content designed to collect host information from visitors.(Citation: ATT ScanBox) Information about the installed software may also be exposed to adversaries via online or other accessible data sets (ex: job postings, network maps, assessment reports, resumes, or purchase invoices). Additionally, adversaries may analyze metadata from victim-owned files (e.g., PDFs, DOCs, images, and sound files hosted on victim-owned websites) to extract information about the software and hardware used to create or process those files. Metadata may reveal software versions, configurations, or timestamps that indicate outdated or vulnerable software. This information can be cross-referenced with known CVEs to identify potential vectors for exploitation in future operations.(Citation: Outpost24)

Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [[T1593-search_open_websites_domains|T1593: Search Open Websites/Domains]] or [[T1596-search_open_technical_databases|T1596: Search Open Technical Databases]]), establishing operational resources (ex: [[T1587-develop_capabilities|T1587: Develop Capabilities]] or [[T1588-obtain_capabilities|T1588: Obtain Capabilities]]), and/or for initial access (ex: [[T1195-supply_chain_compromise|T1195: Supply Chain Compromise]] or [[T1133-external_remote_services|T1133: External Remote Services]]).

### T1592.003: Firmware

^t1592003-firmware

Adversaries may gather information about the victim's host firmware that can be used during targeting. Information about host firmware may include a variety of details such as type and versions on specific hosts, which may be used to infer more information about hosts in the environment (ex: configuration, purpose, age/patch level, etc.).

Adversaries may gather this information in various ways, such as direct elicitation via [[T1598-phishing_for_information|T1598: Phishing for Information]]. Information about host firmware may only be exposed to adversaries via online or other accessible data sets (ex: job postings, network maps, assessment reports, resumes, or purchase invoices).(Citation: ArsTechnica Intel) Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [[T1593-search_open_websites_domains|T1593: Search Open Websites/Domains]] or [[T1596-search_open_technical_databases|T1596: Search Open Technical Databases]]), establishing operational resources (ex: [[T1587-develop_capabilities|T1587: Develop Capabilities]] or [[T1588-obtain_capabilities|T1588: Obtain Capabilities]]), and/or initial access (ex: [[T1195-supply_chain_compromise|T1195: Supply Chain Compromise]] or [[T1190-exploit_public-facing_application|T1190: Exploit Public-Facing Application]]).

### T1592.004: Client Configurations

^t1592004-client-configurations

Adversaries may gather information about the victim's client configurations that can be used during targeting. Information about client configurations may include a variety of details and settings, including operating system/version, virtualization, architecture (ex: 32 or 64 bit), language, and/or time zone.

Adversaries may gather this information in various ways, such as direct collection actions via [[T1595-active_scanning|T1595: Active Scanning]] (ex: listening ports, server banners, user agent strings) or [[T1598-phishing_for_information|T1598: Phishing for Information]]. Adversaries may also compromise sites then include malicious content designed to collect host information from visitors.(Citation: ATT ScanBox) Information about the client configurations may also be exposed to adversaries via online or other accessible data sets (ex: job postings, network maps, assessment reports, resumes, or purchase invoices). Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [[T1593-search_open_websites_domains|T1593: Search Open Websites/Domains]] or [[T1596-search_open_technical_databases|T1596: Search Open Technical Databases]]), establishing operational resources (ex: [[T1587-develop_capabilities|T1587: Develop Capabilities]] or [[T1588-obtain_capabilities|T1588: Obtain Capabilities]]), and/or initial access (ex: [[T1195-supply_chain_compromise|T1195: Supply Chain Compromise]] or [[T1133-external_remote_services|T1133: External Remote Services]]).

## Mitigations

- [[M1056-pre-compromise|M1056: Pre-compromise]]

## Platforms

- PRE

