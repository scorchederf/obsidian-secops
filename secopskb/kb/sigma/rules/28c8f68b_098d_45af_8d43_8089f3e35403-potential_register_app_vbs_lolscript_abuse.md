---
sigma_id: "28c8f68b-098d-45af-8d43-8089f3e35403"
title: "Potential Register_App.Vbs LOLScript Abuse"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_lolscript_register_app.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolscript_register_app.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "28c8f68b-098d-45af-8d43-8089f3e35403"
  - "Potential Register_App.Vbs LOLScript Abuse"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Register_App.Vbs LOLScript Abuse

Detects potential abuse of the "register_app.vbs" script that is part of the Windows SDK. The script offers the capability to register new VSS/VDS Provider as a COM+ application. Attackers can use this to install malicious DLLs for persistence and execution.

## Metadata

- Rule ID: 28c8f68b-098d-45af-8d43-8089f3e35403
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-11-05
- Modified: 2022-07-07
- Source Path: rules/windows/process_creation/proc_creation_win_lolscript_register_app.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection_img:
- Image|endswith:
  - \cscript.exe
  - \wscript.exe
- OriginalFileName:
  - cscript.exe
  - wscript.exe
selection_cli:
  CommandLine|contains: '.vbs -register '
condition: all of selection*
```

## False Positives

- Other VB scripts that leverage the same starting command line flags

## References

- https://twitter.com/sblmsrsn/status/1456613494783160325?s=20
- https://github.com/microsoft/Windows-classic-samples/blob/7cbd99ac1d2b4a0beffbaba29ea63d024ceff700/Samples/Win7Samples/winbase/vss/vsssampleprovider/register_app.vbs

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolscript_register_app.yml)
