---
mitre_id: "TA0043"
mitre_name: "Reconnaissance"
mitre_type: "x-mitre-tactic"
mitre_stix_id: "x-mitre-tactic--daa4cbb1-b4f4-4723-a824-7f1efd6e0592"
mitre_created: "2020-10-02T14:48:41.809Z"
mitre_modified: "2025-04-25T14:45:36.201Z"
mitre_version: "1.0"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/tactics/TA0043/"
framework: "attack"
generated: "true"
build_date: "2026-04-25 20:43:29"
build_source: "script"
object_type: "tactic"
tags:
  - "attack"
  - "tactic"
  - "offense"
mitre_shortname: "reconnaissance"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

The adversary is trying to gather information they can use to plan future operations.

Reconnaissance consists of techniques that involve adversaries actively or passively gathering information that can be used to support targeting. Such information may include details of the victim organization, infrastructure, or staff/personnel. This information can be leveraged by the adversary to aid in other phases of the adversary lifecycle, such as using gathered information to plan and execute Initial Access, to scope and prioritize post-compromise objectives, or to drive and lead further Reconnaissance efforts.

## Workspace

- [[workspaces/attack/tactics/TA0043-reconnaissance-note|Open workspace note]]

![[workspaces/attack/tactics/TA0043-reconnaissance-note]]

## Related Techniques

- [[T1589-gather_victim_identity_information|T1589: Gather Victim Identity Information]]
    - [[T1589-gather_victim_identity_information#^t1589001-credentials|T1589.001: Credentials]]
    - [[T1589-gather_victim_identity_information#^t1589002-email-addresses|T1589.002: Email Addresses]]
    - [[T1589-gather_victim_identity_information#^t1589003-employee-names|T1589.003: Employee Names]]
- [[T1590-gather_victim_network_information|T1590: Gather Victim Network Information]]
    - [[T1590-gather_victim_network_information#^t1590001-domain-properties|T1590.001: Domain Properties]]
    - [[T1590-gather_victim_network_information#^t1590002-dns|T1590.002: DNS]]
    - [[T1590-gather_victim_network_information#^t1590003-network-trust-dependencies|T1590.003: Network Trust Dependencies]]
    - [[T1590-gather_victim_network_information#^t1590004-network-topology|T1590.004: Network Topology]]
    - [[T1590-gather_victim_network_information#^t1590005-ip-addresses|T1590.005: IP Addresses]]
    - [[T1590-gather_victim_network_information#^t1590006-network-security-appliances|T1590.006: Network Security Appliances]]
- [[T1591-gather_victim_org_information|T1591: Gather Victim Org Information]]
    - [[T1591-gather_victim_org_information#^t1591001-determine-physical-locations|T1591.001: Determine Physical Locations]]
    - [[T1591-gather_victim_org_information#^t1591002-business-relationships|T1591.002: Business Relationships]]
    - [[T1591-gather_victim_org_information#^t1591003-identify-business-tempo|T1591.003: Identify Business Tempo]]
    - [[T1591-gather_victim_org_information#^t1591004-identify-roles|T1591.004: Identify Roles]]
- [[T1592-gather_victim_host_information|T1592: Gather Victim Host Information]]
    - [[T1592-gather_victim_host_information#^t1592001-hardware|T1592.001: Hardware]]
    - [[T1592-gather_victim_host_information#^t1592002-software|T1592.002: Software]]
    - [[T1592-gather_victim_host_information#^t1592003-firmware|T1592.003: Firmware]]
    - [[T1592-gather_victim_host_information#^t1592004-client-configurations|T1592.004: Client Configurations]]
- [[T1593-search_open_websites_domains|T1593: Search Open Websites/Domains]]
    - [[T1593-search_open_websites_domains#^t1593001-social-media|T1593.001: Social Media]]
    - [[T1593-search_open_websites_domains#^t1593002-search-engines|T1593.002: Search Engines]]
    - [[T1593-search_open_websites_domains#^t1593003-code-repositories|T1593.003: Code Repositories]]
- [[T1594-search_victim-owned_websites|T1594: Search Victim-Owned Websites]]
- [[T1595-active_scanning|T1595: Active Scanning]]
    - [[T1595-active_scanning#^t1595001-scanning-ip-blocks|T1595.001: Scanning IP Blocks]]
    - [[T1595-active_scanning#^t1595002-vulnerability-scanning|T1595.002: Vulnerability Scanning]]
    - [[T1595-active_scanning#^t1595003-wordlist-scanning|T1595.003: Wordlist Scanning]]
- [[T1596-search_open_technical_databases|T1596: Search Open Technical Databases]]
    - [[T1596-search_open_technical_databases#^t1596001-dns-passive-dns|T1596.001: DNS/Passive DNS]]
    - [[T1596-search_open_technical_databases#^t1596002-whois|T1596.002: WHOIS]]
    - [[T1596-search_open_technical_databases#^t1596003-digital-certificates|T1596.003: Digital Certificates]]
    - [[T1596-search_open_technical_databases#^t1596004-cdns|T1596.004: CDNs]]
    - [[T1596-search_open_technical_databases#^t1596005-scan-databases|T1596.005: Scan Databases]]
- [[T1597-search_closed_sources|T1597: Search Closed Sources]]
    - [[T1597-search_closed_sources#^t1597001-threat-intel-vendors|T1597.001: Threat Intel Vendors]]
    - [[T1597-search_closed_sources#^t1597002-purchase-technical-data|T1597.002: Purchase Technical Data]]
- [[T1598-phishing_for_information|T1598: Phishing for Information]]
    - [[T1598-phishing_for_information#^t1598001-spearphishing-service|T1598.001: Spearphishing Service]]
    - [[T1598-phishing_for_information#^t1598002-spearphishing-attachment|T1598.002: Spearphishing Attachment]]
    - [[T1598-phishing_for_information#^t1598003-spearphishing-link|T1598.003: Spearphishing Link]]
    - [[T1598-phishing_for_information#^t1598004-spearphishing-voice|T1598.004: Spearphishing Voice]]
- [[T1681-search_threat_vendor_data|T1681: Search Threat Vendor Data]]

