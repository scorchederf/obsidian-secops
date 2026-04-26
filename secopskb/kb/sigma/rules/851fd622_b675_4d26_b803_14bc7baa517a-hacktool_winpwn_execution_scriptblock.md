---
sigma_id: "851fd622-b675-4d26-b803-14bc7baa517a"
title: "HackTool - WinPwn Execution - ScriptBlock"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_hktl_winpwn.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_hktl_winpwn.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "high"
logsource: "windows / ps_script"
aliases:
  - "851fd622-b675-4d26-b803-14bc7baa517a"
  - "HackTool - WinPwn Execution - ScriptBlock"
attack_technique_ids:
  - "T1046"
  - "T1082"
  - "T1106"
  - "T1518"
  - "T1548.002"
  - "T1552.001"
  - "T1555"
  - "T1555.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# HackTool - WinPwn Execution - ScriptBlock

Detects scriptblock text keywords indicative of potential usge of the tool WinPwn. A tool for Windows and Active Directory reconnaissance and exploitation.

## Metadata

- Rule ID: 851fd622-b675-4d26-b803-14bc7baa517a
- Status: test
- Level: high
- Author: Swachchhanda Shrawan Poudel
- Date: 2023-12-04
- Source Path: rules/windows/powershell/powershell_script/posh_ps_hktl_winpwn.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1046-network_service_discovery|T1046]]
- [[kb/attack/techniques/T1082-system_information_discovery|T1082]]
- [[kb/attack/techniques/T1106-native_api|T1106]]
- [[kb/attack/techniques/T1518-software_discovery|T1518]]
- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548.002]]
- [[kb/attack/techniques/T1552-unsecured_credentials|T1552.001]]
- [[kb/attack/techniques/T1555-credentials_from_password_stores|T1555]]
- [[kb/attack/techniques/T1555-credentials_from_password_stores|T1555.003]]

## Detection

```yaml
selection:
  ScriptBlockText|contains:
  - Offline_Winpwn
  - 'WinPwn '
  - WinPwn.exe
  - WinPwn.ps1
condition: selection
```

## False Positives

- As the script block is a blob of text. False positive may occur with scripts that contain the keyword as a reference or simply use it for detection.

## References

- https://github.com/S3cur3Th1sSh1t/WinPwn
- https://www.publicnow.com/view/EB87DB49C654D9B63995FAD4C9DE3D3CC4F6C3ED?1671634841
- https://reconshell.com/winpwn-tool-for-internal-windows-pentesting-and-ad-security/
- https://github.com/redcanaryco/atomic-red-team/blob/4d6c4e8e23d465af7a2388620cfe3f8c76e16cf0/atomics/T1082/T1082.md
- https://grep.app/search?q=winpwn&filter[repo][0]=redcanaryco/atomic-red-team

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_hktl_winpwn.yml)
