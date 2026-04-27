---
sigma_id: "7b6a7418-3afc-11f0-aff4-000d3abf478c"
title: "Obfuscated PowerShell MSI Install via WindowsInstaller COM"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_comobject_msi.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_comobject_msi.yml"
build_date: "2026-04-27 19:13:53"
status: "experimental"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "7b6a7418-3afc-11f0-aff4-000d3abf478c"
  - "Obfuscated PowerShell MSI Install via WindowsInstaller COM"
attack_technique_ids:
  - "T1027.010"
  - "T1218.007"
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the execution of obfuscated PowerShell commands that attempt to install MSI packages via the Windows Installer COM object (`WindowsInstaller.Installer`).
The technique involves manipulating strings to hide functionality, such as constructing class names using string insertion (e.g., 'indowsInstaller.Installer'.Insert(0,'W')) and correcting
malformed URLs (e.g., converting 'htps://' to 'https://') at runtime. This behavior is commonly associated with malware loaders or droppers that aim to bypass static detection
by hiding intent in runtime-generated strings and using legitimate tools for code execution. The use of `InstallProduct` and COM object creation, particularly combined with
hidden window execution and suppressed UI, indicates an attempt to install software (likely malicious) without user interaction.

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1027-obfuscated_files_or_information#^t1027010-command-obfuscation|T1027.010: Command Obfuscation]]
- [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218007-msiexec|T1218.007: Msiexec]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]]

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
  - .Insert(
  - UILevel
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://informationsecuritybuzz.com/the-real-danger-behind-a-simple-windows-shortcut/
- https://redcanary.com/blog/threat-intelligence/intelligence-insights-may-2025/
- https://www.virustotal.com/gui/file/f9710b0ba4de5fa0e7ec27da462d4d2fc6838eba83a19f23f6617a466bbad457

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_comobject_msi.yml)
