---
id: S0174
name: Responder
created: 2018-01-16 16:13:52.465000+00:00
modified: 2025-04-16 20:38:54.639000+00:00
type: tool
x_mitre_version: 1.2
x_mitre_domains: enterprise-attack
---

# Responder

Responder is an open source tool used for LLMNR, NBT-NS and MDNS poisoning, with built-in HTTP/SMB/MSSQL/FTP/LDAP rogue authentication server supporting NTLMv1/NTLMv2/LMv2, Extended Security NTLMSSP and Basic HTTP authentication. (Citation: GitHub Responder)

## Properties

- id: S0174
- name: Responder
- created: 2018-01-16 16:13:52.465000+00:00
- modified: 2025-04-16 20:38:54.639000+00:00
- type: tool
- x_mitre_version: 1.2
- x_mitre_domains: enterprise-attack

## Uses Techniques

- [[T1040-network_sniffing|T1040: Network Sniffing]]
- [[T1557-adversary-in-the-middle|T1557: Adversary-in-the-Middle]]
    - [[T1557-adversary-in-the-middle#^t1557001-llmnr-nbt-ns-poisoning-and-smb-relay|T1557.001: LLMNR/NBT-NS Poisoning and SMB Relay]]

