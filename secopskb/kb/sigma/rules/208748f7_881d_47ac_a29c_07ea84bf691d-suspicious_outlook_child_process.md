---
sigma_id: "208748f7-881d-47ac-a29c-07ea84bf691d"
title: "Suspicious Outlook Child Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_office_outlook_susp_child_processes.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_office_outlook_susp_child_processes.yml"
build_date: "2026-04-26 15:01:52"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious Outlook Child Process

Detects a suspicious process spawning from an Outlook process.

## Metadata

- Rule ID: 208748f7-881d-47ac-a29c-07ea84bf691d
- Status: test
- Level: high
- Author: Michael Haag, Florian Roth (Nextron Systems), Markus Neis, Elastic, FPT.EagleEye Team
- Date: 2022-02-28
- Modified: 2023-02-04
- Source Path: rules/windows/process_creation/proc_creation_win_office_outlook_susp_child_processes.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1204-user_execution|T1204.002]]

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
