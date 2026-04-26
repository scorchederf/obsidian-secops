---
sigma_id: "646bc99f-6682-4b47-a73a-17b1b64c9d34"
title: "Execute Files with Msdeploy.exe"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_lolbin_msdeploy.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_msdeploy.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "646bc99f-6682-4b47-a73a-17b1b64c9d34"
  - "Execute Files with Msdeploy.exe"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Execute Files with Msdeploy.exe

Detects file execution using the msdeploy.exe lolbin

## Metadata

- Rule ID: 646bc99f-6682-4b47-a73a-17b1b64c9d34
- Status: test
- Level: medium
- Author: Beyu Denis, oscd.community
- Date: 2020-10-18
- Modified: 2021-11-27
- Source Path: rules/windows/process_creation/proc_creation_win_lolbin_msdeploy.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection:
  CommandLine|contains|all:
  - verb:sync
  - -source:RunCommand
  - -dest:runCommand
  Image|endswith: \msdeploy.exe
condition: selection
```

## False Positives

- System administrator Usage

## References

- https://lolbas-project.github.io/lolbas/OtherMSBinaries/Msdeploy/
- https://twitter.com/pabraeken/status/995837734379032576
- https://twitter.com/pabraeken/status/999090532839313408

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_msdeploy.yml)
