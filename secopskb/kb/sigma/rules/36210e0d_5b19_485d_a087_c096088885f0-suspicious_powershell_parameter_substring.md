---
sigma_id: "36210e0d-5b19-485d-a087-c096088885f0"
title: "Suspicious PowerShell Parameter Substring"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_susp_parameter_variation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_susp_parameter_variation.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "36210e0d-5b19-485d-a087-c096088885f0"
  - "Suspicious PowerShell Parameter Substring"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Suspicious PowerShell Parameter Substring

Detects suspicious PowerShell invocation with a parameter substring

## Metadata

- Rule ID: 36210e0d-5b19-485d-a087-c096088885f0
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems), Daniel Bohannon (idea), Roberto Rodriguez (Fix)
- Date: 2019-01-16
- Modified: 2022-07-14
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_susp_parameter_variation.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection:
  Image|endswith:
  - \powershell.exe
  - \pwsh.exe
  CommandLine|contains:
  - ' -windowstyle h '
  - ' -windowstyl h'
  - ' -windowsty h'
  - ' -windowst h'
  - ' -windows h'
  - ' -windo h'
  - ' -wind h'
  - ' -win h'
  - ' -wi h'
  - ' -win h '
  - ' -win hi '
  - ' -win hid '
  - ' -win hidd '
  - ' -win hidde '
  - ' -NoPr '
  - ' -NoPro '
  - ' -NoProf '
  - ' -NoProfi '
  - ' -NoProfil '
  - ' -nonin '
  - ' -nonint '
  - ' -noninte '
  - ' -noninter '
  - ' -nonintera '
  - ' -noninterac '
  - ' -noninteract '
  - ' -noninteracti '
  - ' -noninteractiv '
  - ' -ec '
  - ' -encodedComman '
  - ' -encodedComma '
  - ' -encodedComm '
  - ' -encodedCom '
  - ' -encodedCo '
  - ' -encodedC '
  - ' -encoded '
  - ' -encode '
  - ' -encod '
  - ' -enco '
  - ' -en '
  - ' -executionpolic '
  - ' -executionpoli '
  - ' -executionpol '
  - ' -executionpo '
  - ' -executionp '
  - ' -execution bypass'
  - ' -executio bypass'
  - ' -executi bypass'
  - ' -execut bypass'
  - ' -execu bypass'
  - ' -exec bypass'
  - ' -exe bypass'
  - ' -ex bypass'
  - ' -ep bypass'
  - ' /windowstyle h '
  - ' /windowstyl h'
  - ' /windowsty h'
  - ' /windowst h'
  - ' /windows h'
  - ' /windo h'
  - ' /wind h'
  - ' /win h'
  - ' /wi h'
  - ' /win h '
  - ' /win hi '
  - ' /win hid '
  - ' /win hidd '
  - ' /win hidde '
  - ' /NoPr '
  - ' /NoPro '
  - ' /NoProf '
  - ' /NoProfi '
  - ' /NoProfil '
  - ' /nonin '
  - ' /nonint '
  - ' /noninte '
  - ' /noninter '
  - ' /nonintera '
  - ' /noninterac '
  - ' /noninteract '
  - ' /noninteracti '
  - ' /noninteractiv '
  - ' /ec '
  - ' /encodedComman '
  - ' /encodedComma '
  - ' /encodedComm '
  - ' /encodedCom '
  - ' /encodedCo '
  - ' /encodedC '
  - ' /encoded '
  - ' /encode '
  - ' /encod '
  - ' /enco '
  - ' /en '
  - ' /executionpolic '
  - ' /executionpoli '
  - ' /executionpol '
  - ' /executionpo '
  - ' /executionp '
  - ' /execution bypass'
  - ' /executio bypass'
  - ' /executi bypass'
  - ' /execut bypass'
  - ' /execu bypass'
  - ' /exec bypass'
  - ' /exe bypass'
  - ' /ex bypass'
  - ' /ep bypass'
condition: selection
```

## False Positives

- Unknown

## References

- http://www.danielbohannon.com/blog-1/2017/3/12/powershell-execution-argument-obfuscation-how-it-can-make-detection-easier

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_susp_parameter_variation.yml)
