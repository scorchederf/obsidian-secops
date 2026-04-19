---
id: S0699
name: Mythic
created: 2022-03-26 01:38:12.966000+00:00
modified: 2025-04-16 20:38:56.653000+00:00
type: tool
x_mitre_version: 1.0
x_mitre_domains: enterprise-attack
---

# Mythic

[Mythic](https://attack.mitre.org/software/S0699) is an open source, cross-platform post-exploitation/command and control platform. [Mythic](https://attack.mitre.org/software/S0699) is designed to "plug-n-play" with various agents and communication channels.(Citation: Mythic Github)(Citation: Mythic SpecterOps)(Citation: Mythc Documentation) Deployed [Mythic](https://attack.mitre.org/software/S0699) C2 servers have been observed as part of potentially malicious infrastructure.(Citation: RecordedFuture 2021 Ad Infra)

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

