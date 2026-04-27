---
mitre_id: "TA0042"
mitre_name: "Resource Development"
mitre_type: "x-mitre-tactic"
mitre_stix_id: "x-mitre-tactic--d679bca2-e57d-4935-8650-8031c87a4400"
mitre_created: "2020-09-30T16:11:59.650Z"
mitre_modified: "2025-04-25T14:45:35.841Z"
mitre_version: "1.0"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/tactics/TA0042/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "tactic"
tags:
  - "attack"
  - "tactic"
  - "offense"
mitre_shortname: "resource-development"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

The adversary is trying to establish resources they can use to support operations.

Resource Development consists of techniques that involve adversaries creating, purchasing, or compromising/stealing resources that can be used to support targeting. Such resources include infrastructure, accounts, or capabilities. These resources can be leveraged by the adversary to aid in other phases of the adversary lifecycle, such as using purchased domains to support Command and Control, email accounts for phishing as a part of Initial Access, or stealing code signing certificates to help with Defense Evasion.

## Workspace

- [[workspaces/attack/tactics/TA0042-resource_development-note|Open workspace note]]

![[workspaces/attack/tactics/TA0042-resource_development-note]]

## Related Techniques

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
    - [[T1584-compromise_infrastructure#^t1584001-domains|T1584.001: Domains]]
    - [[T1584-compromise_infrastructure#^t1584002-dns-server|T1584.002: DNS Server]]
    - [[T1584-compromise_infrastructure#^t1584003-virtual-private-server|T1584.003: Virtual Private Server]]
    - [[T1584-compromise_infrastructure#^t1584004-server|T1584.004: Server]]
    - [[T1584-compromise_infrastructure#^t1584005-botnet|T1584.005: Botnet]]
    - [[T1584-compromise_infrastructure#^t1584006-web-services|T1584.006: Web Services]]
    - [[T1584-compromise_infrastructure#^t1584007-serverless|T1584.007: Serverless]]
    - [[T1584-compromise_infrastructure#^t1584008-network-devices|T1584.008: Network Devices]]
- [[T1585-establish_accounts|T1585: Establish Accounts]]
    - [[T1585-establish_accounts#^t1585001-social-media-accounts|T1585.001: Social Media Accounts]]
    - [[T1585-establish_accounts#^t1585002-email-accounts|T1585.002: Email Accounts]]
    - [[T1585-establish_accounts#^t1585003-cloud-accounts|T1585.003: Cloud Accounts]]
- [[T1586-compromise_accounts|T1586: Compromise Accounts]]
    - [[T1586-compromise_accounts#^t1586001-social-media-accounts|T1586.001: Social Media Accounts]]
    - [[T1586-compromise_accounts#^t1586002-email-accounts|T1586.002: Email Accounts]]
    - [[T1586-compromise_accounts#^t1586003-cloud-accounts|T1586.003: Cloud Accounts]]
- [[T1587-develop_capabilities|T1587: Develop Capabilities]]
    - [[T1587-develop_capabilities#^t1587001-malware|T1587.001: Malware]]
    - [[T1587-develop_capabilities#^t1587002-code-signing-certificates|T1587.002: Code Signing Certificates]]
    - [[T1587-develop_capabilities#^t1587003-digital-certificates|T1587.003: Digital Certificates]]
    - [[T1587-develop_capabilities#^t1587004-exploits|T1587.004: Exploits]]
- [[T1588-obtain_capabilities|T1588: Obtain Capabilities]]
    - [[T1588-obtain_capabilities#^t1588001-malware|T1588.001: Malware]]
    - [[T1588-obtain_capabilities#^t1588002-tool|T1588.002: Tool]]
    - [[T1588-obtain_capabilities#^t1588003-code-signing-certificates|T1588.003: Code Signing Certificates]]
    - [[T1588-obtain_capabilities#^t1588004-digital-certificates|T1588.004: Digital Certificates]]
    - [[T1588-obtain_capabilities#^t1588005-exploits|T1588.005: Exploits]]
    - [[T1588-obtain_capabilities#^t1588006-vulnerabilities|T1588.006: Vulnerabilities]]
    - [[T1588-obtain_capabilities#^t1588007-artificial-intelligence|T1588.007: Artificial Intelligence]]
- [[T1608-stage_capabilities|T1608: Stage Capabilities]]
    - [[T1608-stage_capabilities#^t1608001-upload-malware|T1608.001: Upload Malware]]
    - [[T1608-stage_capabilities#^t1608002-upload-tool|T1608.002: Upload Tool]]
    - [[T1608-stage_capabilities#^t1608003-install-digital-certificate|T1608.003: Install Digital Certificate]]
    - [[T1608-stage_capabilities#^t1608004-drive-by-target|T1608.004: Drive-by Target]]
    - [[T1608-stage_capabilities#^t1608005-link-target|T1608.005: Link Target]]
    - [[T1608-stage_capabilities#^t1608006-seo-poisoning|T1608.006: SEO Poisoning]]
- [[T1650-acquire_access|T1650: Acquire Access]]

