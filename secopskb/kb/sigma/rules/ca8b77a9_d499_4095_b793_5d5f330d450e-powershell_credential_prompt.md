---
sigma_id: "ca8b77a9-d499-4095-b793-5d5f330d450e"
title: "PowerShell Credential Prompt"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_prompt_credentials.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_prompt_credentials.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "windows / ps_script"
aliases:
  - "ca8b77a9-d499-4095-b793-5d5f330d450e"
  - "PowerShell Credential Prompt"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# PowerShell Credential Prompt

Detects PowerShell calling a credential prompt

## Metadata

- Rule ID: ca8b77a9-d499-4095-b793-5d5f330d450e
- Status: test
- Level: high
- Author: John Lambert (idea), Florian Roth (Nextron Systems)
- Date: 2017-04-09
- Modified: 2022-12-25
- Source Path: rules/windows/powershell/powershell_script/posh_ps_prompt_credentials.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection:
  ScriptBlockText|contains: PromptForCredential
condition: selection
```

## False Positives

- Unknown

## References

- https://twitter.com/JohnLaTwC/status/850381440629981184
- https://t.co/ezOTGy1a1G

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_prompt_credentials.yml)
