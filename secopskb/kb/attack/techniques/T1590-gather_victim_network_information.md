---
mitre_id: "T1590"
mitre_name: "Gather Victim Network Information"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--9d48cab2-7929-4812-ad22-f536665f0109"
mitre_created: "2020-10-02T15:45:17.628Z"
mitre_modified: "2025-10-24T17:49:08.938Z"
mitre_version: "1.0"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1590/"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

---

Adversaries may gather information about the victim's networks that can be used during targeting. Information about networks may include a variety of details, including administrative data (ex: IP ranges, domain names, etc.) as well as specifics regarding its topology and operations.

Adversaries may gather this information in various ways, such as direct collection actions via [[T1595-active_scanning|T1595: Active Scanning]] or [[T1598-phishing_for_information|T1598: Phishing for Information]]. Information about networks may also be exposed to adversaries via online or other accessible data sets (ex: [[T1596-search_open_technical_databases|T1596: Search Open Technical Databases]]).(Citation: WHOIS)(Citation: DNS Dumpster)(Citation: Circl Passive DNS) Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [[T1595-active_scanning|T1595: Active Scanning]] or [[T1593-search_open_websites_domains|T1593: Search Open Websites/Domains]]), establishing operational resources (ex: [[T1583-acquire_infrastructure|T1583: Acquire Infrastructure]] or [[T1584-compromise_infrastructure|T1584: Compromise Infrastructure]]), and/or initial access (ex: [[T1199-trusted_relationship|T1199: Trusted Relationship]]).

## Workspace

- [[workspaces/attack/techniques/T1590-gather_victim_network_information-note|Open workspace note]]

![[workspaces/attack/techniques/T1590-gather_victim_network_information-note]]

## Tactics

- [[TA0043-reconnaissance|TA0043: Reconnaissance]]

## Subtechniques

### T1590.001: Domain Properties

^t1590001-domain-properties

Adversaries may gather information about the victim's network domain(s) that can be used during targeting. Information about domains and their properties may include a variety of details, including what domain(s) the victim owns as well as administrative data (ex: name, registrar, etc.) and more directly actionable information such as contacts (email addresses and phone numbers), business addresses, and name servers.

Adversaries may gather this information in various ways, such as direct collection actions via [[T1595-active_scanning|T1595: Active Scanning]] or [[T1598-phishing_for_information|T1598: Phishing for Information]]. Information about victim domains and their properties may also be exposed to adversaries via online or other accessible data sets (ex: [[T1596-search_open_technical_databases#^t1596002-whois|T1596.002: WHOIS]]).(Citation: WHOIS)(Citation: DNS Dumpster)(Citation: Circl Passive DNS) Where third-party cloud providers are in use, this information may also be exposed through publicly available API endpoints, such as GetUserRealm and autodiscover in Office 365 environments.(Citation: Azure Active Directory Reconnaisance)(Citation: Office 265 Azure Domain Availability) Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [[T1596-search_open_technical_databases|T1596: Search Open Technical Databases]], [[T1593-search_open_websites_domains|T1593: Search Open Websites/Domains]], or [[T1598-phishing_for_information|T1598: Phishing for Information]]), establishing operational resources (ex: [[T1583-acquire_infrastructure|T1583: Acquire Infrastructure]] or [[T1584-compromise_infrastructure|T1584: Compromise Infrastructure]]), and/or initial access (ex: [[T1566-phishing|T1566: Phishing]]).

### T1590.002: DNS

^t1590002-dns

Adversaries may gather information about the victim's DNS that can be used during targeting. DNS information may include a variety of details, including registered name servers as well as records that outline addressing for a target’s subdomains, mail servers, and other hosts. DNS MX, TXT, and SPF records may also reveal the use of third party cloud and SaaS providers, such as Office 365, G Suite, Salesforce, or Zendesk.(Citation: Sean Metcalf Twitter DNS Records)

Adversaries may gather this information in various ways, such as querying or otherwise collecting details via [[T1596-search_open_technical_databases#^t1596001-dns-passive-dns|T1596.001: DNS/Passive DNS]]. DNS information may also be exposed to adversaries via online or other accessible data sets (ex: [[T1596-search_open_technical_databases|T1596: Search Open Technical Databases]]).(Citation: DNS Dumpster)(Citation: Circl Passive DNS) Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [[T1596-search_open_technical_databases|T1596: Search Open Technical Databases]], [[T1593-search_open_websites_domains|T1593: Search Open Websites/Domains]], or [[T1595-active_scanning|T1595: Active Scanning]]), establishing operational resources (ex: [[T1583-acquire_infrastructure|T1583: Acquire Infrastructure]] or [[T1584-compromise_infrastructure|T1584: Compromise Infrastructure]]), and/or initial access (ex: [[T1133-external_remote_services|T1133: External Remote Services]]).

Adversaries may also use DNS zone transfer (DNS query type AXFR) to collect all records from a misconfigured DNS server.(Citation: Trails-DNS)(Citation: DNS-CISA)(Citation: Alexa-dns)

### T1590.003: Network Trust Dependencies

^t1590003-network-trust-dependencies

Adversaries may gather information about the victim's network trust dependencies that can be used during targeting. Information about network trusts may include a variety of details, including second or third-party organizations/domains (ex: managed service providers, contractors, etc.) that have connected (and potentially elevated) network access.

Adversaries may gather this information in various ways, such as direct elicitation via [[T1598-phishing_for_information|T1598: Phishing for Information]]. Information about network trusts may also be exposed to adversaries via online or other accessible data sets (ex: [[T1596-search_open_technical_databases|T1596: Search Open Technical Databases]]).(Citation: Pentesting AD Forests) Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [[T1595-active_scanning|T1595: Active Scanning]] or [[T1593-search_open_websites_domains|T1593: Search Open Websites/Domains]]), establishing operational resources (ex: [[T1583-acquire_infrastructure|T1583: Acquire Infrastructure]] or [[T1584-compromise_infrastructure|T1584: Compromise Infrastructure]]), and/or initial access (ex: [[T1199-trusted_relationship|T1199: Trusted Relationship]]).

### T1590.004: Network Topology

^t1590004-network-topology

Adversaries may gather information about the victim's network topology that can be used during targeting. Information about network topologies may include a variety of details, including the physical and/or logical arrangement of both external-facing and internal network environments. This information may also include specifics regarding network devices (gateways, routers, etc.) and other infrastructure.

Adversaries may gather this information in various ways, such as direct collection actions via [[T1595-active_scanning|T1595: Active Scanning]] or [[T1598-phishing_for_information|T1598: Phishing for Information]]. Information about network topologies may also be exposed to adversaries via online or other accessible data sets (ex: [[T1594-search_victim-owned_websites|T1594: Search Victim-Owned Websites]]).(Citation: DNS Dumpster) Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [[T1596-search_open_technical_databases|T1596: Search Open Technical Databases]] or [[T1593-search_open_websites_domains|T1593: Search Open Websites/Domains]]), establishing operational resources (ex: [[T1583-acquire_infrastructure|T1583: Acquire Infrastructure]] or [[T1584-compromise_infrastructure|T1584: Compromise Infrastructure]]), and/or initial access (ex: [[T1133-external_remote_services|T1133: External Remote Services]]).

### T1590.005: IP Addresses

^t1590005-ip-addresses

Adversaries may gather the victim's IP addresses that can be used during targeting. Public IP addresses may be allocated to organizations by block, or a range of sequential addresses. Information about assigned IP addresses may include a variety of details, such as which IP addresses are in use. IP addresses may also enable an adversary to derive other details about a victim, such as organizational size, physical location(s), Internet service provider, and or where/how their publicly-facing infrastructure is hosted.

Adversaries may gather this information in various ways, such as direct collection actions via [[T1595-active_scanning|T1595: Active Scanning]] or [[T1598-phishing_for_information|T1598: Phishing for Information]]. Information about assigned IP addresses may also be exposed to adversaries via online or other accessible data sets (ex: [[T1596-search_open_technical_databases|T1596: Search Open Technical Databases]]).(Citation: WHOIS)(Citation: DNS Dumpster)(Citation: Circl Passive DNS) Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [[T1595-active_scanning|T1595: Active Scanning]] or [[T1593-search_open_websites_domains|T1593: Search Open Websites/Domains]]), establishing operational resources (ex: [[T1583-acquire_infrastructure|T1583: Acquire Infrastructure]] or [[T1584-compromise_infrastructure|T1584: Compromise Infrastructure]]), and/or initial access (ex: [[T1133-external_remote_services|T1133: External Remote Services]]).

### T1590.006: Network Security Appliances

^t1590006-network-security-appliances

Adversaries may gather information about the victim's network security appliances that can be used during targeting. Information about network security appliances may include a variety of details, such as the existence and specifics of deployed firewalls, content filters, and proxies/bastion hosts. Adversaries may also target information about victim network-based intrusion detection systems (NIDS) or other appliances related to defensive cybersecurity operations.

Adversaries may gather this information in various ways, such as direct collection actions via [[T1595-active_scanning|T1595: Active Scanning]] or [[T1598-phishing_for_information|T1598: Phishing for Information]].(Citation: Nmap Firewalls NIDS) Information about network security appliances may also be exposed to adversaries via online or other accessible data sets (ex: [[T1594-search_victim-owned_websites|T1594: Search Victim-Owned Websites]]). Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [[T1596-search_open_technical_databases|T1596: Search Open Technical Databases]] or [[T1593-search_open_websites_domains|T1593: Search Open Websites/Domains]]), establishing operational resources (ex: [[T1587-develop_capabilities|T1587: Develop Capabilities]] or [[T1588-obtain_capabilities|T1588: Obtain Capabilities]]), and/or initial access (ex: [[T1133-external_remote_services|T1133: External Remote Services]]).

## Mitigations

- [[M1056-pre-compromise|M1056: Pre-compromise]]

## Platforms

- PRE

