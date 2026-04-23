---
mitre_id: "T1596"
mitre_name: "Search Open Technical Databases"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--55fc4df0-b42c-479a-b860-7a6761bcaad0"
mitre_created: "2020-10-02T16:56:05.810Z"
mitre_modified: "2025-10-24T17:48:48.734Z"
mitre_version: "1.0"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1596/"
build_date: "2026-04-23 20:16:46"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "PRE"
mitre_tactic_ids:
  - "TA0043"
---

# T1596: Search Open Technical Databases

Adversaries may search freely available technical databases for information about victims that can be used during targeting. Information about victims may be available in online databases and repositories, such as registrations of domains/certificates as well as public collections of network data/artifacts gathered from traffic and/or scans.(Citation: WHOIS)(Citation: DNS Dumpster)(Citation: Circl Passive DNS)(Citation: Medium SSL Cert)(Citation: SSLShopper Lookup)(Citation: DigitalShadows CDN)(Citation: Shodan)

Adversaries may search in different open databases depending on what information they seek to gather. Information from these sources may reveal opportunities for other forms of reconnaissance (ex: [[T1598-phishing_for_information|T1598: Phishing for Information]] or [[T1593-search_open_websites_domains|T1593: Search Open Websites/Domains]]), establishing operational resources (ex: [[T1583-acquire_infrastructure|T1583: Acquire Infrastructure]] or [[T1584-compromise_infrastructure|T1584: Compromise Infrastructure]]), and/or initial access (ex: [[T1133-external_remote_services|T1133: External Remote Services]] or [[T1199-trusted_relationship|T1199: Trusted Relationship]]).

## Tactics

- [[TA0043-reconnaissance|TA0043: Reconnaissance]]

## Subtechniques

### T1596.001: DNS/Passive DNS

^t1596001-dns-passive-dns

Adversaries may search DNS data for information about victims that can be used during targeting. DNS information may include a variety of details, including registered name servers as well as records that outline addressing for a target’s subdomains, mail servers, and other hosts.

Adversaries may search DNS data to gather actionable information. Threat actors can query nameservers for a target organization directly, or search through centralized repositories of logged DNS query responses (known as passive DNS).(Citation: DNS Dumpster)(Citation: Circl Passive DNS) Adversaries may also seek and target DNS misconfigurations/leaks that reveal information about internal networks. Information from these sources may reveal opportunities for other forms of reconnaissance (ex: [[T1594-search_victim-owned_websites|T1594: Search Victim-Owned Websites]] or [[T1593-search_open_websites_domains|T1593: Search Open Websites/Domains]]), establishing operational resources (ex: [[T1583-acquire_infrastructure|T1583: Acquire Infrastructure]] or [[T1584-compromise_infrastructure|T1584: Compromise Infrastructure]]), and/or initial access (ex: [[T1133-external_remote_services|T1133: External Remote Services]] or [[T1199-trusted_relationship|T1199: Trusted Relationship]]).

### T1596.002: WHOIS

^t1596002-whois

Adversaries may search public WHOIS data for information about victims that can be used during targeting. WHOIS data is stored by regional Internet registries (RIR) responsible for allocating and assigning Internet resources such as domain names. Anyone can query WHOIS servers for information about a registered domain, such as assigned IP blocks, contact information, and DNS nameservers.(Citation: WHOIS)

Adversaries may search WHOIS data to gather actionable information. Threat actors can use online resources or command-line utilities to pillage through WHOIS data for information about potential victims. Information from these sources may reveal opportunities for other forms of reconnaissance (ex: [[T1595-active_scanning|T1595: Active Scanning]] or [[T1598-phishing_for_information|T1598: Phishing for Information]]), establishing operational resources (ex: [[T1583-acquire_infrastructure|T1583: Acquire Infrastructure]] or [[T1584-compromise_infrastructure|T1584: Compromise Infrastructure]]), and/or initial access (ex: [[T1133-external_remote_services|T1133: External Remote Services]] or [[T1199-trusted_relationship|T1199: Trusted Relationship]]).

### T1596.003: Digital Certificates

^t1596003-digital-certificates

Adversaries may search public digital certificate data for information about victims that can be used during targeting. Digital certificates are issued by a certificate authority (CA) in order to cryptographically verify the origin of signed content. These certificates, such as those used for encrypted web traffic (HTTPS SSL/TLS communications), contain information about the registered organization such as name and location.

Adversaries may search digital certificate data to gather actionable information. Threat actors can use online resources and lookup tools to harvest information about certificates.(Citation: SSLShopper Lookup) Digital certificate data may also be available from artifacts signed by the organization (ex: certificates used from encrypted web traffic are served with content).(Citation: Medium SSL Cert) Information from these sources may reveal opportunities for other forms of reconnaissance (ex: [[T1595-active_scanning|T1595: Active Scanning]] or [[T1598-phishing_for_information|T1598: Phishing for Information]]), establishing operational resources (ex: [[T1587-develop_capabilities|T1587: Develop Capabilities]] or [[T1588-obtain_capabilities|T1588: Obtain Capabilities]]), and/or initial access (ex: [[T1133-external_remote_services|T1133: External Remote Services]] or [[T1199-trusted_relationship|T1199: Trusted Relationship]]).

### T1596.004: CDNs

^t1596004-cdns

Adversaries may search content delivery network (CDN) data about victims that can be used during targeting. CDNs allow an organization to host content from a distributed, load balanced array of servers. CDNs may also allow organizations to customize content delivery based on the requestor’s geographical region.

Adversaries may search CDN data to gather actionable information. Threat actors can use online resources and lookup tools to harvest information about content servers within a CDN. Adversaries may also seek and target CDN misconfigurations that leak sensitive information not intended to be hosted and/or do not have the same protection mechanisms (ex: login portals) as the content hosted on the organization’s website.(Citation: DigitalShadows CDN) Information from these sources may reveal opportunities for other forms of reconnaissance (ex: [[T1595-active_scanning|T1595: Active Scanning]] or [[T1593-search_open_websites_domains|T1593: Search Open Websites/Domains]]), establishing operational resources (ex: [[T1583-acquire_infrastructure|T1583: Acquire Infrastructure]] or [[T1584-compromise_infrastructure|T1584: Compromise Infrastructure]]), and/or initial access (ex: [[T1189-drive-by_compromise|T1189: Drive-by Compromise]]).

### T1596.005: Scan Databases

^t1596005-scan-databases

Adversaries may search within public scan databases for information about victims that can be used during targeting. Various online services continuously publish the results of Internet scans/surveys, often harvesting information such as active IP addresses, hostnames, open ports, certificates, and even server banners.(Citation: Shodan)

Adversaries may search scan databases to gather actionable information. Threat actors can use online resources and lookup tools to harvest information from these services. Adversaries may seek information about their already identified targets, or use these datasets to discover opportunities for successful breaches. Information from these sources may reveal opportunities for other forms of reconnaissance (ex: [[T1595-active_scanning|T1595: Active Scanning]] or [[T1593-search_open_websites_domains|T1593: Search Open Websites/Domains]]), establishing operational resources (ex: [[T1587-develop_capabilities|T1587: Develop Capabilities]] or [[T1588-obtain_capabilities|T1588: Obtain Capabilities]]), and/or initial access (ex: [[T1133-external_remote_services|T1133: External Remote Services]] or [[T1190-exploit_public-facing_application|T1190: Exploit Public-Facing Application]]).

## Mitigations

- [[M1056-pre-compromise|M1056: Pre-compromise]]

## Platforms

- PRE

