---
sigma_id: "c70e019b-1479-4b65-b0cc-cd0c6093a599"
title: "PowerShell Called from an Executable Version Mismatch"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_classic/posh_pc_exe_calling_ps.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_classic/posh_pc_exe_calling_ps.yml"
build_date: "2026-04-27 19:13:55"
status: "test"
level: "high"
logsource: "windows / ps_classic_start"
aliases:
  - "c70e019b-1479-4b65-b0cc-cd0c6093a599"
  - "PowerShell Called from an Executable Version Mismatch"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects PowerShell called from an executable by the version mismatch method

## Logsource

- category: ps_classic_start
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]]

## Detection

```yaml
selection_engine:
  Data|contains:
  - EngineVersion=2.
  - EngineVersion=4.
  - EngineVersion=5.
selection_host:
  Data|contains: HostVersion=3.
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://adsecurity.org/?p=2921

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_classic/posh_pc_exe_calling_ps.yml)
