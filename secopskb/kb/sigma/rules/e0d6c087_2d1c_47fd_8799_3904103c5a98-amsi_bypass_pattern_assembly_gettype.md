---
sigma_id: "e0d6c087-2d1c-47fd-8799-3904103c5a98"
title: "AMSI Bypass Pattern Assembly GetType"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_amsi_bypass_pattern_nov22.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_amsi_bypass_pattern_nov22.yml"
build_date: "2026-04-26 14:14:19"
status: "test"
level: "high"
logsource: "windows / ps_script"
aliases:
  - "e0d6c087-2d1c-47fd-8799-3904103c5a98"
  - "AMSI Bypass Pattern Assembly GetType"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# AMSI Bypass Pattern Assembly GetType

Detects code fragments found in small and obfuscated AMSI bypass PowerShell scripts

## Metadata

- Rule ID: e0d6c087-2d1c-47fd-8799-3904103c5a98
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-11-09
- Source Path: rules/windows/powershell/powershell_script/posh_ps_amsi_bypass_pattern_nov22.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection:
  ScriptBlockText|contains|all:
  - '[Ref].Assembly.GetType'
  - SetValue($null,$true)
  - NonPublic,Static
condition: selection
```

## False Positives

- Unknown

## References

- https://www.mdsec.co.uk/2018/06/exploring-powershell-amsi-and-logging-evasion/
- https://twitter.com/cyb3rops/status/1588574518057979905?s=20&t=A7hh93ONM7ni1Rj1jO5OaA

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_amsi_bypass_pattern_nov22.yml)
