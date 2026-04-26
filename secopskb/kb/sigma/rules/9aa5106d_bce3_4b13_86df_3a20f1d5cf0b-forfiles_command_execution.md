---
sigma_id: "9aa5106d-bce3-4b13-86df-3a20f1d5cf0b"
title: "Forfiles Command Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_forfiles_proxy_execution_.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_forfiles_proxy_execution_.yml"
build_date: "2026-04-26 14:14:25"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "9aa5106d-bce3-4b13-86df-3a20f1d5cf0b"
  - "Forfiles Command Execution"
attack_technique_ids:
  - "T1059"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Forfiles Command Execution

Detects the execution of "forfiles" with the "/c" flag.
While this is an expected behavior of the tool, it can be abused in order to proxy execution through it with any binary.
Can be used to bypass application whitelisting.

## Metadata

- Rule ID: 9aa5106d-bce3-4b13-86df-3a20f1d5cf0b
- Status: test
- Level: medium
- Author: Tim Rauch, Elastic, E.M. Anhaus (originally from Atomic Blue Detections, Endgame), oscd.community
- Date: 2022-06-14
- Modified: 2024-03-05
- Source Path: rules/windows/process_creation/proc_creation_win_forfiles_proxy_execution_.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]

## Detection

```yaml
selection_img:
- Image|endswith: \forfiles.exe
- OriginalFileName: forfiles.exe
selection_cli:
  CommandLine|contains|windash: ' -c '
condition: all of selection_*
```

## False Positives

- Legitimate use via a batch script or by an administrator.

## References

- https://lolbas-project.github.io/lolbas/Binaries/Forfiles/
- https://pentestlab.blog/2020/07/06/indirect-command-execution/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_forfiles_proxy_execution_.yml)
