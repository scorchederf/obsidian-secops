---
sigma_id: "aa35a627-33fb-4d04-a165-d33b4afca3e8"
title: "Remote LSASS Process Access Through Windows Remote Management"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_access/proc_access_win_lsass_remote_access_trough_winrm.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_access/proc_access_win_lsass_remote_access_trough_winrm.yml"
build_date: "2026-04-27 19:13:55"
status: "stable"
level: "high"
logsource: "windows / process_access"
aliases:
  - "aa35a627-33fb-4d04-a165-d33b4afca3e8"
  - "Remote LSASS Process Access Through Windows Remote Management"
attack_technique_ids:
  - "T1003.001"
  - "T1059.001"
  - "T1021.006"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects remote access to the LSASS process via WinRM. This could be a sign of credential dumping from tools like mimikatz.

## Logsource

- category: process_access
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping#^t1003001-lsass-memory|T1003.001: LSASS Memory]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]]
- [[kb/attack/techniques/T1021-remote_services#^t1021006-windows-remote-management|T1021.006: Windows Remote Management]]

### Software Tags

- S0002

## Detection

```yaml
selection:
  TargetImage|endswith: \lsass.exe
  SourceImage|endswith: :\Windows\system32\wsmprovhost.exe
filter_main_access:
  GrantedAccess: '0x80000000'
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unlikely

## References

- https://pentestlab.blog/2018/05/15/lateral-movement-winrm/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_access/proc_access_win_lsass_remote_access_trough_winrm.yml)
