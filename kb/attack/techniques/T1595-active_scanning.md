---
mitre_id: "T1595"
mitre_name: "Active Scanning"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--67073dde-d720-45ae-83da-b12d5e73ca3b"
mitre_created: "2020-10-02T16:53:16.526Z"
mitre_modified: "2025-10-24T17:48:53.018Z"
mitre_version: "1.0"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1595/"
framework: "attack"
generated: "true"
build_date: "2026-04-23 22:40:56"
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

# T1595: Active Scanning

Adversaries may execute active reconnaissance scans to gather information that can be used during targeting. Active scans are those where the adversary probes victim infrastructure via network traffic, as opposed to other forms of reconnaissance that do not involve direct interaction.

Adversaries may perform different forms of active scanning depending on what information they seek to gather. These scans can also be performed in various ways, including using native features of network protocols such as ICMP.(Citation: Botnet Scan)(Citation: OWASP Fingerprinting) Information from these scans may reveal opportunities for other forms of reconnaissance (ex: [[T1593-search_open_websites_domains|T1593: Search Open Websites/Domains]] or [[T1596-search_open_technical_databases|T1596: Search Open Technical Databases]]), establishing operational resources (ex: [[T1587-develop_capabilities|T1587: Develop Capabilities]] or [[T1588-obtain_capabilities|T1588: Obtain Capabilities]]), and/or initial access (ex: [[T1133-external_remote_services|T1133: External Remote Services]] or [[T1190-exploit_public-facing_application|T1190: Exploit Public-Facing Application]]).

## Tactics

- [[TA0043-reconnaissance|TA0043: Reconnaissance]]

## Subtechniques

### T1595.001: Scanning IP Blocks

^t1595001-scanning-ip-blocks

Adversaries may scan victim IP blocks to gather information that can be used during targeting. Public IP addresses may be allocated to organizations by block, or a range of sequential addresses.

Adversaries may scan IP blocks in order to [[T1590-gather_victim_network_information|T1590: Gather Victim Network Information]], such as which IP addresses are actively in use as well as more detailed information about hosts assigned these addresses. Scans may range from simple pings (ICMP requests and responses) to more nuanced scans that may reveal host software/versions via server banners or other network artifacts.(Citation: Botnet Scan) Information from these scans may reveal opportunities for other forms of reconnaissance (ex: [[T1593-search_open_websites_domains|T1593: Search Open Websites/Domains]] or [[T1596-search_open_technical_databases|T1596: Search Open Technical Databases]]), establishing operational resources (ex: [[T1587-develop_capabilities|T1587: Develop Capabilities]] or [[T1588-obtain_capabilities|T1588: Obtain Capabilities]]), and/or initial access (ex: [[T1133-external_remote_services|T1133: External Remote Services]]).

### T1595.002: Vulnerability Scanning

^t1595002-vulnerability-scanning

Adversaries may scan victims for vulnerabilities that can be used during targeting. Vulnerability scans typically check if the configuration of a target host/application (ex: software and version) potentially aligns with the target of a specific exploit the adversary may seek to use.

These scans may also include more broad attempts to [[T1592-gather_victim_host_information|T1592: Gather Victim Host Information]] that can be used to identify more commonly known, exploitable vulnerabilities. Vulnerability scans typically harvest running software and version numbers via server banners, listening ports, or other network artifacts.(Citation: OWASP Vuln Scanning) Information from these scans may reveal opportunities for other forms of reconnaissance (ex: [[T1593-search_open_websites_domains|T1593: Search Open Websites/Domains]] or [[T1596-search_open_technical_databases|T1596: Search Open Technical Databases]]), establishing operational resources (ex: [[T1587-develop_capabilities|T1587: Develop Capabilities]] or [[T1588-obtain_capabilities|T1588: Obtain Capabilities]]), and/or initial access (ex: [[T1190-exploit_public-facing_application|T1190: Exploit Public-Facing Application]]).

### T1595.003: Wordlist Scanning

^t1595003-wordlist-scanning

Adversaries may iteratively probe infrastructure using brute-forcing and crawling techniques. While this technique employs similar methods to [[T1110-brute_force|T1110: Brute Force]], its goal is the identification of content and infrastructure rather than the discovery of valid credentials. Wordlists used in these scans may contain generic, commonly used names and file extensions or terms specific to a particular software. Adversaries may also create custom, target-specific wordlists using data gathered from other Reconnaissance techniques (ex: [[T1591-gather_victim_org_information|T1591: Gather Victim Org Information]], or [[T1594-search_victim-owned_websites|T1594: Search Victim-Owned Websites]]).

For example, adversaries may use web content discovery tools such as Dirb, DirBuster, and GoBuster and generic or custom wordlists to enumerate a website’s pages and directories.(Citation: ClearSky Lebanese Cedar Jan 2021) This can help them to discover old, vulnerable pages or hidden administrative portals that could become the target of further operations (ex: [[T1190-exploit_public-facing_application|T1190: Exploit Public-Facing Application]] or [[T1110-brute_force|T1110: Brute Force]]).  

As cloud storage solutions typically use globally unique names, adversaries may also use target-specific wordlists and tools such as s3recon and GCPBucketBrute to enumerate public and private buckets on cloud infrastructure.(Citation: S3Recon GitHub)(Citation: GCPBucketBrute) Once storage objects are discovered, adversaries may leverage [[T1530-data_from_cloud_storage|T1530: Data from Cloud Storage]] to access valuable information that can be exfiltrated or used to escalate privileges and move laterally. 

## Mitigations

- [[M1056-pre-compromise|M1056: Pre-compromise]]

## Platforms

- PRE

## Workspace

- [[kb/notes/attack/techniques/t1595-notes|Open workspace note]]

