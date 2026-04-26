---
mitre_id: "S0591"
mitre_name: "ConnectWise"
mitre_type: "tool"
mitre_stix_id: "tool--842976c7-f9c8-41b2-8371-41dc64fbe261"
mitre_created: "2021-03-18T13:39:27.676Z"
mitre_modified: "2025-10-13T20:02:57.828Z"
mitre_version: "1.1"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/software/S0591/"
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
  - "ConnectWise"
  - "ScreenConnect"
aliases:
  - "S0591"
  - "ConnectWise"
  - "ScreenConnect"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

[ConnectWise](https://attack.mitre.org/software/S0591) is a legitimate remote administration tool that has been used since at least 2016 by threat actors including [MuddyWater](https://attack.mitre.org/groups/G0069) and [GOLD SOUTHFIELD](https://attack.mitre.org/groups/G0115) to connect to and conduct lateral movement in target environments.(Citation: Anomali Static Kitten February 2021)(Citation: Trend Micro Muddy Water March 2021)

## Workspace

- [[workspaces/tools/S0591-connectwise-note|Open workspace note]]

![[workspaces/tools/S0591-connectwise-note]]

## Uses Techniques

- [[T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]]
    - [[T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]]
- [[T1113-screen_capture|T1113: Screen Capture]]
- [[T1125-video_capture|T1125: Video Capture]]

