---
sigma_id: "9465ddf4-f9e4-4ebd-8d98-702df3a93239"
title: "IIS Native-Code Module Command Line Installation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_iis_appcmd_susp_module_install.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_iis_appcmd_susp_module_install.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "9465ddf4-f9e4-4ebd-8d98-702df3a93239"
  - "IIS Native-Code Module Command Line Installation"
attack_technique_ids:
  - "T1505.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# IIS Native-Code Module Command Line Installation

Detects suspicious IIS native-code module installations via command line

## Metadata

- Rule ID: 9465ddf4-f9e4-4ebd-8d98-702df3a93239
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2019-12-11
- Modified: 2024-03-13
- Source Path: rules/windows/process_creation/proc_creation_win_iis_appcmd_susp_module_install.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1505-server_software_component|T1505.003]]

## Detection

```yaml
selection_img:
- Image|endswith: \appcmd.exe
- OriginalFileName: appcmd.exe
selection_cli:
  CommandLine|contains|all:
  - install
  - module
  CommandLine|contains|windash: '-name:'
filter_iis_setup:
  ParentImage: C:\Windows\System32\inetsrv\iissetup.exe
condition: all of selection_* and not 1 of filter_*
```

## False Positives

- Unknown as it may vary from organisation to organisation how admins use to install IIS modules

## References

- https://researchcenter.paloaltonetworks.com/2018/01/unit42-oilrig-uses-rgdoor-iis-backdoor-targets-middle-east/
- https://www.microsoft.com/security/blog/2022/07/26/malicious-iis-extensions-quietly-open-persistent-backdoors-into-servers/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_iis_appcmd_susp_module_install.yml)
