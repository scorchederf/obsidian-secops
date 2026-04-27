---
sigma_id: "6f0947a4-1c5e-4e0d-8ac7-53159b8f23ca"
title: "Potentially Suspicious Child Process Of Regsvr32"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_regsvr32_susp_child_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_regsvr32_susp_child_process.yml"
build_date: "2026-04-27 19:13:54"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "6f0947a4-1c5e-4e0d-8ac7-53159b8f23ca"
  - "Potentially Suspicious Child Process Of Regsvr32"
attack_technique_ids:
  - "T1218.010"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects potentially suspicious child processes of "regsvr32.exe".

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218010-regsvr32|T1218.010: Regsvr32]]

## Detection

```yaml
selection:
  ParentImage|endswith: \regsvr32.exe
  Image|endswith:
  - \calc.exe
  - \cscript.exe
  - \explorer.exe
  - \mshta.exe
  - \net.exe
  - \net1.exe
  - \nltest.exe
  - \notepad.exe
  - \powershell.exe
  - \pwsh.exe
  - \reg.exe
  - \schtasks.exe
  - \werfault.exe
  - \wscript.exe
filter_main_werfault:
  Image|endswith: \werfault.exe
  CommandLine|contains: ' -u -p '
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unlikely, but can rarely occur. Apply additional filters accordingly.

## References

- https://redcanary.com/blog/intelligence-insights-april-2022/
- https://www.echotrail.io/insights/search/regsvr32.exe
- https://www.ired.team/offensive-security/code-execution/t1117-regsvr32-aka-squiblydoo

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_regsvr32_susp_child_process.yml)
