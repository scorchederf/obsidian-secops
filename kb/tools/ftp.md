---
id: S0095
name: ftp
created: 2017-05-31 21:33:00.565000+00:00
modified: 2025-06-04 16:11:23.752000+00:00
type: tool
x_mitre_version: 2.2
x_mitre_domains: enterprise-attack
---

# ftp

[ftp](https://attack.mitre.org/software/S0095) is a utility commonly available with operating systems to transfer information over the File Transfer Protocol (FTP). Adversaries can use it to transfer other tools onto a system or to exfiltrate data.(Citation: Microsoft FTP)(Citation: Linux FTP)

## Properties

- id: S0095
- name: ftp
- created: 2017-05-31 21:33:00.565000+00:00
- modified: 2025-06-04 16:11:23.752000+00:00
- type: tool
- x_mitre_version: 2.2
- x_mitre_domains: enterprise-attack

## Uses Techniques

- [[T1048-exfiltration_over_alternative_protocol|T1048: Exfiltration Over Alternative Protocol]]
    - [[T1048-exfiltration_over_alternative_protocol#^t1048003-exfiltration-over-unencrypted-non-c2-protocol|T1048.003: Exfiltration Over Unencrypted Non-C2 Protocol]]
- [[T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]
- [[T1570-lateral_tool_transfer|T1570: Lateral Tool Transfer]]

