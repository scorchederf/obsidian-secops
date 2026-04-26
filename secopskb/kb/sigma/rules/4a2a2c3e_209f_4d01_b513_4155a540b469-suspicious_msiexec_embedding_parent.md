---
sigma_id: "4a2a2c3e-209f-4d01-b513-4155a540b469"
title: "Suspicious MsiExec Embedding Parent"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_msiexec_embedding.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_msiexec_embedding.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "4a2a2c3e-209f-4d01-b513-4155a540b469"
  - "Suspicious MsiExec Embedding Parent"
attack_technique_ids:
  - "T1218.007"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious MsiExec Embedding Parent

Adversaries may abuse msiexec.exe to proxy the execution of malicious payloads

## Metadata

- Rule ID: 4a2a2c3e-209f-4d01-b513-4155a540b469
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-04-16
- Modified: 2022-07-14
- Source Path: rules/windows/process_creation/proc_creation_win_msiexec_embedding.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.007]]

## Detection

```yaml
selection:
  Image|endswith:
  - \powershell.exe
  - \pwsh.exe
  - \cmd.exe
  ParentCommandLine|contains|all:
  - MsiExec.exe
  - '-Embedding '
filter_splunk_ufw:
  Image|endswith: :\Windows\System32\cmd.exe
  CommandLine|contains: C:\Program Files\SplunkUniversalForwarder\bin\
filter_vs:
- CommandLine|contains: \DismFoDInstall.cmd
- ParentCommandLine|contains|all:
  - '\MsiExec.exe -Embedding '
  - Global\MSI0000
condition: selection and not 1 of filter*
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1218.007/T1218.007.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_msiexec_embedding.yml)
