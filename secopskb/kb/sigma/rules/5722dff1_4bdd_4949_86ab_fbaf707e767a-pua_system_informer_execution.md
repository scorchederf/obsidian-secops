---
sigma_id: "5722dff1-4bdd-4949-86ab-fbaf707e767a"
title: "PUA - System Informer Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_pua_system_informer.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_system_informer.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "5722dff1-4bdd-4949-86ab-fbaf707e767a"
  - "PUA - System Informer Execution"
attack_technique_ids:
  - "T1082"
  - "T1564"
  - "T1543"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PUA - System Informer Execution

Detects the execution of System Informer, a task manager tool to view and manipulate processes, kernel options and other low level operations

## Metadata

- Rule ID: 5722dff1-4bdd-4949-86ab-fbaf707e767a
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2023-05-08
- Modified: 2024-11-23
- Source Path: rules/windows/process_creation/proc_creation_win_pua_system_informer.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1082-system_information_discovery|T1082]]
- [[kb/attack/techniques/T1564-hide_artifacts|T1564]]
- [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543]]

## Detection

```yaml
selection:
- Image|endswith: \SystemInformer.exe
- OriginalFileName: SystemInformer.exe
- Description: System Informer
- Product: System Informer
- Hashes|contains:
  - MD5=19426363A37C03C3ED6FEDF57B6696EC
  - SHA1=8B12C6DA8FAC0D5E8AB999C31E5EA04AF32D53DC
  - SHA256=8EE9D84DE50803545937A63C686822388A3338497CDDB660D5D69CF68B68F287
  - IMPHASH=B68908ADAEB5D662F87F2528AF318F12
condition: selection
```

## False Positives

- System Informer is regularly used legitimately by system administrators or developers. Apply additional filters accordingly

## References

- https://github.com/winsiderss/systeminformer

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_system_informer.yml)
