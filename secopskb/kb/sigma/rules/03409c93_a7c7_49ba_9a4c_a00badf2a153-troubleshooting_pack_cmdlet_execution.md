---
sigma_id: "03409c93-a7c7-49ba-9a4c-a00badf2a153"
title: "Troubleshooting Pack Cmdlet Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_susp_follina_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_follina_execution.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "03409c93-a7c7-49ba-9a4c-a00badf2a153"
  - "Troubleshooting Pack Cmdlet Execution"
attack_technique_ids:
  - "T1202"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Troubleshooting Pack Cmdlet Execution

Detects execution of "TroubleshootingPack" cmdlets to leverage CVE-2022-30190 or action similar to "msdt" lolbin (as described in LOLBAS)

## Metadata

- Rule ID: 03409c93-a7c7-49ba-9a4c-a00badf2a153
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-06-21
- Source Path: rules/windows/powershell/powershell_script/posh_ps_susp_follina_execution.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1202-indirect_command_execution|T1202]]

## Detection

```yaml
selection:
  ScriptBlockText|contains|all:
  - Invoke-TroubleshootingPack
  - C:\Windows\Diagnostics\System\PCW
  - -AnswerFile
  - -Unattended
condition: selection
```

## False Positives

- Legitimate usage of "TroubleshootingPack" cmdlet for troubleshooting purposes

## References

- https://twitter.com/nas_bench/status/1537919885031772161
- https://lolbas-project.github.io/lolbas/Binaries/Msdt/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_follina_execution.yml)
