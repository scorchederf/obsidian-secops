---
id: S0508
name: ngrok
created: 2023-09-14 18:56:34.771000+00:00
modified: 2025-10-16 19:37:56.911000+00:00
type: tool
x_mitre_version: 1.4
x_mitre_domains: enterprise-attack
---

# ngrok

[ngrok](https://attack.mitre.org/software/S0508) is a legitimate reverse proxy tool that can create a secure tunnel to servers located behind firewalls or on local machines that do not have a public IP. [ngrok](https://attack.mitre.org/software/S0508) has been leveraged by threat actors in several campaigns including use for lateral movement and data exfiltration.(Citation: Zdnet Ngrok September 2018)(Citation: FireEye Maze May 2020)(Citation: Cyware Ngrok May 2019)(Citation: MalwareBytes LazyScripter Feb 2021)

## Properties

- id: S0508
- name: ngrok
- created: 2023-09-14 18:56:34.771000+00:00
- modified: 2025-10-16 19:37:56.911000+00:00
- type: tool
- x_mitre_version: 1.4
- x_mitre_domains: enterprise-attack

## Uses Techniques

- [[T1090-proxy|T1090: Proxy]]
- [[T1102-web_service|T1102: Web Service]]
- [[T1567-exfiltration_over_web_service|T1567: Exfiltration Over Web Service]]
- [[T1568-dynamic_resolution|T1568: Dynamic Resolution]]
    - [[T1568-dynamic_resolution#^t1568002-domain-generation-algorithms|T1568.002: Domain Generation Algorithms]]
- [[T1572-protocol_tunneling|T1572: Protocol Tunneling]]

