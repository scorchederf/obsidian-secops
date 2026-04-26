---
sigma_id: "1f49f2ab-26bc-48b3-96cc-dcffbc93eadf"
title: "Potential Suspicious PowerShell Keywords"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_susp_keywords.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_keywords.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "1f49f2ab-26bc-48b3-96cc-dcffbc93eadf"
  - "Potential Suspicious PowerShell Keywords"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Suspicious PowerShell Keywords

Detects potentially suspicious keywords that could indicate the use of a PowerShell exploitation framework

## Metadata

- Rule ID: 1f49f2ab-26bc-48b3-96cc-dcffbc93eadf
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems), Perez Diego (@darkquassar), Tuan Le (NCSGroup)
- Date: 2019-02-11
- Modified: 2023-04-21
- Source Path: rules/windows/powershell/powershell_script/posh_ps_susp_keywords.yml

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
  ScriptBlockText|contains:
  - System.Reflection.Assembly.Load($
  - '[System.Reflection.Assembly]::Load($'
  - '[Reflection.Assembly]::Load($'
  - System.Reflection.AssemblyName
  - Reflection.Emit.AssemblyBuilderAccess
  - Reflection.Emit.CustomAttributeBuilder
  - Runtime.InteropServices.UnmanagedType
  - Runtime.InteropServices.DllImportAttribute
  - SuspendThread
  - rundll32
condition: selection
```

## False Positives

- Unknown

## References

- https://posts.specterops.io/entering-a-covenant-net-command-and-control-e11038bcf462
- https://github.com/PowerShellMafia/PowerSploit/blob/d943001a7defb5e0d1657085a77a0e78609be58f/CodeExecution/Invoke-ReflectivePEInjection.ps1
- https://github.com/hlldz/Phant0m/blob/30c2935d8cf4aafda17ee2fab7cd0c4aa9a607c2/old/Invoke-Phant0m.ps1
- https://gist.github.com/MHaggis/0dbe00ad401daa7137c81c99c268cfb7

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_keywords.yml)
