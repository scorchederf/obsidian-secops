---
sigma_id: "c80e66d8-1780-48a9-b412-46663fd21ac0"
title: "Suspicious Autorun Registry Modified via WMI"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_autorun_registry_modified_via_wmic.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_autorun_registry_modified_via_wmic.yml"
build_date: "2026-04-26 14:14:35"
status: "experimental"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "c80e66d8-1780-48a9-b412-46663fd21ac0"
  - "Suspicious Autorun Registry Modified via WMI"
attack_technique_ids:
  - "T1547.001"
  - "T1047"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Autorun Registry Modified via WMI

Detects suspicious activity where the WMIC process is used to create an autorun registry entry via reg.exe, which is often indicative of persistence mechanisms employed by malware.

## Metadata

- Rule ID: c80e66d8-1780-48a9-b412-46663fd21ac0
- Status: experimental
- Level: high
- Author: Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2025-02-17
- Source Path: rules/windows/process_creation/proc_creation_win_autorun_registry_modified_via_wmic.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.001]]
- [[kb/attack/techniques/T1047-windows_management_instrumentation|T1047]]

## Detection

```yaml
selection_execution_img:
- Image|endswith: \wmic.exe
- OriginalFileName: wmic.exe
- ParentImage|endswith: \wmiprvse.exe
selection_execution_cmd:
  CommandLine|contains|all:
  - reg
  - ' add '
  CommandLine|contains:
  - \Software\Microsoft\Windows\CurrentVersion\Run
  - \Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Run
  - \Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run
selection_suspicious_paths_1:
  CommandLine|contains:
  - :\Perflogs
  - :\ProgramData'
  - :\Windows\Temp
  - :\Temp
  - \AppData\Local\Temp
  - \AppData\Roaming
  - :\$Recycle.bin
  - :\Users\Default
  - :\Users\public
  - '%temp%'
  - '%tmp%'
  - '%Public%'
  - '%AppData%'
selection_suspicious_paths_user_1:
  CommandLine|contains: :\Users\
selection_suspicious_paths_user_2:
  CommandLine|contains:
  - \Favorites
  - \Favourites
  - \Contacts
  - \Music
  - \Pictures
  - \Documents
  - \Photos
condition: all of selection_execution_* and (selection_suspicious_paths_1 or (all
  of selection_suspicious_paths_user_*))
```

## False Positives

- Legitimate administrative activity or software installations

## References

- Internal Research
- https://github.com/HackTricks-wiki/hacktricks/blob/e4c7b21b8f36c97c35b7c622732b38a189ce18f7/src/windows-hardening/windows-local-privilege-escalation/privilege-escalation-with-autorun-binaries.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_autorun_registry_modified_via_wmic.yml)
