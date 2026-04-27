---
sigma_id: "1dd05363-104e-4b4a-b963-196a534b03a1"
title: "Potential Suspicious Mofcomp Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_mofcomp_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_mofcomp_execution.yml"
build_date: "2026-04-27 19:13:54"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "1dd05363-104e-4b4a-b963-196a534b03a1"
  - "Potential Suspicious Mofcomp Execution"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects execution of the "mofcomp" utility as a child of a suspicious shell or script running utility or by having a suspicious path in the commandline.
The "mofcomp" utility parses a file containing MOF statements and adds the classes and class instances defined in the file to the WMI repository.
Attackers abuse this utility to install malicious MOF scripts

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]

## Detection

```yaml
selection_img:
- Image|endswith: \mofcomp.exe
- OriginalFileName: mofcomp.exe
selection_case:
- ParentImage|endswith:
  - \cmd.exe
  - \powershell.exe
  - \pwsh.exe
  - \wsl.exe
  - \wscript.exe
  - \cscript.exe
- CommandLine|contains:
  - \AppData\Local\Temp
  - \Users\Public\
  - \WINDOWS\Temp\
  - '%temp%'
  - '%tmp%'
  - '%appdata%'
filter_main_wmiprvse:
  ParentImage: C:\Windows\System32\wbem\WmiPrvSE.exe
  CommandLine|contains: C:\Windows\TEMP\
  CommandLine|endswith: .mof
filter_optional_null_parent:
  CommandLine|contains: C:\Windows\TEMP\
  CommandLine|endswith: .mof
condition: all of selection_* and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Unknown

## References

- https://thedfirreport.com/2022/07/11/select-xmrig-from-sqlserver/
- https://github.com/The-DFIR-Report/Sigma-Rules/blob/75260568a7ffe61b2458ca05f6f25914efb44337/win_mofcomp_execution.yml
- https://learn.microsoft.com/en-us/windows/win32/wmisdk/mofcomp

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_mofcomp_execution.yml)
