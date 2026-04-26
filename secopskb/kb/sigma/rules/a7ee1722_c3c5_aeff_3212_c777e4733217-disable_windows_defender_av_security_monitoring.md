---
sigma_id: "a7ee1722-c3c5-aeff-3212-c777e4733217"
title: "Disable Windows Defender AV Security Monitoring"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_disable_defender_av_security_monitoring.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_disable_defender_av_security_monitoring.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "a7ee1722-c3c5-aeff-3212-c777e4733217"
  - "Disable Windows Defender AV Security Monitoring"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Disable Windows Defender AV Security Monitoring

Detects attackers attempting to disable Windows Defender using Powershell

## Metadata

- Rule ID: a7ee1722-c3c5-aeff-3212-c777e4733217
- Status: test
- Level: high
- Author: ok @securonix invrep-de, oscd.community, frack113
- Date: 2020-10-12
- Modified: 2022-11-18
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_disable_defender_av_security_monitoring.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection_pwsh_binary:
- Image|endswith:
  - \powershell.exe
  - \pwsh.exe
- OriginalFileName:
  - PowerShell.EXE
  - pwsh.dll
selection_pwsh_cli:
  CommandLine|contains:
  - -DisableBehaviorMonitoring $true
  - -DisableRuntimeMonitoring $true
selection_sc_binary:
- Image|endswith: \sc.exe
- OriginalFileName: sc.exe
selection_sc_tamper_cmd_stop:
  CommandLine|contains|all:
  - stop
  - WinDefend
selection_sc_tamper_cmd_delete:
  CommandLine|contains|all:
  - delete
  - WinDefend
selection_sc_tamper_cmd_disabled:
  CommandLine|contains|all:
  - config
  - WinDefend
  - start=disabled
condition: all of selection_pwsh_* or (selection_sc_binary and 1 of selection_sc_tamper_*)
```

## False Positives

- Minimal, for some older versions of dev tools, such as pycharm, developers were known to sometimes disable Windows Defender to improve performance, but this generally is not considered a good security practice.

## References

- https://research.nccgroup.com/2020/06/23/wastedlocker-a-new-ransomware-variant-developed-by-the-evil-corp-group/
- https://rvsec0n.wordpress.com/2020/01/24/malwares-that-bypass-windows-defender/
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1562.001/T1562.001.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_disable_defender_av_security_monitoring.yml)
