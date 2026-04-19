---
id: T1590
name: Gather Victim Network Information
created: 2020-10-02 15:45:17.628000+00:00
modified: 2025-10-24 17:49:08.938000+00:00
type: attack-pattern
x_mitre_version: 1.0
x_mitre_domains: enterprise-attack
---

## Tactic

- [[reconnaissance|Reconnaissance]]

Adversaries may gather information about the victim's networks that can be used during targeting. Information about networks may include a variety of details, including administrative data (ex: IP ranges, domain names, etc.) as well as specifics regarding its topology and operations.

Adversaries may gather this information in various ways, such as direct collection actions via [Active Scanning](https://attack.mitre.org/techniques/T1595) or [Phishing for Information](https://attack.mitre.org/techniques/T1598). Information about networks may also be exposed to adversaries via online or other accessible data sets (ex: [Search Open Technical Databases](https://attack.mitre.org/techniques/T1596)).(Citation: WHOIS)(Citation: DNS Dumpster)(Citation: Circl Passive DNS) Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [Active Scanning](https://attack.mitre.org/techniques/T1595) or [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593)), establishing operational resources (ex: [Acquire Infrastructure](https://attack.mitre.org/techniques/T1583) or [Compromise Infrastructure](https://attack.mitre.org/techniques/T1584)), and/or initial access (ex: [Trusted Relationship](https://attack.mitre.org/techniques/T1199)).

## Subtechniques

### T1590.001: Domain Properties
^t1590001-domain-properties

**Parent Technique**
- [[T1590-gather_victim_network_information|T1590: Gather Victim Network Information]]

**Tactic**
- [[reconnaissance|Reconnaissance]]

Adversaries may gather information about the victim's network domain(s) that can be used during targeting. Information about domains and their properties may include a variety of details, including what domain(s) the victim owns as well as administrative data (ex: name, registrar, etc.) and more directly actionable information such as contacts (email addresses and phone numbers), business addresses, and name servers.

Adversaries may gather this information in various ways, such as direct collection actions via [Active Scanning](https://attack.mitre.org/techniques/T1595) or [Phishing for Information](https://attack.mitre.org/techniques/T1598). Information about victim domains and their properties may also be exposed to adversaries via online or other accessible data sets (ex: [WHOIS](https://attack.mitre.org/techniques/T1596/002)).(Citation: WHOIS)(Citation: DNS Dumpster)(Citation: Circl Passive DNS) Where third-party cloud providers are in use, this information may also be exposed through publicly available API endpoints, such as GetUserRealm and autodiscover in Office 365 environments.(Citation: Azure Active Directory Reconnaisance)(Citation: Office 265 Azure Domain Availability) Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [Search Open Technical Databases](https://attack.mitre.org/techniques/T1596), [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593), or [Phishing for Information](https://attack.mitre.org/techniques/T1598)), establishing operational resources (ex: [Acquire Infrastructure](https://attack.mitre.org/techniques/T1583) or [Compromise Infrastructure](https://attack.mitre.org/techniques/T1584)), and/or initial access (ex: [Phishing](https://attack.mitre.org/techniques/T1566)).

#### Properties

- id: T1590.001
- name: Domain Properties
- created: 2020-10-02 15:46:24.670000+00:00
- modified: 2025-10-24 17:49:31.581000+00:00
- type: attack-pattern
- x_mitre_version: 1.1
- x_mitre_domains: enterprise-attack

### T1590.002: DNS
^t1590002-dns

**Parent Technique**
- [[T1590-gather_victim_network_information|T1590: Gather Victim Network Information]]

**Tactic**
- [[reconnaissance|Reconnaissance]]

Adversaries may gather information about the victim's DNS that can be used during targeting. DNS information may include a variety of details, including registered name servers as well as records that outline addressing for a target’s subdomains, mail servers, and other hosts. DNS MX, TXT, and SPF records may also reveal the use of third party cloud and SaaS providers, such as Office 365, G Suite, Salesforce, or Zendesk.(Citation: Sean Metcalf Twitter DNS Records)

Adversaries may gather this information in various ways, such as querying or otherwise collecting details via [DNS/Passive DNS](https://attack.mitre.org/techniques/T1596/001). DNS information may also be exposed to adversaries via online or other accessible data sets (ex: [Search Open Technical Databases](https://attack.mitre.org/techniques/T1596)).(Citation: DNS Dumpster)(Citation: Circl Passive DNS) Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [Search Open Technical Databases](https://attack.mitre.org/techniques/T1596), [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593), or [Active Scanning](https://attack.mitre.org/techniques/T1595)), establishing operational resources (ex: [Acquire Infrastructure](https://attack.mitre.org/techniques/T1583) or [Compromise Infrastructure](https://attack.mitre.org/techniques/T1584)), and/or initial access (ex: [External Remote Services](https://attack.mitre.org/techniques/T1133)).

Adversaries may also use DNS zone transfer (DNS query type AXFR) to collect all records from a misconfigured DNS server.(Citation: Trails-DNS)(Citation: DNS-CISA)(Citation: Alexa-dns)

#### Properties

- id: T1590.002
- name: DNS
- created: 2020-10-02 15:47:10.102000+00:00
- modified: 2025-10-24 17:48:24.404000+00:00
- type: attack-pattern
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

### T1590.003: Network Trust Dependencies
^t1590003-network-trust-dependencies

**Parent Technique**
- [[T1590-gather_victim_network_information|T1590: Gather Victim Network Information]]

**Tactic**
- [[reconnaissance|Reconnaissance]]

Adversaries may gather information about the victim's network trust dependencies that can be used during targeting. Information about network trusts may include a variety of details, including second or third-party organizations/domains (ex: managed service providers, contractors, etc.) that have connected (and potentially elevated) network access.

Adversaries may gather this information in various ways, such as direct elicitation via [Phishing for Information](https://attack.mitre.org/techniques/T1598). Information about network trusts may also be exposed to adversaries via online or other accessible data sets (ex: [Search Open Technical Databases](https://attack.mitre.org/techniques/T1596)).(Citation: Pentesting AD Forests) Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [Active Scanning](https://attack.mitre.org/techniques/T1595) or [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593)), establishing operational resources (ex: [Acquire Infrastructure](https://attack.mitre.org/techniques/T1583) or [Compromise Infrastructure](https://attack.mitre.org/techniques/T1584)), and/or initial access (ex: [Trusted Relationship](https://attack.mitre.org/techniques/T1199)).

#### Properties

- id: T1590.003
- name: Network Trust Dependencies
- created: 2020-10-02 15:47:59.457000+00:00
- modified: 2025-10-24 17:48:38.803000+00:00
- type: attack-pattern
- x_mitre_version: 1.0
- x_mitre_domains: enterprise-attack

### T1590.004: Network Topology
^t1590004-network-topology

**Parent Technique**
- [[T1590-gather_victim_network_information|T1590: Gather Victim Network Information]]

**Tactic**
- [[reconnaissance|Reconnaissance]]

Adversaries may gather information about the victim's network topology that can be used during targeting. Information about network topologies may include a variety of details, including the physical and/or logical arrangement of both external-facing and internal network environments. This information may also include specifics regarding network devices (gateways, routers, etc.) and other infrastructure.

Adversaries may gather this information in various ways, such as direct collection actions via [Active Scanning](https://attack.mitre.org/techniques/T1595) or [Phishing for Information](https://attack.mitre.org/techniques/T1598). Information about network topologies may also be exposed to adversaries via online or other accessible data sets (ex: [Search Victim-Owned Websites](https://attack.mitre.org/techniques/T1594)).(Citation: DNS Dumpster) Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [Search Open Technical Databases](https://attack.mitre.org/techniques/T1596) or [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593)), establishing operational resources (ex: [Acquire Infrastructure](https://attack.mitre.org/techniques/T1583) or [Compromise Infrastructure](https://attack.mitre.org/techniques/T1584)), and/or initial access (ex: [External Remote Services](https://attack.mitre.org/techniques/T1133)).

#### Properties

- id: T1590.004
- name: Network Topology
- created: 2020-10-02 15:49:03.815000+00:00
- modified: 2025-10-24 17:48:37.652000+00:00
- type: attack-pattern
- x_mitre_version: 1.0
- x_mitre_domains: enterprise-attack

### T1590.005: IP Addresses
^t1590005-ip-addresses

**Parent Technique**
- [[T1590-gather_victim_network_information|T1590: Gather Victim Network Information]]

**Tactic**
- [[reconnaissance|Reconnaissance]]

Adversaries may gather the victim's IP addresses that can be used during targeting. Public IP addresses may be allocated to organizations by block, or a range of sequential addresses. Information about assigned IP addresses may include a variety of details, such as which IP addresses are in use. IP addresses may also enable an adversary to derive other details about a victim, such as organizational size, physical location(s), Internet service provider, and or where/how their publicly-facing infrastructure is hosted.

Adversaries may gather this information in various ways, such as direct collection actions via [Active Scanning](https://attack.mitre.org/techniques/T1595) or [Phishing for Information](https://attack.mitre.org/techniques/T1598). Information about assigned IP addresses may also be exposed to adversaries via online or other accessible data sets (ex: [Search Open Technical Databases](https://attack.mitre.org/techniques/T1596)).(Citation: WHOIS)(Citation: DNS Dumpster)(Citation: Circl Passive DNS) Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [Active Scanning](https://attack.mitre.org/techniques/T1595) or [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593)), establishing operational resources (ex: [Acquire Infrastructure](https://attack.mitre.org/techniques/T1583) or [Compromise Infrastructure](https://attack.mitre.org/techniques/T1584)), and/or initial access (ex: [External Remote Services](https://attack.mitre.org/techniques/T1133)).

#### Properties

- id: T1590.005
- name: IP Addresses
- created: 2020-10-02 15:59:11.695000+00:00
- modified: 2025-10-24 17:48:23.845000+00:00
- type: attack-pattern
- x_mitre_version: 1.0
- x_mitre_domains: enterprise-attack

### T1590.006: Network Security Appliances
^t1590006-network-security-appliances

**Parent Technique**
- [[T1590-gather_victim_network_information|T1590: Gather Victim Network Information]]

**Tactic**
- [[reconnaissance|Reconnaissance]]

Adversaries may gather information about the victim's network security appliances that can be used during targeting. Information about network security appliances may include a variety of details, such as the existence and specifics of deployed firewalls, content filters, and proxies/bastion hosts. Adversaries may also target information about victim network-based intrusion detection systems (NIDS) or other appliances related to defensive cybersecurity operations.

Adversaries may gather this information in various ways, such as direct collection actions via [Active Scanning](https://attack.mitre.org/techniques/T1595) or [Phishing for Information](https://attack.mitre.org/techniques/T1598).(Citation: Nmap Firewalls NIDS) Information about network security appliances may also be exposed to adversaries via online or other accessible data sets (ex: [Search Victim-Owned Websites](https://attack.mitre.org/techniques/T1594)). Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [Search Open Technical Databases](https://attack.mitre.org/techniques/T1596) or [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593)), establishing operational resources (ex: [Develop Capabilities](https://attack.mitre.org/techniques/T1587) or [Obtain Capabilities](https://attack.mitre.org/techniques/T1588)), and/or initial access (ex: [External Remote Services](https://attack.mitre.org/techniques/T1133)).

#### Properties

- id: T1590.006
- name: Network Security Appliances
- created: 2020-10-02 16:01:35.350000+00:00
- modified: 2025-10-24 17:48:55.360000+00:00
- type: attack-pattern
- x_mitre_version: 1.0
- x_mitre_domains: enterprise-attack

## Mitigations

- [[M1056-pre-compromise|M1056: Pre-compromise]]

## Platforms

- PRE

