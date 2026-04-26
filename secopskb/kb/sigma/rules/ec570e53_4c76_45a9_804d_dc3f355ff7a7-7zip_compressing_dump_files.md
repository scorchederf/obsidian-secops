---
sigma_id: "ec570e53-4c76-45a9-804d-dc3f355ff7a7"
title: "7Zip Compressing Dump Files"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_7zip_exfil_dmp_files.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_7zip_exfil_dmp_files.yml"
build_date: "2026-04-26 14:14:19"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "ec570e53-4c76-45a9-804d-dc3f355ff7a7"
  - "7Zip Compressing Dump Files"
attack_technique_ids:
  - "T1560.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# 7Zip Compressing Dump Files

Detects execution of 7z in order to compress a file with a ".dmp"/".dump" extension, which could be a step in a process of dump file exfiltration.

## Metadata

- Rule ID: ec570e53-4c76-45a9-804d-dc3f355ff7a7
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-09-27
- Modified: 2023-09-12
- Source Path: rules/windows/process_creation/proc_creation_win_7zip_exfil_dmp_files.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1560-archive_collected_data|T1560.001]]

## Detection

```yaml
selection_img:
- Description|contains: 7-Zip
- Image|endswith:
  - \7z.exe
  - \7zr.exe
  - \7za.exe
- OriginalFileName:
  - 7z.exe
  - 7za.exe
selection_extension:
  CommandLine|contains:
  - .dmp
  - .dump
  - .hdmp
condition: all of selection_*
```

## False Positives

- Legitimate use of 7z with a command line in which ".dmp" or ".dump" appears accidentally
- Legitimate use of 7z to compress WER ".dmp" files for troubleshooting

## References

- https://thedfirreport.com/2022/09/26/bumblebee-round-two/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_7zip_exfil_dmp_files.yml)
