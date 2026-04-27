---
mitre_id: "S0699"
mitre_name: "Mythic"
mitre_type: "tool"
mitre_stix_id: "tool--d505fc8b-2e64-46eb-96d6-9ef7ffca5b66"
mitre_created: "2022-03-26T01:38:12.966Z"
mitre_modified: "2025-04-16T20:38:56.653Z"
mitre_version: "1.0"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/software/S0699/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "tool"
tags:
  - "attack"
  - "tool"
  - "offense"
mitre_aliases:
  - "Mythic"
aliases:
  - "S0699"
  - "Mythic"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

[Mythic](https://attack.mitre.org/software/S0699) is an open source, cross-platform post-exploitation/command and control platform. [Mythic](https://attack.mitre.org/software/S0699) is designed to "plug-n-play" with various agents and communication channels.(Citation: Mythic Github)(Citation: Mythic SpecterOps)(Citation: Mythc Documentation) Deployed [Mythic](https://attack.mitre.org/software/S0699) C2 servers have been observed as part of potentially malicious infrastructure.(Citation: RecordedFuture 2021 Ad Infra)

## Workspace

- [[workspaces/tools/S0699-mythic-note|Open workspace note]]

![[workspaces/tools/S0699-mythic-note]]

## Uses Techniques

- [[T1008-fallback_channels|T1008: Fallback Channels]]
- [[T1030-data_transfer_size_limits|T1030: Data Transfer Size Limits]]
- [[T1071-application_layer_protocol|T1071: Application Layer Protocol]]
    - [[T1071-application_layer_protocol#^t1071001-web-protocols|T1071.001: Web Protocols]]
    - [[T1071-application_layer_protocol#^t1071002-file-transfer-protocols|T1071.002: File Transfer Protocols]]
    - [[T1071-application_layer_protocol#^t1071004-dns|T1071.004: DNS]]
- [[T1090-proxy|T1090: Proxy]]
    - [[T1090-proxy#^t1090001-internal-proxy|T1090.001: Internal Proxy]]
    - [[T1090-proxy#^t1090002-external-proxy|T1090.002: External Proxy]]
    - [[T1090-proxy#^t1090004-domain-fronting|T1090.004: Domain Fronting]]
- [[T1095-non-application_layer_protocol|T1095: Non-Application Layer Protocol]]
- [[T1119-automated_collection|T1119: Automated Collection]]
- [[T1132-data_encoding|T1132: Data Encoding]]
- [[T1572-protocol_tunneling|T1572: Protocol Tunneling]]
- [[T1573-encrypted_channel|T1573: Encrypted Channel]]
    - [[T1573-encrypted_channel#^t1573002-asymmetric-cryptography|T1573.002: Asymmetric Cryptography]]

