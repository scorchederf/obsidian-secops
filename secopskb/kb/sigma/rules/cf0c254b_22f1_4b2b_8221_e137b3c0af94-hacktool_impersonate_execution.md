---
sigma_id: "cf0c254b-22f1-4b2b-8221-e137b3c0af94"
title: "HackTool - Impersonate Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_impersonate.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_impersonate.yml"
build_date: "2026-04-26 14:14:26"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "cf0c254b-22f1-4b2b-8221-e137b3c0af94"
  - "HackTool - Impersonate Execution"
attack_technique_ids:
  - "T1134.001"
  - "T1134.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# HackTool - Impersonate Execution

Detects execution of the Impersonate tool. Which can be used to manipulate tokens on a Windows computers remotely (PsExec/WmiExec) or interactively

## Metadata

- Rule ID: cf0c254b-22f1-4b2b-8221-e137b3c0af94
- Status: test
- Level: medium
- Author: Sai Prashanth Pulisetti @pulisettis
- Date: 2022-12-21
- Modified: 2024-11-23
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_impersonate.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1134-access_token_manipulation|T1134.001]]
- [[kb/attack/techniques/T1134-access_token_manipulation|T1134.003]]

## Detection

```yaml
selection_commandline_exe:
  CommandLine|contains: impersonate.exe
selection_commandline_opt:
  CommandLine|contains:
  - ' list '
  - ' exec '
  - ' adduser '
selection_hash:
  Hashes|contains:
  - MD5=9520714AB576B0ED01D1513691377D01
  - SHA256=E81CC96E2118DC4FBFE5BAD1604E0AC7681960143E2101E1A024D52264BB0A8A
  - IMPHASH=0A358FFC1697B7A07D0E817AC740DF62
condition: all of selection_commandline_* or selection_hash
```

## False Positives

- Unknown

## References

- https://sensepost.com/blog/2022/abusing-windows-tokens-to-compromise-active-directory-without-touching-lsass/
- https://github.com/sensepost/impersonate

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_impersonate.yml)
