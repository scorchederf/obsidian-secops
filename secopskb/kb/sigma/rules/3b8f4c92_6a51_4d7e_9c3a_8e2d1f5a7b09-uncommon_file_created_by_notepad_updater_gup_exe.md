---
sigma_id: "3b8f4c92-6a51-4d7e-9c3a-8e2d1f5a7b09"
title: "Uncommon File Created by Notepad++ Updater Gup.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_gup_uncommon_file_creation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_gup_uncommon_file_creation.yml"
build_date: "2026-04-26 17:03:23"
status: "experimental"
level: "high"
logsource: "windows / file_event"
aliases:
  - "3b8f4c92-6a51-4d7e-9c3a-8e2d1f5a7b09"
  - "Uncommon File Created by Notepad++ Updater Gup.EXE"
attack_technique_ids:
  - "T1195.002"
  - "T1557"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Uncommon File Created by Notepad++ Updater Gup.EXE

Detects when the Notepad++ updater (gup.exe) creates files in suspicious or uncommon locations.
This could indicate potential exploitation of the updater component to deliver unwanted malware or unwarranted files.

## Metadata

- Rule ID: 3b8f4c92-6a51-4d7e-9c3a-8e2d1f5a7b09
- Status: experimental
- Level: high
- Author: Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2026-02-03
- Modified: 2026-03-16
- Source Path: rules/windows/file/file_event/file_event_win_gup_uncommon_file_creation.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1195-supply_chain_compromise|T1195.002]]
- [[kb/attack/techniques/T1557-adversary-in-the-middle|T1557]]

## Detection

```yaml
selection:
  Image|endswith: \gup.exe
filter_main_legit_paths:
  TargetFilename|startswith:
  - C:\Program Files\Notepad++\
  - C:\Program Files (x86)\Notepad++\
filter_main_temp_update_installer:
  TargetFilename|startswith: C:\Users\
  TargetFilename|contains|all:
  - \AppData\Local\Temp\
  - npp.
  - .Installer.
  - .exe
filter_main_temp_generic_zip:
  TargetFilename|startswith: C:\Users\
  TargetFilename|contains|all:
  - \AppData\Local\Temp\
  - .zip
filter_main_recycle_bin:
  TargetFilename|startswith: C:\$Recycle.Bin\S-1-5-21
filter_main_plugins:
- TargetFilename|contains:
  - \plugins\JsonTools\testfiles\
  - \Notepad++\plugins\ComparePlugin\
- TargetFilename|contains|all:
  - npp.
  - .portable.
  - \plugins\
condition: selection and not 1 of filter_main_*
```

## False Positives

- Custom or portable Notepad++ installations in non-standard directories.
- Legitimate update processes creating temporary files in unexpected locations.

## References

- https://notepad-plus-plus.org/news/v889-released/
- https://www.heise.de/en/news/Notepad-updater-installed-malware-11109726.html
- https://www.rapid7.com/blog/post/tr-chrysalis-backdoor-dive-into-lotus-blossoms-toolkit/
- https://www.validin.com/blog/exploring_notepad_plus_plus_network_indicators/
- https://securelist.com/notepad-supply-chain-attack/118708/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_gup_uncommon_file_creation.yml)
