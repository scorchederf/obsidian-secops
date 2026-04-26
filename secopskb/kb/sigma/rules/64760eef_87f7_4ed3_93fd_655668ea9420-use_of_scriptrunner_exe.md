---
sigma_id: "64760eef-87f7-4ed3-93fd-655668ea9420"
title: "Use of Scriptrunner.exe"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_lolbin_scriptrunner.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_scriptrunner.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "64760eef-87f7-4ed3-93fd-655668ea9420"
  - "Use of Scriptrunner.exe"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Use of Scriptrunner.exe

The "ScriptRunner.exe" binary can be abused to proxy execution through it and bypass possible whitelisting

## Metadata

- Rule ID: 64760eef-87f7-4ed3-93fd-655668ea9420
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-07-01
- Source Path: rules/windows/process_creation/proc_creation_win_lolbin_scriptrunner.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection_img:
- Image|endswith: \ScriptRunner.exe
- OriginalFileName: ScriptRunner.exe
selection_cli:
  CommandLine|contains: ' -appvscript '
condition: all of selection*
```

## False Positives

- Legitimate use when App-v is deployed

## References

- https://lolbas-project.github.io/lolbas/Binaries/Scriptrunner/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_scriptrunner.yml)
