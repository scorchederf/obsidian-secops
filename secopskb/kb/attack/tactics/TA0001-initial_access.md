---
mitre_id: "TA0001"
mitre_name: "Initial Access"
mitre_type: "x-mitre-tactic"
mitre_stix_id: "x-mitre-tactic--ffd5bcee-6e16-4dd2-8eca-7b3beedf33ca"
mitre_created: "2018-10-17T00:14:20.652Z"
mitre_modified: "2025-04-25T14:45:36.917Z"
mitre_version: "1.0"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/tactics/TA0001/"
framework: "attack"
generated: "true"
build_date: "2026-04-25 14:47:22"
build_source: "script"
object_type: "tactic"
tags:
  - "attack"
  - "tactic"
  - "offense"
mitre_shortname: "initial-access"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[notes/index|Notes]]

---

The adversary is trying to get into your network.

Initial Access consists of techniques that use various entry vectors to gain their initial foothold within a network. Techniques used to gain a foothold include targeted spearphishing and exploiting weaknesses on public-facing web servers. Footholds gained through initial access may allow for continued access, like valid accounts and use of external remote services, or may be limited-use due to changing passwords.

## Workspace

- [[notes/attack/tactics/TA0001-initial_access-note|Open workspace note]]

![[notes/attack/tactics/TA0001-initial_access-note]]

## Related Techniques

- [[T1078-valid_accounts|T1078: Valid Accounts]]
    - [[T1078-valid_accounts#^t1078001-default-accounts|T1078.001: Default Accounts]]
    - [[T1078-valid_accounts#^t1078002-domain-accounts|T1078.002: Domain Accounts]]
    - [[T1078-valid_accounts#^t1078003-local-accounts|T1078.003: Local Accounts]]
    - [[T1078-valid_accounts#^t1078004-cloud-accounts|T1078.004: Cloud Accounts]]
- [[T1091-replication_through_removable_media|T1091: Replication Through Removable Media]]
- [[T1133-external_remote_services|T1133: External Remote Services]]
- [[T1189-drive-by_compromise|T1189: Drive-by Compromise]]
- [[T1190-exploit_public-facing_application|T1190: Exploit Public-Facing Application]]
- [[T1195-supply_chain_compromise|T1195: Supply Chain Compromise]]
    - [[T1195-supply_chain_compromise#^t1195001-compromise-software-dependencies-and-development-tools|T1195.001: Compromise Software Dependencies and Development Tools]]
    - [[T1195-supply_chain_compromise#^t1195002-compromise-software-supply-chain|T1195.002: Compromise Software Supply Chain]]
    - [[T1195-supply_chain_compromise#^t1195003-compromise-hardware-supply-chain|T1195.003: Compromise Hardware Supply Chain]]
- [[T1199-trusted_relationship|T1199: Trusted Relationship]]
- [[T1200-hardware_additions|T1200: Hardware Additions]]
- [[T1566-phishing|T1566: Phishing]]
    - [[T1566-phishing#^t1566001-spearphishing-attachment|T1566.001: Spearphishing Attachment]]
    - [[T1566-phishing#^t1566002-spearphishing-link|T1566.002: Spearphishing Link]]
    - [[T1566-phishing#^t1566003-spearphishing-via-service|T1566.003: Spearphishing via Service]]
    - [[T1566-phishing#^t1566004-spearphishing-voice|T1566.004: Spearphishing Voice]]
- [[T1659-content_injection|T1659: Content Injection]]
- [[T1669-wi-fi_networks|T1669: Wi-Fi Networks]]

