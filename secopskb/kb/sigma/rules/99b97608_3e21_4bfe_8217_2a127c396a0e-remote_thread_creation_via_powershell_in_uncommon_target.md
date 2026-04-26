---
sigma_id: "99b97608-3e21-4bfe-8217-2a127c396a0e"
title: "Remote Thread Creation Via PowerShell In Uncommon Target"
framework: "sigma"
generated: "true"
source_path: "rules/windows/create_remote_thread/create_remote_thread_win_powershell_susp_targets.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/create_remote_thread/create_remote_thread_win_powershell_susp_targets.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / create_remote_thread"
aliases:
  - "99b97608-3e21-4bfe-8217-2a127c396a0e"
  - "Remote Thread Creation Via PowerShell In Uncommon Target"
attack_technique_ids:
  - "T1218.011"
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Remote Thread Creation Via PowerShell In Uncommon Target

Detects the creation of a remote thread from a Powershell process in an uncommon target process

## Metadata

- Rule ID: 99b97608-3e21-4bfe-8217-2a127c396a0e
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2018-06-25
- Modified: 2023-11-10
- Source Path: rules/windows/create_remote_thread/create_remote_thread_win_powershell_susp_targets.yml

## Logsource

- category: create_remote_thread
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.011]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection:
  SourceImage|endswith:
  - \powershell.exe
  - \pwsh.exe
  TargetImage|endswith:
  - \rundll32.exe
  - \regsvr32.exe
condition: selection
```

## False Positives

- Unknown

## References

- https://www.fireeye.com/blog/threat-research/2018/06/bring-your-own-land-novel-red-teaming-technique.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/create_remote_thread/create_remote_thread_win_powershell_susp_targets.yml)
