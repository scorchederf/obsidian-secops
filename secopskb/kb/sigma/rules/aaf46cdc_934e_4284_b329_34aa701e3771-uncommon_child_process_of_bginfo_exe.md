---
sigma_id: "aaf46cdc-934e-4284-b329-34aa701e3771"
title: "Uncommon Child Process Of BgInfo.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_bginfo_uncommon_child_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_bginfo_uncommon_child_process.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "aaf46cdc-934e-4284-b329-34aa701e3771"
  - "Uncommon Child Process Of BgInfo.EXE"
attack_technique_ids:
  - "T1059.005"
  - "T1218"
  - "T1202"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Uncommon Child Process Of BgInfo.EXE

Detects uncommon child processes of "BgInfo.exe" which could be a sign of potential abuse of the binary to proxy execution via external VBScript

## Metadata

- Rule ID: aaf46cdc-934e-4284-b329-34aa701e3771
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems), Beyu Denis, oscd.community
- Date: 2019-10-26
- Modified: 2023-08-16
- Source Path: rules/windows/process_creation/proc_creation_win_bginfo_uncommon_child_process.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.005]]
- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]
- [[kb/attack/techniques/T1202-indirect_command_execution|T1202]]

## Detection

```yaml
selection:
  ParentImage|endswith:
  - \bginfo.exe
  - \bginfo64.exe
condition: selection
```

## False Positives

- Unknown

## References

- https://lolbas-project.github.io/lolbas/OtherMSBinaries/Bginfo/
- https://oddvar.moe/2017/05/18/bypassing-application-whitelisting-with-bginfo/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_bginfo_uncommon_child_process.yml)
