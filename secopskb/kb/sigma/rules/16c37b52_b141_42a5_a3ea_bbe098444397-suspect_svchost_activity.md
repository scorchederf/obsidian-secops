---
sigma_id: "16c37b52-b141-42a5-a3ea-bbe098444397"
title: "Suspect Svchost Activity"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_svchost_execution_with_no_cli_flags.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_svchost_execution_with_no_cli_flags.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "16c37b52-b141-42a5-a3ea-bbe098444397"
  - "Suspect Svchost Activity"
attack_technique_ids:
  - "T1055"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspect Svchost Activity

It is extremely abnormal for svchost.exe to spawn without any CLI arguments and is normally observed when a malicious process spawns the process and injects code into the process memory space.

## Metadata

- Rule ID: 16c37b52-b141-42a5-a3ea-bbe098444397
- Status: test
- Level: high
- Author: David Burkett, @signalblur
- Date: 2019-12-28
- Modified: 2022-06-27
- Source Path: rules/windows/process_creation/proc_creation_win_svchost_execution_with_no_cli_flags.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1055-process_injection|T1055]]

## Detection

```yaml
selection:
  CommandLine|endswith: svchost.exe
  Image|endswith: \svchost.exe
filter:
- ParentImage|endswith:
  - \rpcnet.exe
  - \rpcnetp.exe
- CommandLine: null
condition: selection and not filter
```

## False Positives

- Rpcnet.exe / rpcnetp.exe which is a lojack style software. https://www.blackhat.com/docs/us-14/materials/us-14-Kamlyuk-Kamluk-Computrace-Backdoor-Revisited.pdf

## References

- https://web.archive.org/web/20180718061628/https://securitybytes.io/blue-team-fundamentals-part-two-windows-processes-759fe15965e2

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_svchost_execution_with_no_cli_flags.yml)
