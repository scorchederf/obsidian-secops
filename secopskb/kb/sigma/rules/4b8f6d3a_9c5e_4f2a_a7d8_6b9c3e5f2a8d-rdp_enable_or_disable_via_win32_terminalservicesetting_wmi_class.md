---
sigma_id: "4b8f6d3a-9c5e-4f2a-a7d8-6b9c3e5f2a8d"
title: "RDP Enable or Disable via Win32_TerminalServiceSetting WMI Class"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_rdp_enable_or_disable_via_win32_terminalservicesetting_wmi_class.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rdp_enable_or_disable_via_win32_terminalservicesetting_wmi_class.yml"
build_date: "2026-04-26 14:14:34"
status: "experimental"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "4b8f6d3a-9c5e-4f2a-a7d8-6b9c3e5f2a8d"
  - "RDP Enable or Disable via Win32_TerminalServiceSetting WMI Class"
attack_technique_ids:
  - "T1021.001"
  - "T1047"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# RDP Enable or Disable via Win32_TerminalServiceSetting WMI Class

Detects enabling or disabling of Remote Desktop Protocol (RDP) using alternate methods such as WMIC or PowerShell.
In PowerShell one-liner commands, the "SetAllowTSConnections" method of the "Win32_TerminalServiceSetting" class may be used to enable or disable RDP.
In WMIC, the "rdtoggle" alias or "Win32_TerminalServiceSetting" class may be used for the same purpose.

## Metadata

- Rule ID: 4b8f6d3a-9c5e-4f2a-a7d8-6b9c3e5f2a8d
- Status: experimental
- Level: medium
- Author: Daniel Koifman (KoifSec), Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2025-11-15
- Source Path: rules/windows/process_creation/proc_creation_win_rdp_enable_or_disable_via_win32_terminalservicesetting_wmi_class.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1021-remote_services|T1021.001]]
- [[kb/attack/techniques/T1047-windows_management_instrumentation|T1047]]

## Detection

```yaml
selection_img:
- Image|endswith:
  - \wmic.exe
  - \powershell.exe
  - \pwsh.exe
- OriginalFileName:
  - wmic.exe
  - PowerShell.EXE
  - pwsh.dll
selection_cli_method:
  CommandLine|contains:
  - rdtoggle
  - Win32_TerminalServiceSetting
selection_cli_property:
  CommandLine|contains: SetAllowTSConnections
condition: all of selection_*
```

## False Positives

- Legitimate system administrators enabling RDP for remote support
- System configuration scripts during deployment

## References

- https://www.trendmicro.com/en_gb/research/22/e/uncovering-a-kingminer-botnet-attack-using-trend-micro-managed-x.html
- https://github.com/HackTricks-wiki/hacktricks/blob/72f20a3fa26775b932bd819f1824c6377802a768/src/windows-hardening/basic-cmd-for-pentesters.md#firewall
- https://github.com/Lifailon/RSA/blob/rsa/Sources/RSA-1.4.1.ps1#L1468

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rdp_enable_or_disable_via_win32_terminalservicesetting_wmi_class.yml)
