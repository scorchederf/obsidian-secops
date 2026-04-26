---
sigma_id: "9f5c1d59-33be-4e60-bcab-85d2f566effd"
title: "Suspicious Process Access to LSASS with Dbgcore/Dbghelp DLLs"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_access/proc_access_win_susp_dbgcore_dbghelp_load.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_access/proc_access_win_susp_dbgcore_dbghelp_load.yml"
build_date: "2026-04-26 15:01:52"
status: "experimental"
level: "high"
logsource: "windows / process_access"
aliases:
  - "9f5c1d59-33be-4e60-bcab-85d2f566effd"
  - "Suspicious Process Access to LSASS with Dbgcore/Dbghelp DLLs"
attack_technique_ids:
  - "T1003.001"
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious Process Access to LSASS with Dbgcore/Dbghelp DLLs

Detects suspicious process access to LSASS.exe from processes located in uncommon locations with dbgcore.dll or dbghelp.dll in the call trace.
These DLLs contain functions like MiniDumpWriteDump that can be abused for credential dumping purposes. While modern tools like Mimikatz have moved to using ntdll.dll,
dbgcore.dll and dbghelp.dll are still used by basic credential dumping utilities and legacy tools for LSASS memory access and process suspension techniques.

## Metadata

- Rule ID: 9f5c1d59-33be-4e60-bcab-85d2f566effd
- Status: experimental
- Level: high
- Author: Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2025-11-27
- Source Path: rules/windows/process_access/proc_access_win_susp_dbgcore_dbghelp_load.yml

## Logsource

- category: process_access
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]
- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection_lsass_calltrace:
  TargetImage|endswith: \lsass.exe
  CallTrace|contains:
  - dbgcore.dll
  - dbghelp.dll
selection_susp_location:
  SourceImage|contains:
  - :\Perflogs\
  - :\Temp\
  - :\Users\Public\
  - \$Recycle.Bin\
  - \AppData\Roaming\
  - \Contacts\
  - \Desktop\
  - \Documents\
  - \Downloads\
  - \Favorites\
  - \Favourites\
  - \inetpub\wwwroot\
  - \Music\
  - \Pictures\
  - \Start Menu\Programs\Startup\
  - \Users\Default\
  - \Videos\
  - \Windows\Temp\
condition: all of selection_*
```

## False Positives

- Possibly during software installation or update processes

## References

- https://www.splunk.com/en_us/blog/security/you-bet-your-lsass-hunting-lsass-access.html
- https://docs.microsoft.com/en-us/windows/win32/api/minidumpapiset/nf-minidumpwritedump

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_access/proc_access_win_susp_dbgcore_dbghelp_load.yml)
