---
mitre_id: "S1087"
mitre_name: "AsyncRAT"
mitre_type: "tool"
mitre_stix_id: "tool--6a5947f3-1a36-4653-8734-526df3e1d28d"
mitre_created: "2023-09-20T17:32:59.932Z"
mitre_modified: "2023-10-10T17:19:12.868Z"
mitre_version: "1.0"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/software/S1087/"
framework: "attack"
generated: "true"
build_date: "2026-04-25 14:47:22"
build_source: "script"
object_type: "tool"
tags:
  - "attack"
  - "tool"
  - "offense"
mitre_aliases:
  - "AsyncRAT"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[notes/index|Notes]]

---

[AsyncRAT](https://attack.mitre.org/software/S1087) is an open-source remote access tool originally available through the NYANxCAT Github repository that has been used in malicious campaigns.(Citation: Morphisec Snip3 May 2021)(Citation: Cisco Operation Layover September 2021)(Citation: Telefonica Snip3 December 2021)

## Workspace

- [[notes/tools/S1087-asyncrat-note|Open workspace note]]

![[notes/tools/S1087-asyncrat-note]]

## Uses Techniques

- [[T1033-system_owner_user_discovery|T1033: System Owner/User Discovery]]
- [[T1053-scheduled_task_job|T1053: Scheduled Task/Job]]
    - [[T1053-scheduled_task_job#^t1053005-scheduled-task|T1053.005: Scheduled Task]]
- [[T1056-input_capture|T1056: Input Capture]]
    - [[T1056-input_capture#^t1056001-keylogging|T1056.001: Keylogging]]
- [[T1057-process_discovery|T1057: Process Discovery]]
- [[T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]
- [[T1106-native_api|T1106: Native API]]
- [[T1113-screen_capture|T1113: Screen Capture]]
- [[T1125-video_capture|T1125: Video Capture]]
- [[T1497-virtualization_sandbox_evasion|T1497: Virtualization/Sandbox Evasion]]
    - [[T1497-virtualization_sandbox_evasion#^t1497001-system-checks|T1497.001: System Checks]]
- [[T1564-hide_artifacts|T1564: Hide Artifacts]]
    - [[T1564-hide_artifacts#^t1564003-hidden-window|T1564.003: Hidden Window]]
- [[T1568-dynamic_resolution|T1568: Dynamic Resolution]]
- [[T1622-debugger_evasion|T1622: Debugger Evasion]]
- [[T1680-local_storage_discovery|T1680: Local Storage Discovery]]

