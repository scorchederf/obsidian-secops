---
sigma_id: "3669afd2-9891-4534-a626-e5cf03810a61"
title: "Load Of RstrtMgr.DLL By An Uncommon Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_dll_rstrtmgr_uncommon_load.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_dll_rstrtmgr_uncommon_load.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "low"
logsource: "windows / image_load"
aliases:
  - "3669afd2-9891-4534-a626-e5cf03810a61"
  - "Load Of RstrtMgr.DLL By An Uncommon Process"
attack_technique_ids:
  - "T1486"
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Load Of RstrtMgr.DLL By An Uncommon Process

Detects the load of RstrtMgr DLL (Restart Manager) by an uncommon process.
This library has been used during ransomware campaigns to kill processes that would prevent file encryption by locking them (e.g. Conti ransomware, Cactus ransomware). It has also recently been seen used by the BiBi wiper for Windows.
It could also be used for anti-analysis purposes by shut downing specific processes.

## Metadata

- Rule ID: 3669afd2-9891-4534-a626-e5cf03810a61
- Status: test
- Level: low
- Author: Luc Génaux
- Date: 2023-11-28
- Modified: 2025-12-08
- Source Path: rules/windows/image_load/image_load_dll_rstrtmgr_uncommon_load.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1486-data_encrypted_for_impact|T1486]]
- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection:
- ImageLoaded|endswith: \RstrtMgr.dll
- OriginalFileName: RstrtMgr.dll
filter_main_generic:
  Image|startswith:
  - C:\$WINDOWS.~BT\'
  - C:\$WinREAgent\'
  - C:\Program Files (x86)\'
  - C:\Program Files\'
  - C:\ProgramData\'
  - C:\Windows\explorer.exe'
  - C:\Windows\SoftwareDistribution\'
  - C:\Windows\SysNative\'
  - C:\Windows\System32\'
  - C:\Windows\SysWOW64\'
  - C:\Windows\WinSxS\'
  - C:\WUDownloadCache\'
filter_main_user_software_installations:
  Image|startswith: C:\Users\'
  Image|contains|all:
  - \AppData\Local\Temp\is-
  - .tmp\
  Image|endswith: .tmp
filter_main_admin_software_installations:
  Image|startswith: C:\Windows\Temp\'
filter_optional_onedrive:
  Image|startswith: C:\Users\
  Image|endswith: \AppData\Local\Microsoft\OneDrive\OneDriveStandaloneUpdater.exe
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Other legitimate Windows processes not currently listed
- Processes related to software installation

## References

- https://www.crowdstrike.com/blog/windows-restart-manager-part-1/
- https://www.crowdstrike.com/blog/windows-restart-manager-part-2/
- https://web.archive.org/web/20231221193106/https://www.swascan.com/cactus-ransomware-malware-analysis/
- https://taiwan.postsen.com/business/88601/Hamas-hackers-use-data-destruction-software-BiBi-which-consumes-a-lot-of-processor-resources-to-wipe-Windows-computer-data--iThome.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_dll_rstrtmgr_uncommon_load.yml)
