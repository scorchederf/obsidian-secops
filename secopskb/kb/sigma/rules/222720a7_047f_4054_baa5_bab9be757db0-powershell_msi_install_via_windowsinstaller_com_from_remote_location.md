---
sigma_id: "222720a7-047f-4054-baa5-bab9be757db0"
title: "PowerShell MSI Install via WindowsInstaller COM From Remote Location"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_comobject_msi_remote.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_comobject_msi_remote.yml"
build_date: "2026-04-26 14:14:33"
status: "experimental"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "222720a7-047f-4054-baa5-bab9be757db0"
  - "PowerShell MSI Install via WindowsInstaller COM From Remote Location"
attack_technique_ids:
  - "T1059.001"
  - "T1218"
  - "T1105"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PowerShell MSI Install via WindowsInstaller COM From Remote Location

Detects the execution of PowerShell commands that attempt to install MSI packages via the
Windows Installer COM object (`WindowsInstaller.Installer`) hosted remotely.
This could be indication of malicious software deployment or lateral movement attempts using Windows Installer functionality.
And the usage of WindowsInstaller COM object rather than msiexec could be an attempt to bypass the detection.

## Metadata

- Rule ID: 222720a7-047f-4054-baa5-bab9be757db0
- Status: experimental
- Level: medium
- Author: Meroujan Antonyan (vx3r)
- Date: 2025-06-05
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_comobject_msi_remote.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]
- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]
- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Detection

```yaml
selection_img:
- Image|endswith:
  - \powershell_ise.exe
  - \powershell.exe
  - \pwsh.exe
- OriginalFileName:
  - PowerShell_ISE.EXE
  - PowerShell.EXE
  - pwsh.dll
selection_cli:
  CommandLine|contains|all:
  - -ComObject
  - InstallProduct(
selection_remote:
  CommandLine|contains:
  - http
  - \\\\
filter_main_localhost:
  CommandLine|contains:
  - ://127.0.0.1
  - ://localhost
condition: all of selection_* and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://informationsecuritybuzz.com/the-real-danger-behind-a-simple-windows-shortcut/
- https://redcanary.com/blog/threat-intelligence/intelligence-insights-may-2025/
- https://www.virustotal.com/gui/file/f9710b0ba4de5fa0e7ec27da462d4d2fc6838eba83a19f23f6617a466bbad457

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_comobject_msi_remote.yml)
