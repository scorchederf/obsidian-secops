---
mitre_id: "S0527"
mitre_name: "CSPY Downloader"
mitre_type: "tool"
mitre_stix_id: "tool--5256c0f8-9108-4c92-8b09-482dfacdcd94"
mitre_created: "2020-11-09T14:30:35.202Z"
mitre_modified: "2025-04-16T20:38:52.033Z"
mitre_version: "1.0"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/software/S0527/"
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
  - "CSPY Downloader"
aliases:
  - "S0527"
  - "CSPY Downloader"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

[CSPY Downloader](https://attack.mitre.org/software/S0527) is a tool designed to evade analysis and download additional payloads used by [Kimsuky](https://attack.mitre.org/groups/G0094).(Citation: Cybereason Kimsuky November 2020)

## Workspace

- [[workspaces/tools/S0527-cspy_downloader-note|Open workspace note]]

![[workspaces/tools/S0527-cspy_downloader-note]]

## Uses Techniques

- [[T1027-obfuscated_files_or_information|T1027: Obfuscated Files or Information]]
    - [[T1027-obfuscated_files_or_information#^t1027002-software-packing|T1027.002: Software Packing]]
- [[T1036-masquerading|T1036: Masquerading]]
    - [[T1036-masquerading#^t1036004-masquerade-task-or-service|T1036.004: Masquerade Task or Service]]
- [[T1053-scheduled_task_job|T1053: Scheduled Task/Job]]
    - [[T1053-scheduled_task_job#^t1053005-scheduled-task|T1053.005: Scheduled Task]]
- [[T1070-indicator_removal|T1070: Indicator Removal]]
- [[T1070-indicator_removal|T1070: Indicator Removal]]
    - [[T1070-indicator_removal#^t1070004-file-deletion|T1070.004: File Deletion]]
- [[T1071-application_layer_protocol|T1071: Application Layer Protocol]]
    - [[T1071-application_layer_protocol#^t1071001-web-protocols|T1071.001: Web Protocols]]
- [[T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]
- [[T1112-modify_registry|T1112: Modify Registry]]
- [[T1204-user_execution|T1204: User Execution]]
    - [[T1204-user_execution#^t1204002-malicious-file|T1204.002: Malicious File]]
- [[T1497-virtualization_sandbox_evasion|T1497: Virtualization/Sandbox Evasion]]
    - [[T1497-virtualization_sandbox_evasion#^t1497001-system-checks|T1497.001: System Checks]]
- [[T1548-abuse_elevation_control_mechanism|T1548: Abuse Elevation Control Mechanism]]
    - [[T1548-abuse_elevation_control_mechanism#^t1548002-bypass-user-account-control|T1548.002: Bypass User Account Control]]
- [[T1553-subvert_trust_controls|T1553: Subvert Trust Controls]]
    - [[T1553-subvert_trust_controls#^t1553002-code-signing|T1553.002: Code Signing]]

