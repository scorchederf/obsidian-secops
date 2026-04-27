---
sigma_id: "851fd622-b675-4d26-b803-14bc7baa517a"
title: "HackTool - WinPwn Execution - ScriptBlock"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_hktl_winpwn.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_hktl_winpwn.yml"
build_date: "2026-04-27 19:13:51"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects scriptblock text keywords indicative of potential usge of the tool WinPwn. A tool for Windows and Active Directory reconnaissance and exploitation.

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1046-network_service_discovery|T1046: Network Service Discovery]]
- [[kb/attack/techniques/T1082-system_information_discovery|T1082: System Information Discovery]]
- [[kb/attack/techniques/T1106-native_api|T1106: Native API]]
- [[kb/attack/techniques/T1518-software_discovery|T1518: Software Discovery]]
- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism#^t1548002-bypass-user-account-control|T1548.002: Bypass User Account Control]]
- [[kb/attack/techniques/T1552-unsecured_credentials#^t1552001-credentials-in-files|T1552.001: Credentials In Files]]
- [[kb/attack/techniques/T1555-credentials_from_password_stores|T1555: Credentials from Password Stores]]
- [[kb/attack/techniques/T1555-credentials_from_password_stores#^t1555003-credentials-from-web-browsers|T1555.003: Credentials from Web Browsers]]

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
