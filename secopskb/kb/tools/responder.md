---
mitre_id: "S0174"
mitre_name: "Responder"
mitre_type: "tool"
mitre_stix_id: "tool--a1dd2dbd-1550-44bf-abcc-1a4c52e97719"
mitre_created: "2018-01-16T16:13:52.465Z"
mitre_modified: "2025-04-16T20:38:54.639Z"
mitre_version: "1.2"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/software/S0174/"
framework: "attack"
generated: "true"
build_date: "2026-04-25 14:47:22"
build_source: "script"
object_type: "tool"
tags:
  - "attack"
  - "tool"
  - "offense"
mitre_aliases:
  - "Responder"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[notes/index|Notes]]

---

Responder is an open source tool used for LLMNR, NBT-NS and MDNS poisoning, with built-in HTTP/SMB/MSSQL/FTP/LDAP rogue authentication server supporting NTLMv1/NTLMv2/LMv2, Extended Security NTLMSSP and Basic HTTP authentication. (Citation: GitHub Responder)

## Workspace

- [[notes/tools/S0174-responder-note|Open workspace note]]

![[notes/tools/S0174-responder-note]]

## Uses Techniques

- [[T1040-network_sniffing|T1040: Network Sniffing]]
- [[T1557-adversary-in-the-middle|T1557: Adversary-in-the-Middle]]
    - [[T1557-adversary-in-the-middle#^t1557001-llmnr-nbt-ns-poisoning-and-smb-relay|T1557.001: LLMNR/NBT-NS Poisoning and SMB Relay]]

