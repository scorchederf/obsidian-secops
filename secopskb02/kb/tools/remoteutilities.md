---
mitre_id: "S0592"
mitre_name: "RemoteUtilities"
mitre_type: "tool"
mitre_stix_id: "tool--03c6e0ea-96d3-4b23-9afb-05055663cf4b"
mitre_created: "2021-03-18T14:57:34.628Z"
mitre_modified: "2025-04-25T14:45:11.980Z"
mitre_version: "1.0"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/software/S0592/"
framework: "attack"
generated: "true"
build_date: "2026-04-25 20:43:29"
build_source: "script"
object_type: "tool"
tags:
  - "attack"
  - "tool"
  - "offense"
mitre_aliases:
  - "RemoteUtilities"
aliases:
  - "S0592"
  - "RemoteUtilities"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

[RemoteUtilities](https://attack.mitre.org/software/S0592) is a legitimate remote administration tool that has been used by [MuddyWater](https://attack.mitre.org/groups/G0069) since at least 2021 for execution on target machines.(Citation: Trend Micro Muddy Water March 2021)

## Workspace

- [[workspaces/tools/S0592-remoteutilities-note|Open workspace note]]

![[workspaces/tools/S0592-remoteutilities-note]]

## Uses Techniques

- [[T1083-file_and_directory_discovery|T1083: File and Directory Discovery]]
- [[T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]
- [[T1113-screen_capture|T1113: Screen Capture]]
- [[T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]
    - [[T1218-system_binary_proxy_execution#^t1218007-msiexec|T1218.007: Msiexec]]

