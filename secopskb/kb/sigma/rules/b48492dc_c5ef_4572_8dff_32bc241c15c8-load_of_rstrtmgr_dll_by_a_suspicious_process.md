---
sigma_id: "b48492dc-c5ef-4572-8dff-32bc241c15c8"
title: "Load Of RstrtMgr.DLL By A Suspicious Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_dll_rstrtmgr_suspicious_load.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_dll_rstrtmgr_suspicious_load.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "high"
logsource: "windows / image_load"
aliases:
  - "b48492dc-c5ef-4572-8dff-32bc241c15c8"
  - "Load Of RstrtMgr.DLL By A Suspicious Process"
attack_technique_ids:
  - "T1486"
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Load Of RstrtMgr.DLL By A Suspicious Process

Detects the load of RstrtMgr DLL (Restart Manager) by a suspicious process.
This library has been used during ransomware campaigns to kill processes that would prevent file encryption by locking them (e.g. Conti ransomware, Cactus ransomware). It has also recently been seen used by the BiBi wiper for Windows.
It could also be used for anti-analysis purposes by shut downing specific processes.

## Metadata

- Rule ID: b48492dc-c5ef-4572-8dff-32bc241c15c8
- Status: test
- Level: high
- Author: Luc Génaux
- Date: 2023-11-28
- Source Path: rules/windows/image_load/image_load_dll_rstrtmgr_suspicious_load.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1486-data_encrypted_for_impact|T1486]]
- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection_img:
- ImageLoaded|endswith: \RstrtMgr.dll
- OriginalFileName: RstrtMgr.dll
selection_folders_1:
  Image|contains:
  - :\Perflogs\
  - :\Users\Public\
  - \Temporary Internet
selection_folders_2:
- Image|contains|all:
  - :\Users\
  - \Favorites\
- Image|contains|all:
  - :\Users\
  - \Favourites\
- Image|contains|all:
  - :\Users\
  - \Contacts\
condition: selection_img and 1 of selection_folders_*
```

## False Positives

- Processes related to software installation

## References

- https://www.crowdstrike.com/blog/windows-restart-manager-part-1/
- https://www.crowdstrike.com/blog/windows-restart-manager-part-2/
- https://web.archive.org/web/20231221193106/https://www.swascan.com/cactus-ransomware-malware-analysis/
- https://taiwan.postsen.com/business/88601/Hamas-hackers-use-data-destruction-software-BiBi-which-consumes-a-lot-of-processor-resources-to-wipe-Windows-computer-data--iThome.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_dll_rstrtmgr_suspicious_load.yml)
