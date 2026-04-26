---
sigma_id: "8150732a-0c9d-4a99-82b9-9efb9b90c40c"
title: "Suspicious Msiexec Quiet Install From Remote Location"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_msiexec_install_remote.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_msiexec_install_remote.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "8150732a-0c9d-4a99-82b9-9efb9b90c40c"
  - "Suspicious Msiexec Quiet Install From Remote Location"
attack_technique_ids:
  - "T1218.007"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Msiexec Quiet Install From Remote Location

Detects usage of Msiexec.exe to install packages hosted remotely quietly

## Metadata

- Rule ID: 8150732a-0c9d-4a99-82b9-9efb9b90c40c
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-10-28
- Modified: 2025-10-07
- Source Path: rules/windows/process_creation/proc_creation_win_msiexec_install_remote.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.007]]

## Detection

```yaml
selection_img:
- Image|endswith: \msiexec.exe
- OriginalFileName: msiexec.exe
selection_cli:
  CommandLine|contains|windash:
  - -i
  - -package
  - -a
  - -j
selection_quiet:
  CommandLine|contains|windash: -q
selection_remote:
  CommandLine|contains:
  - http
  - \\\\
filter_optional_openoffice:
  CommandLine|contains|all:
  - \AppData\Local\Temp\OpenOffice
  - Installation Files\openoffice
condition: all of selection_* and not 1 of filter_optional_*
```

## False Positives

- Unknown

## References

- https://www.microsoft.com/en-us/security/blog/2022/10/27/raspberry-robin-worm-part-of-larger-ecosystem-facilitating-pre-ransomware-activity/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_msiexec_install_remote.yml)
