---
sigma_id: "90dcf730-1b71-4ae7-9ffc-6fcf62bd0132"
title: "Suspicious ZipExec Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_zipexec.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_zipexec.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "90dcf730-1b71-4ae7-9ffc-6fcf62bd0132"
  - "Suspicious ZipExec Execution"
attack_technique_ids:
  - "T1218"
  - "T1202"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious ZipExec Execution

ZipExec is a Proof-of-Concept (POC) tool to wrap binary-based tools into a password-protected zip file.

## Metadata

- Rule ID: 90dcf730-1b71-4ae7-9ffc-6fcf62bd0132
- Status: test
- Level: medium
- Author: frack113
- Date: 2021-11-07
- Modified: 2022-12-25
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_zipexec.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]
- [[kb/attack/techniques/T1202-indirect_command_execution|T1202]]

## Detection

```yaml
run:
  CommandLine|contains|all:
  - /generic:Microsoft_Windows_Shell_ZipFolder:filename=
  - .zip
  - '/pass:'
  - '/user:'
delete:
  CommandLine|contains|all:
  - /delete
  - Microsoft_Windows_Shell_ZipFolder:filename=
  - .zip
condition: run or delete
```

## False Positives

- Unknown

## References

- https://twitter.com/SBousseaden/status/1451237393017839616
- https://github.com/Tylous/ZipExec

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_zipexec.yml)
