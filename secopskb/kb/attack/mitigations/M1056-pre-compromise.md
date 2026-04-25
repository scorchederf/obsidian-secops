---
mitre_id: "M1056"
mitre_name: "Pre-compromise"
mitre_type: "course-of-action"
mitre_stix_id: "course-of-action--78bb71be-92b4-46de-acd6-5f998fedf1cc"
mitre_created: "2020-10-19T14:57:58.771Z"
mitre_modified: "2024-12-18T18:24:37.835Z"
mitre_version: "1.1"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/mitigations/M1056/"
framework: "attack"
generated: "true"
build_date: "2026-04-25 14:47:22"
build_source: "script"
object_type: "mitigation"
tags:
  - "attack"
  - "mitigation"
  - "defense"
  - "countermeasure"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[notes/index|Notes]]

---

Pre-compromise mitigations involve proactive measures and defenses implemented to prevent adversaries from successfully identifying and exploiting weaknesses during the Reconnaissance and Resource Development phases of an attack. These activities focus on reducing an organization's attack surface, identify adversarial preparation efforts, and increase the difficulty for attackers to conduct successful operations. This mitigation can be implemented through the following measures:

Limit Information Exposure:

- Regularly audit and sanitize publicly available data, including job posts, websites, and social media.
- Use tools like OSINT monitoring platforms (e.g., SpiderFoot, Recon-ng) to identify leaked information.

Protect Domain and DNS Infrastructure:

- Enable DNSSEC and use WHOIS privacy protection.
- Monitor for domain hijacking or lookalike domains using services like RiskIQ or DomainTools.

External Monitoring:

- Use tools like Shodan, Censys to monitor your external attack surface.
- Deploy external vulnerability scanners to proactively address weaknesses.

Threat Intelligence:

- Leverage platforms like MISP, Recorded Future, or Anomali to track adversarial infrastructure, tools, and activity.

Content and Email Protections:

- Use email security solutions like Proofpoint, Microsoft Defender for Office 365, or Mimecast.
- Enforce SPF/DKIM/DMARC policies to protect against email spoofing.

Training and Awareness:

- Educate employees on identifying phishing attempts, securing their social media, and avoiding information leaks.

## Workspace

- [[notes/attack/mitigations/M1056-pre-compromise-note|Open workspace note]]

![[notes/attack/mitigations/M1056-pre-compromise-note]]

## Mitigates Techniques

- [[T1583-acquire_infrastructure|T1583: Acquire Infrastructure]]
- [[T1583-acquire_infrastructure|T1583: Acquire Infrastructure]]
    - [[T1583-acquire_infrastructure#^t1583001-domains|T1583.001: Domains]]
    - [[T1583-acquire_infrastructure#^t1583002-dns-server|T1583.002: DNS Server]]
    - [[T1583-acquire_infrastructure#^t1583003-virtual-private-server|T1583.003: Virtual Private Server]]
    - [[T1583-acquire_infrastructure#^t1583004-server|T1583.004: Server]]
    - [[T1583-acquire_infrastructure#^t1583005-botnet|T1583.005: Botnet]]
    - [[T1583-acquire_infrastructure#^t1583006-web-services|T1583.006: Web Services]]
    - [[T1583-acquire_infrastructure#^t1583007-serverless|T1583.007: Serverless]]
    - [[T1583-acquire_infrastructure#^t1583008-malvertising|T1583.008: Malvertising]]
- [[T1584-compromise_infrastructure|T1584: Compromise Infrastructure]]
- [[T1584-compromise_infrastructure|T1584: Compromise Infrastructure]]
    - [[T1584-compromise_infrastructure#^t1584001-domains|T1584.001: Domains]]
    - [[T1584-compromise_infrastructure#^t1584002-dns-server|T1584.002: DNS Server]]
    - [[T1584-compromise_infrastructure#^t1584003-virtual-private-server|T1584.003: Virtual Private Server]]
    - [[T1584-compromise_infrastructure#^t1584004-server|T1584.004: Server]]
    - [[T1584-compromise_infrastructure#^t1584005-botnet|T1584.005: Botnet]]
    - [[T1584-compromise_infrastructure#^t1584006-web-services|T1584.006: Web Services]]
    - [[T1584-compromise_infrastructure#^t1584007-serverless|T1584.007: Serverless]]
    - [[T1584-compromise_infrastructure#^t1584008-network-devices|T1584.008: Network Devices]]
- [[T1585-establish_accounts|T1585: Establish Accounts]]
- [[T1585-establish_accounts|T1585: Establish Accounts]]
    - [[T1585-establish_accounts#^t1585001-social-media-accounts|T1585.001: Social Media Accounts]]
    - [[T1585-establish_accounts#^t1585002-email-accounts|T1585.002: Email Accounts]]
    - [[T1585-establish_accounts#^t1585003-cloud-accounts|T1585.003: Cloud Accounts]]
- [[T1586-compromise_accounts|T1586: Compromise Accounts]]
- [[T1586-compromise_accounts|T1586: Compromise Accounts]]
    - [[T1586-compromise_accounts#^t1586001-social-media-accounts|T1586.001: Social Media Accounts]]
    - [[T1586-compromise_accounts#^t1586002-email-accounts|T1586.002: Email Accounts]]
    - [[T1586-compromise_accounts#^t1586003-cloud-accounts|T1586.003: Cloud Accounts]]
- [[T1587-develop_capabilities|T1587: Develop Capabilities]]
- [[T1587-develop_capabilities|T1587: Develop Capabilities]]
    - [[T1587-develop_capabilities#^t1587001-malware|T1587.001: Malware]]
    - [[T1587-develop_capabilities#^t1587002-code-signing-certificates|T1587.002: Code Signing Certificates]]
    - [[T1587-develop_capabilities#^t1587003-digital-certificates|T1587.003: Digital Certificates]]
    - [[T1587-develop_capabilities#^t1587004-exploits|T1587.004: Exploits]]
- [[T1588-obtain_capabilities|T1588: Obtain Capabilities]]
- [[T1588-obtain_capabilities|T1588: Obtain Capabilities]]
    - [[T1588-obtain_capabilities#^t1588001-malware|T1588.001: Malware]]
    - [[T1588-obtain_capabilities#^t1588002-tool|T1588.002: Tool]]
    - [[T1588-obtain_capabilities#^t1588003-code-signing-certificates|T1588.003: Code Signing Certificates]]
    - [[T1588-obtain_capabilities#^t1588004-digital-certificates|T1588.004: Digital Certificates]]
    - [[T1588-obtain_capabilities#^t1588005-exploits|T1588.005: Exploits]]
    - [[T1588-obtain_capabilities#^t1588006-vulnerabilities|T1588.006: Vulnerabilities]]
    - [[T1588-obtain_capabilities#^t1588007-artificial-intelligence|T1588.007: Artificial Intelligence]]
- [[T1589-gather_victim_identity_information|T1589: Gather Victim Identity Information]]
- [[T1589-gather_victim_identity_information|T1589: Gather Victim Identity Information]]
    - [[T1589-gather_victim_identity_information#^t1589001-credentials|T1589.001: Credentials]]
    - [[T1589-gather_victim_identity_information#^t1589002-email-addresses|T1589.002: Email Addresses]]
    - [[T1589-gather_victim_identity_information#^t1589003-employee-names|T1589.003: Employee Names]]
- [[T1590-gather_victim_network_information|T1590: Gather Victim Network Information]]
- [[T1590-gather_victim_network_information|T1590: Gather Victim Network Information]]
    - [[T1590-gather_victim_network_information#^t1590001-domain-properties|T1590.001: Domain Properties]]
    - [[T1590-gather_victim_network_information#^t1590003-network-trust-dependencies|T1590.003: Network Trust Dependencies]]
    - [[T1590-gather_victim_network_information#^t1590004-network-topology|T1590.004: Network Topology]]
    - [[T1590-gather_victim_network_information#^t1590005-ip-addresses|T1590.005: IP Addresses]]
    - [[T1590-gather_victim_network_information#^t1590006-network-security-appliances|T1590.006: Network Security Appliances]]
- [[T1591-gather_victim_org_information|T1591: Gather Victim Org Information]]
- [[T1591-gather_victim_org_information|T1591: Gather Victim Org Information]]
    - [[T1591-gather_victim_org_information#^t1591001-determine-physical-locations|T1591.001: Determine Physical Locations]]
    - [[T1591-gather_victim_org_information#^t1591002-business-relationships|T1591.002: Business Relationships]]
    - [[T1591-gather_victim_org_information#^t1591003-identify-business-tempo|T1591.003: Identify Business Tempo]]
    - [[T1591-gather_victim_org_information#^t1591004-identify-roles|T1591.004: Identify Roles]]
- [[T1592-gather_victim_host_information|T1592: Gather Victim Host Information]]
- [[T1592-gather_victim_host_information|T1592: Gather Victim Host Information]]
    - [[T1592-gather_victim_host_information#^t1592001-hardware|T1592.001: Hardware]]
    - [[T1592-gather_victim_host_information#^t1592002-software|T1592.002: Software]]
    - [[T1592-gather_victim_host_information#^t1592003-firmware|T1592.003: Firmware]]
    - [[T1592-gather_victim_host_information#^t1592004-client-configurations|T1592.004: Client Configurations]]
- [[T1593-search_open_websites_domains|T1593: Search Open Websites/Domains]]
    - [[T1593-search_open_websites_domains#^t1593001-social-media|T1593.001: Social Media]]
    - [[T1593-search_open_websites_domains#^t1593002-search-engines|T1593.002: Search Engines]]
- [[T1594-search_victim-owned_websites|T1594: Search Victim-Owned Websites]]
- [[T1595-active_scanning|T1595: Active Scanning]]
- [[T1595-active_scanning|T1595: Active Scanning]]
    - [[T1595-active_scanning#^t1595001-scanning-ip-blocks|T1595.001: Scanning IP Blocks]]
    - [[T1595-active_scanning#^t1595002-vulnerability-scanning|T1595.002: Vulnerability Scanning]]
    - [[T1595-active_scanning#^t1595003-wordlist-scanning|T1595.003: Wordlist Scanning]]
- [[T1596-search_open_technical_databases|T1596: Search Open Technical Databases]]
- [[T1596-search_open_technical_databases|T1596: Search Open Technical Databases]]
    - [[T1596-search_open_technical_databases#^t1596001-dns-passive-dns|T1596.001: DNS/Passive DNS]]
    - [[T1596-search_open_technical_databases#^t1596002-whois|T1596.002: WHOIS]]
    - [[T1596-search_open_technical_databases#^t1596003-digital-certificates|T1596.003: Digital Certificates]]
    - [[T1596-search_open_technical_databases#^t1596004-cdns|T1596.004: CDNs]]
    - [[T1596-search_open_technical_databases#^t1596005-scan-databases|T1596.005: Scan Databases]]
- [[T1597-search_closed_sources|T1597: Search Closed Sources]]
- [[T1597-search_closed_sources|T1597: Search Closed Sources]]
    - [[T1597-search_closed_sources#^t1597001-threat-intel-vendors|T1597.001: Threat Intel Vendors]]
    - [[T1597-search_closed_sources#^t1597002-purchase-technical-data|T1597.002: Purchase Technical Data]]
- [[T1608-stage_capabilities|T1608: Stage Capabilities]]
- [[T1608-stage_capabilities|T1608: Stage Capabilities]]
    - [[T1608-stage_capabilities#^t1608001-upload-malware|T1608.001: Upload Malware]]
    - [[T1608-stage_capabilities#^t1608002-upload-tool|T1608.002: Upload Tool]]
    - [[T1608-stage_capabilities#^t1608003-install-digital-certificate|T1608.003: Install Digital Certificate]]
    - [[T1608-stage_capabilities#^t1608004-drive-by-target|T1608.004: Drive-by Target]]
    - [[T1608-stage_capabilities#^t1608005-link-target|T1608.005: Link Target]]
    - [[T1608-stage_capabilities#^t1608006-seo-poisoning|T1608.006: SEO Poisoning]]
- [[T1650-acquire_access|T1650: Acquire Access]]
- [[T1681-search_threat_vendor_data|T1681: Search Threat Vendor Data]]

