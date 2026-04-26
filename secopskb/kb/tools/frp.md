---
mitre_id: "S1144"
mitre_name: "FRP"
mitre_type: "tool"
mitre_stix_id: "tool--36dd807e-b5bc-4c3e-91ed-80682360148c"
mitre_created: "2024-07-10T18:46:33.555Z"
mitre_modified: "2024-07-30T18:17:09.725Z"
mitre_version: "1.0"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/software/S1144/"
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
  - "FRP"
aliases:
  - "S1144"
  - "FRP"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

[FRP](https://attack.mitre.org/software/S1144), which stands for Fast Reverse Proxy, is an openly available tool that is capable of exposing a server located behind a firewall or Network Address Translation (NAT) to the Internet. [FRP](https://attack.mitre.org/software/S1144) can support multiple protocols including TCP, UDP, and HTTP(S) and has been abused by threat actors to proxy command and control communications.(Citation: FRP GitHub)(Citation: Joint Cybersecurity Advisory Volt Typhoon June 2023)(Citation: RedCanary Mockingbird May 2020)(Citation: DFIR Phosphorus November 2021)

## Workspace

- [[workspaces/tools/S1144-frp-note|Open workspace note]]

![[workspaces/tools/S1144-frp-note]]

## Uses Techniques

- [[T1046-network_service_discovery|T1046: Network Service Discovery]]
- [[T1049-system_network_connections_discovery|T1049: System Network Connections Discovery]]
- [[T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]]
    - [[T1059-command_and_scripting_interpreter#^t1059007-javascript|T1059.007: JavaScript]]
- [[T1071-application_layer_protocol|T1071: Application Layer Protocol]]
    - [[T1071-application_layer_protocol#^t1071001-web-protocols|T1071.001: Web Protocols]]
- [[T1090-proxy|T1090: Proxy]]
- [[T1090-proxy|T1090: Proxy]]
    - [[T1090-proxy#^t1090003-multi-hop-proxy|T1090.003: Multi-hop Proxy]]
- [[T1095-non-application_layer_protocol|T1095: Non-Application Layer Protocol]]
- [[T1572-protocol_tunneling|T1572: Protocol Tunneling]]
- [[T1573-encrypted_channel|T1573: Encrypted Channel]]
    - [[T1573-encrypted_channel#^t1573001-symmetric-cryptography|T1573.001: Symmetric Cryptography]]
    - [[T1573-encrypted_channel#^t1573002-asymmetric-cryptography|T1573.002: Asymmetric Cryptography]]

