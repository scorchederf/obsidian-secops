---
sigma_id: "ed965133-513f-41d9-a441-e38076a0798f"
title: "Suspicious PowerShell Invocations - Generic"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_susp_invocation_generic.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_invocation_generic.yml"
build_date: "2026-04-27 19:13:57"
status: "test"
level: "high"
logsource: "windows / ps_script"
aliases:
  - "ed965133-513f-41d9-a441-e38076a0798f"
  - "Suspicious PowerShell Invocations - Generic"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects suspicious PowerShell invocation command parameters

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]]

## Detection

```yaml
selection_encoded:
  ScriptBlockText|contains:
  - ' -enc '
  - ' -EncodedCommand '
  - ' -ec '
selection_hidden:
  ScriptBlockText|contains:
  - ' -w hidden '
  - ' -window hidden '
  - ' -windowstyle hidden '
  - ' -w 1 '
selection_noninteractive:
  ScriptBlockText|contains:
  - ' -noni '
  - ' -noninteractive '
condition: all of selection*
```

## False Positives

- Very special / sneaky PowerShell scripts

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_invocation_generic.yml)
