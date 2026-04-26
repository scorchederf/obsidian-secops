---
sigma_id: "065b00ca-5d5c-4557-ac95-64a6d0b64d86"
title: "Remote Access Tool - Anydesk Execution From Suspicious Folder"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_remote_access_tools_anydesk_susp_exec.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_remote_access_tools_anydesk_susp_exec.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "065b00ca-5d5c-4557-ac95-64a6d0b64d86"
  - "Remote Access Tool - Anydesk Execution From Suspicious Folder"
attack_technique_ids:
  - "T1219.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Remote Access Tool - Anydesk Execution From Suspicious Folder

An adversary may use legitimate desktop support and remote access software, such as Team Viewer, Go2Assist, LogMein, AmmyyAdmin, etc, to establish an interactive command and control channel to target systems within networks.
These services are commonly used as legitimate technical support software, and may be allowed by application control within a target environment.
Remote access tools like VNC, Ammyy, and Teamviewer are used frequently when compared with other legitimate software commonly used by adversaries. (Citation: Symantec Living off the Land)

## Metadata

- Rule ID: 065b00ca-5d5c-4557-ac95-64a6d0b64d86
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-05-20
- Modified: 2025-02-24
- Source Path: rules/windows/process_creation/proc_creation_win_remote_access_tools_anydesk_susp_exec.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1219-remote_access_tools|T1219.002]]

## Detection

```yaml
selection:
- Image|endswith:
  - \AnyDesk.exe
  - \AnyDeskMSI.exe
- Description: AnyDesk
- Product: AnyDesk
- Company: AnyDesk Software GmbH
filter:
  Image|contains:
  - \AppData\
  - Program Files (x86)\AnyDesk
  - Program Files\AnyDesk
condition: selection and not filter
```

## False Positives

- Legitimate use of AnyDesk from a non-standard folder

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1219/T1219.md#atomic-test-2---anydesk-files-detected-test-on-windows
- https://thedfirreport.com/2025/02/24/confluence-exploit-leads-to-lockbit-ransomware/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_remote_access_tools_anydesk_susp_exec.yml)
