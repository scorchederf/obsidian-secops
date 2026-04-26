---
sigma_id: "114de787-4eb2-48cc-abdb-c0b449f93ea4"
title: "Suspicious X509Enrollment - Process Creation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_x509enrollment.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_x509enrollment.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "114de787-4eb2-48cc-abdb-c0b449f93ea4"
  - "Suspicious X509Enrollment - Process Creation"
attack_technique_ids:
  - "T1553.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious X509Enrollment - Process Creation

Detect use of X509Enrollment

## Metadata

- Rule ID: 114de787-4eb2-48cc-abdb-c0b449f93ea4
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-12-23
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_x509enrollment.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1553-subvert_trust_controls|T1553.004]]

## Detection

```yaml
selection:
  CommandLine|contains:
  - X509Enrollment.CBinaryConverter
  - 884e2002-217d-11da-b2a4-000e7bbb2b09
condition: selection
```

## False Positives

- Legitimate administrative script

## References

- https://speakerdeck.com/heirhabarov/hunting-for-powershell-abuse?slide=42
- https://speakerdeck.com/heirhabarov/hunting-for-powershell-abuse?slide=41
- https://learn.microsoft.com/en-us/dotnet/api/microsoft.hpc.scheduler.store.cx509enrollmentwebclassfactoryclass?view=hpc-sdk-5.1.6115

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_x509enrollment.yml)
