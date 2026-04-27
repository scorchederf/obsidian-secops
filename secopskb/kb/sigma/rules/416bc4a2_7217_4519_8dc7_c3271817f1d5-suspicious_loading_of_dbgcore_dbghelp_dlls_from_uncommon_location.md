---
sigma_id: "416bc4a2-7217-4519-8dc7-c3271817f1d5"
title: "Suspicious Loading of Dbgcore/Dbghelp DLLs from Uncommon Location"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_win_susp_dbgcore_dbghelp_load.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_win_susp_dbgcore_dbghelp_load.yml"
build_date: "2026-04-26 17:03:23"
status: "experimental"
level: "high"
logsource: "windows / image_load"
aliases:
  - "416bc4a2-7217-4519-8dc7-c3271817f1d5"
  - "Suspicious Loading of Dbgcore/Dbghelp DLLs from Uncommon Location"
attack_technique_ids:
  - "T1003"
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Suspicious Loading of Dbgcore/Dbghelp DLLs from Uncommon Location

Detects loading of dbgcore.dll or dbghelp.dll from uncommon locations such as user directories.
These DLLs contain the MiniDumpWriteDump function, which can be abused for credential dumping purposes or in some cases for evading EDR/AV detection by suspending processes.

## Metadata

- Rule ID: 416bc4a2-7217-4519-8dc7-c3271817f1d5
- Status: experimental
- Level: high
- Author: Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2025-11-27
- Modified: 2026-01-09
- Source Path: rules/windows/image_load/image_load_win_susp_dbgcore_dbghelp_load.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003]]
- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection_img:
  Image|contains:
  - :\Perflogs\
  - :\Temp\
  - :\Users\Public\
  - \$Recycle.Bin\
  - \Contacts\
  - \Documents\
  - \Favorites\
  - \Favourites\
  - \inetpub\wwwroot\
  - \Music\
  - \Pictures\
  - \Start Menu\Programs\Startup\
  - \Users\Default\
  - \Videos\
selection_dll:
  ImageLoaded|endswith:
  - \dbgcore.dll
  - \dbghelp.dll
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://blog.axelarator.net/hunting-for-edr-freeze/
- https://www.zerosalarium.com/2025/09/EDR-Freeze-Puts-EDRs-Antivirus-Into-Coma.html
- https://www.splunk.com/en_us/blog/security/you-bet-your-lsass-hunting-lsass-access.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_win_susp_dbgcore_dbghelp_load.yml)
