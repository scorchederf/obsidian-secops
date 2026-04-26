---
sigma_id: "eca8ae39-5c3c-4321-b538-9e64fe25822e"
title: "Installation of WSL Kali-Linux"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_wsl_kali_linux_installation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wsl_kali_linux_installation.yml"
build_date: "2026-04-26 14:14:27"
status: "experimental"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "eca8ae39-5c3c-4321-b538-9e64fe25822e"
  - "Installation of WSL Kali-Linux"
attack_technique_ids:
  - "T1059"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Installation of WSL Kali-Linux

Detects installation of Kali Linux distribution through Windows Subsystem for Linux (WSL).
Attackers may use Kali Linux WSL to leverage its penetration testing tools and capabilities for malicious purposes.

## Metadata

- Rule ID: eca8ae39-5c3c-4321-b538-9e64fe25822e
- Status: experimental
- Level: high
- Author: Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2025-10-10
- Source Path: rules/windows/process_creation/proc_creation_win_wsl_kali_linux_installation.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]

## Detection

```yaml
selection_wsl_img:
- Image|endswith: \wsl.exe
- OriginalFileName: wsl
selection_wsl_install:
  CommandLine|contains:
  - ' --install '
  - ' -i '
selection_wsl_kali:
  CommandLine|contains: kali
condition: all of selection_wsl_*
```

## False Positives

- Legitimate installation or usage of Kali Linux WSL by administrators or security teams

## References

- https://medium.com/@redfanatic7/running-kali-linux-on-windows-51ad95166e6e
- https://learn.microsoft.com/en-us/windows/wsl/install

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wsl_kali_linux_installation.yml)
