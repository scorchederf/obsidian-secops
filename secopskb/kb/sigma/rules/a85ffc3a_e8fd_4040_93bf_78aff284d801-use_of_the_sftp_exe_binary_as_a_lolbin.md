---
sigma_id: "a85ffc3a-e8fd-4040-93bf-78aff284d801"
title: "Use Of The SFTP.EXE Binary As A LOLBIN"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_lolbin_sftp.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_sftp.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "a85ffc3a-e8fd-4040-93bf-78aff284d801"
  - "Use Of The SFTP.EXE Binary As A LOLBIN"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Use Of The SFTP.EXE Binary As A LOLBIN

Detects the usage of the "sftp.exe" binary as a LOLBIN by abusing the "-D" flag

## Metadata

- Rule ID: a85ffc3a-e8fd-4040-93bf-78aff284d801
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-11-10
- Source Path: rules/windows/process_creation/proc_creation_win_lolbin_sftp.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection:
  Image|endswith: \sftp.exe
  CommandLine|contains:
  - ' -D ..'
  - ' -D C:\'
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/LOLBAS-Project/LOLBAS/pull/264

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_sftp.yml)
