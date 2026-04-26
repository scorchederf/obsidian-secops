---
sigma_id: "79a87aa6-e4bd-42fc-a5bb-5e6fbdcd62f5"
title: "Msiexec Quiet Installation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_msiexec_install_quiet.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_msiexec_install_quiet.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "79a87aa6-e4bd-42fc-a5bb-5e6fbdcd62f5"
  - "Msiexec Quiet Installation"
attack_technique_ids:
  - "T1218.007"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Msiexec Quiet Installation

Adversaries may abuse msiexec.exe to proxy execution of malicious payloads.
Msiexec.exe is the command-line utility for the Windows Installer and is thus commonly associated with executing installation packages (.msi)

## Metadata

- Rule ID: 79a87aa6-e4bd-42fc-a5bb-5e6fbdcd62f5
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-01-16
- Modified: 2024-12-01
- Source Path: rules/windows/process_creation/proc_creation_win_msiexec_install_quiet.yml

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
filter_user_temp:
  ParentImage|startswith: C:\Users\
  ParentImage|contains: \AppData\Local\Temp\
filter_system_temp:
  ParentImage|startswith: C:\Windows\Temp\
filter_ccm:
  ParentImage: C:\Windows\CCM\Ccm32BitLauncher.exe
  IntegrityLevel:
  - System
  - S-1-16-16384
condition: all of selection_* and not 1 of filter_*
```

## False Positives

- WindowsApps installing updates via the quiet flag

## References

- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/msiexec
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1218.007/T1218.007.md
- https://twitter.com/_st0pp3r_/status/1583914244344799235

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_msiexec_install_quiet.yml)
