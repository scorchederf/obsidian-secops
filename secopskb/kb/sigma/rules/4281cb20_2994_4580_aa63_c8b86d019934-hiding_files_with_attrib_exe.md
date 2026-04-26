---
sigma_id: "4281cb20-2994-4580-aa63-c8b86d019934"
title: "Hiding Files with Attrib.exe"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_attrib_hiding_files.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_attrib_hiding_files.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "4281cb20-2994-4580-aa63-c8b86d019934"
  - "Hiding Files with Attrib.exe"
attack_technique_ids:
  - "T1564.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Hiding Files with Attrib.exe

Detects usage of attrib.exe to hide files from users.

## Metadata

- Rule ID: 4281cb20-2994-4580-aa63-c8b86d019934
- Status: test
- Level: medium
- Author: Sami Ruohonen
- Date: 2019-01-16
- Modified: 2023-03-14
- Source Path: rules/windows/process_creation/proc_creation_win_attrib_hiding_files.yml

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
  CommandLine|contains: ' +h '
filter_main_msiexec:
  CommandLine|contains: '\desktop.ini '
filter_optional_intel:
  ParentImage|endswith: \cmd.exe
  CommandLine: +R +H +S +A \\\*.cui
  ParentCommandLine: C:\\WINDOWS\\system32\\\*.bat
condition: all of selection_* and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- IgfxCUIService.exe hiding *.cui files via .bat script (attrib.exe a child of cmd.exe and igfxCUIService.exe is the parent of the cmd.exe)
- Msiexec.exe hiding desktop.ini

## References

- https://unit42.paloaltonetworks.com/unit42-sure-ill-take-new-combojack-malware-alters-clipboards-steal-cryptocurrency/
- https://www.uptycs.com/blog/lolbins-are-no-laughing-matter

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_attrib_hiding_files.yml)
