---
mitre_id: "S0111"
mitre_name: "schtasks"
mitre_type: "tool"
mitre_stix_id: "tool--c9703cd3-141c-43a0-a926-380082be5d04"
mitre_created: "2017-05-31T21:33:07.218Z"
mitre_modified: "2025-04-16T20:38:56.004Z"
mitre_version: "1.2"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/software/S0111/"
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
  - "schtasks"
  - "schtasks.exe"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[notes/index|Notes]]

---

[schtasks](https://attack.mitre.org/software/S0111) is used to schedule execution of programs or scripts on a Windows system to run at a specific date and time. (Citation: TechNet Schtasks)

## Workspace

- [[notes/tools/S0111-schtasks-note|Open workspace note]]

![[notes/tools/S0111-schtasks-note]]

## Uses Techniques

- [[T1053-scheduled_task_job|T1053: Scheduled Task/Job]]
    - [[T1053-scheduled_task_job#^t1053005-scheduled-task|T1053.005: Scheduled Task]]

