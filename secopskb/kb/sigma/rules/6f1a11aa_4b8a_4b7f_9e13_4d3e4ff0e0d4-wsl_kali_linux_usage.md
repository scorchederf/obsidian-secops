---
sigma_id: "6f1a11aa-4b8a-4b7f-9e13-4d3e4ff0e0d4"
title: "WSL Kali-Linux Usage"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_wsl_kali_linux_usage.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wsl_kali_linux_usage.yml"
build_date: "2026-04-26 17:03:24"
status: "experimental"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "6f1a11aa-4b8a-4b7f-9e13-4d3e4ff0e0d4"
  - "WSL Kali-Linux Usage"
attack_technique_ids:
  - "T1202"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# WSL Kali-Linux Usage

Detects the use of Kali Linux through Windows Subsystem for Linux

## Metadata

- Rule ID: 6f1a11aa-4b8a-4b7f-9e13-4d3e4ff0e0d4
- Status: experimental
- Level: high
- Author: Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2025-10-10
- Source Path: rules/windows/process_creation/proc_creation_win_wsl_kali_linux_usage.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1202-indirect_command_execution|T1202]]

## Detection

```yaml
selection_img_appdata:
- Image|contains|all:
  - :\Users\
  - \AppData\Local\packages\KaliLinux
- Image|contains|all:
  - :\Users\
  - \AppData\Local\Microsoft\WindowsApps\kali.exe
selection_img_windowsapps:
  Image|contains: :\Program Files\WindowsApps\KaliLinux.
  Image|endswith: \kali.exe
selection_kali_wsl_parent:
  ParentImage|endswith:
  - \wsl.exe
  - \wslhost.exe
selection_kali_wsl_child:
- Image|contains:
  - \kali.exe
  - \KaliLinux
- CommandLine|contains:
  - Kali.exe
  - Kali-linux
  - kalilinux
filter_main_install_uninstall:
  CommandLine|contains:
  - ' -i '
  - ' --install '
  - ' --unregister '
condition: 1 of selection_img_* or all of selection_kali_* and not 1 of filter_main_*
```

## False Positives

- Legitimate installation or usage of Kali Linux WSL by administrators or security teams

## References

- https://medium.com/@redfanatic7/running-kali-linux-on-windows-51ad95166e6e
- https://learn.microsoft.com/en-us/windows/wsl/install

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wsl_kali_linux_usage.yml)
