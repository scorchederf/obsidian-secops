---
sigma_id: "bafac3d6-7de9-4dd9-8874-4a1194b493ed"
title: "Abusing Print Executable"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_print_remote_file_copy.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_print_remote_file_copy.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "bafac3d6-7de9-4dd9-8874-4a1194b493ed"
  - "Abusing Print Executable"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Abusing Print Executable

Attackers can use print.exe for remote file copy

## Metadata

- Rule ID: bafac3d6-7de9-4dd9-8874-4a1194b493ed
- Status: test
- Level: medium
- Author: Furkan CALISKAN, @caliskanfurkan_, @oscd_initiative
- Date: 2020-10-05
- Modified: 2022-07-07
- Source Path: rules/windows/process_creation/proc_creation_win_print_remote_file_copy.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection:
  Image|endswith: \print.exe
  CommandLine|startswith: print
  CommandLine|contains|all:
  - /D
  - .exe
filter_print:
  CommandLine|contains: print.exe
condition: selection and not filter_print
```

## False Positives

- Unknown

## References

- https://lolbas-project.github.io/lolbas/Binaries/Print/
- https://twitter.com/Oddvarmoe/status/985518877076541440

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_print_remote_file_copy.yml)
