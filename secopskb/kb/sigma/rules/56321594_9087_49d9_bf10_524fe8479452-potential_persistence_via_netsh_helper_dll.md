---
sigma_id: "56321594-9087-49d9-bf10-524fe8479452"
title: "Potential Persistence Via Netsh Helper DLL"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_netsh_helper_dll_persistence.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_netsh_helper_dll_persistence.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "56321594-9087-49d9-bf10-524fe8479452"
  - "Potential Persistence Via Netsh Helper DLL"
attack_technique_ids:
  - "T1546.007"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Persistence Via Netsh Helper DLL

Detects the execution of netsh with "add helper" flag in order to add a custom helper DLL. This technique can be abused to add a malicious helper DLL that can be used as a persistence proxy that gets called when netsh.exe is executed.

## Metadata

- Rule ID: 56321594-9087-49d9-bf10-524fe8479452
- Status: test
- Level: medium
- Author: Victor Sergeev, oscd.community
- Date: 2019-10-25
- Modified: 2023-11-28
- Source Path: rules/windows/process_creation/proc_creation_win_netsh_helper_dll_persistence.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.007]]

### Software Tags

- S0108

## Detection

```yaml
selection_img:
- OriginalFileName: netsh.exe
- Image|endswith: \netsh.exe
selection_cli:
  CommandLine|contains|all:
  - add
  - helper
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1546.007/T1546.007.md
- https://github.com/outflanknl/NetshHelperBeacon
- https://web.archive.org/web/20160928212230/https://www.adaptforward.com/2016/09/using-netshell-to-execute-evil-dlls-and-persist-on-a-host/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_netsh_helper_dll_persistence.yml)
