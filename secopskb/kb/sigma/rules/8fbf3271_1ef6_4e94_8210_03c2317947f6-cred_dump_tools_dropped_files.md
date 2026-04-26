---
sigma_id: "8fbf3271-1ef6-4e94-8210-03c2317947f6"
title: "Cred Dump Tools Dropped Files"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_cred_dump_tools_dropped_files.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_cred_dump_tools_dropped_files.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "8fbf3271-1ef6-4e94-8210-03c2317947f6"
  - "Cred Dump Tools Dropped Files"
attack_technique_ids:
  - "T1003.001"
  - "T1003.002"
  - "T1003.003"
  - "T1003.004"
  - "T1003.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Cred Dump Tools Dropped Files

Files with well-known filenames (parts of credential dump software or files produced by them) creation

## Metadata

- Rule ID: 8fbf3271-1ef6-4e94-8210-03c2317947f6
- Status: test
- Level: high
- Author: Teymur Kheirkhabarov, oscd.community
- Date: 2019-11-01
- Modified: 2025-10-25
- Source Path: rules/windows/file/file_event/file_event_win_cred_dump_tools_dropped_files.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]
- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.002]]
- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.003]]
- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.004]]
- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.005]]

## Detection

```yaml
selection:
- TargetFilename|contains:
  - \fgdump-log
  - \kirbi
  - \pwdump
  - \pwhashes
  - \wce_ccache
  - \wce_krbtkts
- TargetFilename|endswith:
  - \cachedump.exe
  - \cachedump64.exe
  - \DumpExt.dll
  - \DumpSvc.exe
  - \Dumpy.exe
  - \fgexec.exe
  - \lsremora.dll
  - \lsremora64.dll
  - \NTDS.out
  - \procdump.exe
  - \procdump64.exe
  - \procdump64a.exe
  - \pstgdump.exe
  - \pwdump.exe
  - \SAM.out
  - \SECURITY.out
  - \servpw.exe
  - \servpw64.exe
  - \SYSTEM.out
  - \test.pwd
  - \wceaux.dll
condition: selection
```

## False Positives

- Legitimate Administrator using tool for password recovery

## References

- https://www.slideshare.net/heirhabarov/hunting-for-credentials-dumping-in-windows-environment

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_cred_dump_tools_dropped_files.yml)
