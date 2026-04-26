---
sigma_id: "8823e85d-31d8-473e-b7f4-92da070f0fc6"
title: "Suspicious ShellExec_RunDLL Call Via Ordinal"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_rundll32_susp_shellexec_ordinal_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_susp_shellexec_ordinal_execution.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "8823e85d-31d8-473e-b7f4-92da070f0fc6"
  - "Suspicious ShellExec_RunDLL Call Via Ordinal"
attack_technique_ids:
  - "T1218.011"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious ShellExec_RunDLL Call Via Ordinal

Detects suspicious call to the "ShellExec_RunDLL" exported function of SHELL32.DLL through the ordinal number to launch other commands.
Adversary might only use the ordinal number in order to bypass existing detection that alert on usage of ShellExec_RunDLL on CommandLine.

## Metadata

- Rule ID: 8823e85d-31d8-473e-b7f4-92da070f0fc6
- Status: test
- Level: high
- Author: Swachchhanda Shrawan Poudel
- Date: 2024-12-01
- Source Path: rules/windows/process_creation/proc_creation_win_rundll32_susp_shellexec_ordinal_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.011]]

## Detection

```yaml
selection_parent_img:
  ParentCommandLine|contains: SHELL32.DLL
selection_parent_ordinal:
  ParentCommandLine|contains:
  - '#568'
  - '#570'
  - '#572'
  - '#576'
selection_susp_cli_parent:
- ParentCommandLine|contains:
  - comspec
  - iex
  - Invoke-
  - msiexec
  - odbcconf
  - regsvr32
- ParentCommandLine|contains:
  - \Desktop\
  - \ProgramData\
  - \Temp\
  - \Users\Public\
selection_susp_child_img:
  Image|endswith:
  - \bash.exe
  - \bitsadmin.exe
  - \cmd.exe
  - \cscript.exe
  - \curl.exe
  - \mshta.exe
  - \msiexec.exe
  - \msxsl.exe
  - \odbcconf.exe
  - \powershell.exe
  - \pwsh.exe
  - \regsvr32.exe
  - \schtasks.exe
  - \wmic.exe
  - \wscript.exe
condition: all of selection_parent_* and 1 of selection_susp_*
```

## False Positives

- Unknown

## References

- https://redcanary.com/blog/raspberry-robin/
- https://www.microsoft.com/en-us/security/blog/2022/10/27/raspberry-robin-worm-part-of-larger-ecosystem-facilitating-pre-ransomware-activity/
- https://github.com/SigmaHQ/sigma/issues/1009
- https://strontic.github.io/xcyclopedia/library/shell32.dll-65DA072F25DE83D9F83653E3FEA3644D.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_susp_shellexec_ordinal_execution.yml)
