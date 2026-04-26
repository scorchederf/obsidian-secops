---
sigma_id: "c740d4cf-a1e9-41de-bb16-8a46a4f57918"
title: "Potential Suspicious Windows Feature Enabled - ProcCreation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_enable_susp_windows_optional_feature.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_enable_susp_windows_optional_feature.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "c740d4cf-a1e9-41de-bb16-8a46a4f57918"
  - "Potential Suspicious Windows Feature Enabled - ProcCreation"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Suspicious Windows Feature Enabled - ProcCreation

Detects usage of the built-in PowerShell cmdlet "Enable-WindowsOptionalFeature" used as a Deployment Image Servicing and Management tool.
Similar to DISM.exe, this cmdlet is used to enumerate, install, uninstall, configure, and update features and packages in Windows images

## Metadata

- Rule ID: c740d4cf-a1e9-41de-bb16-8a46a4f57918
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-12-29
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_enable_susp_windows_optional_feature.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_cmd:
  CommandLine|contains|all:
  - Enable-WindowsOptionalFeature
  - -Online
  - -FeatureName
selection_feature:
  CommandLine|contains:
  - TelnetServer
  - Internet-Explorer-Optional-amd64
  - TFTP
  - SMB1Protocol
  - Client-ProjFS
  - Microsoft-Windows-Subsystem-Linux
condition: all of selection_*
```

## False Positives

- Legitimate usage of the features listed in the rule.

## References

- https://learn.microsoft.com/en-us/powershell/module/dism/enable-windowsoptionalfeature?view=windowsserver2022-ps
- https://learn.microsoft.com/en-us/windows/win32/projfs/enabling-windows-projected-file-system
- https://learn.microsoft.com/en-us/windows/wsl/install-on-server

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_enable_susp_windows_optional_feature.yml)
