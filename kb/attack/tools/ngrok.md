---
mitre_id: "S0508"
mitre_name: "ngrok"
mitre_type: "tool"
mitre_stix_id: "tool--2f7f03bb-f367-4a5a-ad9b-310a12a48906"
mitre_created: "2023-09-14T18:56:34.771Z"
mitre_modified: "2025-10-16T19:37:56.911Z"
mitre_version: "1.4"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/software/S0508/"
framework: "attack"
generated: "true"
build_date: "2026-04-23 22:40:56"
build_source: "script"
object_type: "tool"
tags:
  - "attack"
  - "tool"
  - "offense"
mitre_aliases:
  - "ngrok"
---

# ngrok

[ngrok](https://attack.mitre.org/software/S0508) is a legitimate reverse proxy tool that can create a secure tunnel to servers located behind firewalls or on local machines that do not have a public IP. [ngrok](https://attack.mitre.org/software/S0508) has been leveraged by threat actors in several campaigns including use for lateral movement and data exfiltration.(Citation: Zdnet Ngrok September 2018)(Citation: FireEye Maze May 2020)(Citation: Cyware Ngrok May 2019)(Citation: MalwareBytes LazyScripter Feb 2021)

## Uses Techniques

- [[T1090-proxy|T1090: Proxy]]
- [[T1102-web_service|T1102: Web Service]]
- [[T1567-exfiltration_over_web_service|T1567: Exfiltration Over Web Service]]
- [[T1568-dynamic_resolution|T1568: Dynamic Resolution]]
    - [[T1568-dynamic_resolution#^t1568002-domain-generation-algorithms|T1568.002: Domain Generation Algorithms]]
- [[T1572-protocol_tunneling|T1572: Protocol Tunneling]]

## Workspace

- [[kb/notes/attack/tools/s0508-notes|Open workspace note]]

