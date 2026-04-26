---
sigma_id: "d4498716-1d52-438f-8084-4a603157d131"
title: "Password Provided In Command Line Of Net.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_net_use_password_plaintext.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_net_use_password_plaintext.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "d4498716-1d52-438f-8084-4a603157d131"
  - "Password Provided In Command Line Of Net.EXE"
attack_technique_ids:
  - "T1021.002"
  - "T1078"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Password Provided In Command Line Of Net.EXE

Detects a when net.exe is called with a password in the command line

## Metadata

- Rule ID: d4498716-1d52-438f-8084-4a603157d131
- Status: test
- Level: medium
- Author: Tim Shelton (HAWK.IO)
- Date: 2021-12-09
- Modified: 2023-02-21
- Source Path: rules/windows/process_creation/proc_creation_win_net_use_password_plaintext.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1021-remote_services|T1021.002]]
- [[kb/attack/techniques/T1078-valid_accounts|T1078]]

## Detection

```yaml
selection_img:
- Image|endswith:
  - \net.exe
  - \net1.exe
- OriginalFileName:
  - net.exe
  - net1.exe
selection_cli:
  CommandLine|contains|all:
  - ' use '
  - :*\\
  - /USER:* *
filter_main_empty:
  CommandLine|endswith: ' '
condition: all of selection_* and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_net_use_password_plaintext.yml)
