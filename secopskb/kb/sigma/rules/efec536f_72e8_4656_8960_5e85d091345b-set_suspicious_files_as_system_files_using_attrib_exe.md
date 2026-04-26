---
sigma_id: "efec536f-72e8-4656-8960-5e85d091345b"
title: "Set Suspicious Files as System Files Using Attrib.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_attrib_system_susp_paths.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_attrib_system_susp_paths.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "efec536f-72e8-4656-8960-5e85d091345b"
  - "Set Suspicious Files as System Files Using Attrib.EXE"
attack_technique_ids:
  - "T1564.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Set Suspicious Files as System Files Using Attrib.EXE

Detects the usage of attrib with the "+s" option to set scripts or executables located in suspicious locations as system files to hide them from users and make them unable to be deleted with simple rights. The rule limits the search to specific extensions and directories to avoid FPs

## Metadata

- Rule ID: efec536f-72e8-4656-8960-5e85d091345b
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-06-28
- Modified: 2023-03-14
- Source Path: rules/windows/process_creation/proc_creation_win_attrib_system_susp_paths.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1564-hide_artifacts|T1564.001]]

## Detection

```yaml
selection_img:
- Image|endswith: \attrib.exe
- OriginalFileName: ATTRIB.EXE
selection_cli:
  CommandLine|contains: ' +s'
selection_paths:
  CommandLine|contains:
  - ' %'
  - \Users\Public\
  - \AppData\Local\
  - \ProgramData\
  - \Downloads\
  - \Windows\Temp\
selection_ext:
  CommandLine|contains:
  - .bat
  - .dll
  - .exe
  - .hta
  - .ps1
  - .vbe
  - .vbs
filter_optional_installer:
  CommandLine|contains|all:
  - \Windows\TEMP\
  - .exe
condition: all of selection* and not 1 of filter_optional_*
```

## False Positives

- Unknown

## References

- https://app.any.run/tasks/c28cabc8-a19f-40f3-a78b-cae506a5c0d4
- https://app.any.run/tasks/cfc8870b-ccd7-4210-88cf-a8087476a6d0
- https://unit42.paloaltonetworks.com/unit42-sure-ill-take-new-combojack-malware-alters-clipboards-steal-cryptocurrency/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_attrib_system_susp_paths.yml)
