---
sigma_id: "5687f942-867b-4578-ade7-1e341c46e99a"
title: "VMToolsd Suspicious Child Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_vmware_vmtoolsd_susp_child_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_vmware_vmtoolsd_susp_child_process.yml"
build_date: "2026-04-27 19:13:58"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "5687f942-867b-4578-ade7-1e341c46e99a"
  - "VMToolsd Suspicious Child Process"
attack_technique_ids:
  - "T1059"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects suspicious child process creations of VMware Tools process which may indicate persistence setup

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]]

## Detection

```yaml
selection_parent:
  ParentImage|endswith: \vmtoolsd.exe
selection_img:
- Image|endswith:
  - \cmd.exe
  - \cscript.exe
  - \mshta.exe
  - \powershell.exe
  - \pwsh.exe
  - \regsvr32.exe
  - \rundll32.exe
  - \wscript.exe
- OriginalFileName:
  - Cmd.Exe
  - cscript.exe
  - MSHTA.EXE
  - PowerShell.EXE
  - pwsh.dll
  - REGSVR32.EXE
  - RUNDLL32.EXE
  - wscript.exe
filter_main_vmwaretools_script:
  Image|endswith: \cmd.exe
  CommandLine|contains:
  - \VMware\VMware Tools\poweron-vm-default.bat
  - \VMware\VMware Tools\poweroff-vm-default.bat
  - \VMware\VMware Tools\resume-vm-default.bat
  - \VMware\VMware Tools\suspend-vm-default.bat
filter_main_empty:
  Image|endswith: \cmd.exe
  CommandLine: ''
filter_main_null:
  Image|endswith: \cmd.exe
  CommandLine: null
condition: all of selection* and not 1 of filter_main_*
```

## False Positives

- Legitimate use by VM administrator

## References

- https://bohops.com/2021/10/08/analyzing-and-detecting-a-vmtools-persistence-technique/
- https://user-images.githubusercontent.com/61026070/136518004-b68cce7d-f9b8-4e9a-9b7b-53b1568a9a94.png
- https://github.com/vmware/open-vm-tools/blob/master/open-vm-tools/tools.conf

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_vmware_vmtoolsd_susp_child_process.yml)
