---
sigma_id: "9df0dd3a-1a5c-47e3-a2bc-30ed177646a0"
title: "Remote Code Execute via Winrm.vbs"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_winrm_execution_via_scripting_api_winrm_vbs.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_winrm_execution_via_scripting_api_winrm_vbs.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "9df0dd3a-1a5c-47e3-a2bc-30ed177646a0"
  - "Remote Code Execute via Winrm.vbs"
attack_technique_ids:
  - "T1216"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Remote Code Execute via Winrm.vbs

Detects an attempt to execute code or create service on remote host via winrm.vbs.

## Metadata

- Rule ID: 9df0dd3a-1a5c-47e3-a2bc-30ed177646a0
- Status: test
- Level: medium
- Author: Julia Fomina, oscd.community
- Date: 2020-10-07
- Modified: 2023-03-03
- Source Path: rules/windows/process_creation/proc_creation_win_winrm_execution_via_scripting_api_winrm_vbs.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1216-system_script_proxy_execution|T1216]]

## Detection

```yaml
selection_img:
- Image|endswith: \cscript.exe
- OriginalFileName: cscript.exe
selection_cli:
  CommandLine|contains|all:
  - winrm
  - invoke Create wmicimv2/Win32_
  - -r:http
condition: all of selection*
```

## False Positives

- Unknown

## References

- https://twitter.com/bohops/status/994405551751815170
- https://redcanary.com/blog/lateral-movement-winrm-wmi/
- https://lolbas-project.github.io/lolbas/Scripts/Winrm/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_winrm_execution_via_scripting_api_winrm_vbs.yml)
