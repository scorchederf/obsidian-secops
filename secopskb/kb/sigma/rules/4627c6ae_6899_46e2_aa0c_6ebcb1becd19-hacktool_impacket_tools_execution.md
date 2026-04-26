---
sigma_id: "4627c6ae-6899-46e2-aa0c-6ebcb1becd19"
title: "HackTool - Impacket Tools Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_impacket_tools.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_impacket_tools.yml"
build_date: "2026-04-26 14:14:26"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "4627c6ae-6899-46e2-aa0c-6ebcb1becd19"
  - "HackTool - Impacket Tools Execution"
attack_technique_ids:
  - "T1557.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# HackTool - Impacket Tools Execution

Detects the execution of different compiled Windows binaries of the impacket toolset (based on names or part of their names - could lead to false positives)

## Metadata

- Rule ID: 4627c6ae-6899-46e2-aa0c-6ebcb1becd19
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2021-07-24
- Modified: 2023-02-07
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_impacket_tools.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1557-adversary-in-the-middle|T1557.001]]

## Detection

```yaml
selection:
- Image|contains:
  - \goldenPac
  - \karmaSMB
  - \kintercept
  - \ntlmrelayx
  - \rpcdump
  - \samrdump
  - \secretsdump
  - \smbexec
  - \smbrelayx
  - \wmiexec
  - \wmipersist
- Image|endswith:
  - \atexec_windows.exe
  - \dcomexec_windows.exe
  - \dpapi_windows.exe
  - \findDelegation_windows.exe
  - \GetADUsers_windows.exe
  - \GetNPUsers_windows.exe
  - \getPac_windows.exe
  - \getST_windows.exe
  - \getTGT_windows.exe
  - \GetUserSPNs_windows.exe
  - \ifmap_windows.exe
  - \mimikatz_windows.exe
  - \netview_windows.exe
  - \nmapAnswerMachine_windows.exe
  - \opdump_windows.exe
  - \psexec_windows.exe
  - \rdp_check_windows.exe
  - \sambaPipe_windows.exe
  - \smbclient_windows.exe
  - \smbserver_windows.exe
  - \sniff_windows.exe
  - \sniffer_windows.exe
  - \split_windows.exe
  - \ticketer_windows.exe
condition: selection
```

## False Positives

- Legitimate use of the impacket tools

## References

- https://github.com/ropnop/impacket_static_binaries/releases/tag/0.9.21-dev-binaries

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_impacket_tools.yml)
