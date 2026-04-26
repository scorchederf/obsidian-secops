---
mitre_id: "S0040"
mitre_name: "HTRAN"
mitre_type: "tool"
mitre_stix_id: "tool--d5e96a35-7b0b-4c6a-9533-d63ecbda563e"
mitre_created: "2017-05-31T21:32:32.011Z"
mitre_modified: "2024-11-17T16:27:34.671Z"
mitre_version: "1.2"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/software/S0040/"
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
  - "HTRAN"
  - "HUC Packet Transmit Tool"
aliases:
  - "S0040"
  - "HTRAN"
  - "HUC Packet Transmit Tool"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

[HTRAN](https://attack.mitre.org/software/S0040) is a tool that proxies connections through intermediate hops and aids users in disguising their true geographical location. It can be used by adversaries to hide their location when interacting with the victim networks. (Citation: Operation Quantum Entanglement)(Citation: NCSC Joint Report Public Tools)

## Workspace

- [[workspaces/tools/S0040-htran-note|Open workspace note]]

![[workspaces/tools/S0040-htran-note]]

## Uses Techniques

- [[T1014-rootkit|T1014: Rootkit]]
- [[T1055-process_injection|T1055: Process Injection]]
- [[T1090-proxy|T1090: Proxy]]

