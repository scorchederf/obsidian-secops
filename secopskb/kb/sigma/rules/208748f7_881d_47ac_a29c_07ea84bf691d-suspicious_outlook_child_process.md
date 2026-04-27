---
sigma_id: "208748f7-881d-47ac-a29c-07ea84bf691d"
title: "Suspicious Outlook Child Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_office_outlook_susp_child_processes.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_office_outlook_susp_child_processes.yml"
build_date: "2026-04-27 19:13:57"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "208748f7-881d-47ac-a29c-07ea84bf691d"
  - "Suspicious Outlook Child Process"
attack_technique_ids:
  - "T1204.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects a suspicious process spawning from an Outlook process.

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1204-user_execution#^t1204002-malicious-file|T1204.002: Malicious File]]

## Detection

```yaml
selection:
  ParentImage|endswith: \OUTLOOK.EXE
  Image|endswith:
  - \AppVLP.exe
  - \bash.exe
  - \cmd.exe
  - \cscript.exe
  - \forfiles.exe
  - \hh.exe
  - \mftrace.exe
  - \msbuild.exe
  - \msdt.exe
  - \mshta.exe
  - \msiexec.exe
  - \powershell.exe
  - \pwsh.exe
  - \regsvr32.exe
  - \schtasks.exe
  - \scrcons.exe
  - \scriptrunner.exe
  - \sh.exe
  - \svchost.exe
  - \wmic.exe
  - \wscript.exe
condition: selection
```

## False Positives

- Unknown

## References

- https://www.hybrid-analysis.com/sample/465aabe132ccb949e75b8ab9c5bda36d80cf2fd503d52b8bad54e295f28bbc21?environmentId=100
- https://mgreen27.github.io/posts/2018/04/02/DownloadCradle.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_office_outlook_susp_child_processes.yml)
