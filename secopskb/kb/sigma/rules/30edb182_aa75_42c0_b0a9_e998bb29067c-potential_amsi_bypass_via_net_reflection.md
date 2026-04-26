---
sigma_id: "30edb182-aa75-42c0-b0a9-e998bb29067c"
title: "Potential AMSI Bypass Via .NET Reflection"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_amsi_init_failed_bypass.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_amsi_init_failed_bypass.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "30edb182-aa75-42c0-b0a9-e998bb29067c"
  - "Potential AMSI Bypass Via .NET Reflection"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potential AMSI Bypass Via .NET Reflection

Detects Request to "amsiInitFailed" that can be used to disable AMSI Scanning

## Metadata

- Rule ID: 30edb182-aa75-42c0-b0a9-e998bb29067c
- Status: test
- Level: high
- Author: Markus Neis, @Kostastsale
- Date: 2018-08-17
- Modified: 2023-02-03
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_amsi_init_failed_bypass.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection:
- CommandLine|contains|all:
  - System.Management.Automation.AmsiUtils
  - amsiInitFailed
- CommandLine|contains|all:
  - '[Ref].Assembly.GetType'
  - SetValue($null,$true)
  - NonPublic,Static
condition: selection
```

## False Positives

- Unlikely

## References

- https://s3cur3th1ssh1t.github.io/Bypass_AMSI_by_manual_modification/
- https://www.mdsec.co.uk/2018/06/exploring-powershell-amsi-and-logging-evasion/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_amsi_init_failed_bypass.yml)
