---
sigma_id: "a35f5a72-f347-4e36-8895-9869b0d5fc6d"
title: "Suspicious Program Location Whitelisted In Firewall Via Netsh.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_netsh_fw_allow_program_in_susp_location.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_netsh_fw_allow_program_in_susp_location.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "a35f5a72-f347-4e36-8895-9869b0d5fc6d"
  - "Suspicious Program Location Whitelisted In Firewall Via Netsh.EXE"
attack_technique_ids:
  - "T1562.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Suspicious Program Location Whitelisted In Firewall Via Netsh.EXE

Detects Netsh command execution that whitelists a program located in a suspicious location in the Windows Firewall

## Metadata

- Rule ID: a35f5a72-f347-4e36-8895-9869b0d5fc6d
- Status: test
- Level: high
- Author: Sander Wiebing, Jonhnathan Ribeiro, Daniil Yugoslavskiy, oscd.community
- Date: 2020-05-25
- Modified: 2023-12-11
- Source Path: rules/windows/process_creation/proc_creation_win_netsh_fw_allow_program_in_susp_location.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.004]]

## Detection

```yaml
selection_img:
- Image|endswith: \netsh.exe
- OriginalFileName: netsh.exe
selection_cli:
- CommandLine|contains|all:
  - firewall
  - add
  - allowedprogram
- CommandLine|contains|all:
  - advfirewall
  - firewall
  - add
  - rule
  - action=allow
  - program=
selection_paths:
  CommandLine|contains:
  - :\$Recycle.bin\
  - :\RECYCLER.BIN\
  - :\RECYCLERS.BIN\
  - :\SystemVolumeInformation\
  - :\Temp\
  - :\Users\Default\
  - :\Users\Desktop\
  - :\Users\Public\
  - :\Windows\addins\
  - :\Windows\cursors\
  - :\Windows\debug\
  - :\Windows\drivers\
  - :\Windows\fonts\
  - :\Windows\help\
  - :\Windows\system32\tasks\
  - :\Windows\Tasks\
  - :\Windows\Temp\
  - \Downloads\
  - \Local Settings\Temporary Internet Files\
  - \Temporary Internet Files\Content.Outlook\
  - '%Public%\'
  - '%TEMP%'
  - '%TMP%'
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://www.virusradar.com/en/Win32_Kasidet.AD/description
- https://www.hybrid-analysis.com/sample/07e789f4f2f3259e7559fdccb36e96814c2dbff872a21e1fa03de9ee377d581f?environmentId=100

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_netsh_fw_allow_program_in_susp_location.yml)
