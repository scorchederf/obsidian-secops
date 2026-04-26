---
sigma_id: "418a3163-3247-4b7b-9933-dcfcb7c52ea9"
title: "Compressed File Creation Via Tar.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_tar_compression.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_tar_compression.yml"
build_date: "2026-04-26 14:14:22"
status: "test"
level: "low"
logsource: "windows / process_creation"
aliases:
  - "418a3163-3247-4b7b-9933-dcfcb7c52ea9"
  - "Compressed File Creation Via Tar.EXE"
attack_technique_ids:
  - "T1560"
  - "T1560.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Compressed File Creation Via Tar.EXE

Detects execution of "tar.exe" in order to create a compressed file.
Adversaries may abuse various utilities to compress or encrypt data before exfiltration.

## Metadata

- Rule ID: 418a3163-3247-4b7b-9933-dcfcb7c52ea9
- Status: test
- Level: low
- Author: Nasreddine Bencherchali (Nextron Systems), AdmU3
- Date: 2023-12-19
- Source Path: rules/windows/process_creation/proc_creation_win_tar_compression.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1560-archive_collected_data|T1560]]
- [[kb/attack/techniques/T1560-archive_collected_data|T1560.001]]

## Detection

```yaml
selection_img:
- Image|endswith: \tar.exe
- OriginalFileName: bsdtar
selection_create:
  CommandLine|contains:
  - -c
  - -r
  - -u
condition: all of selection_*
```

## False Positives

- Likely

## References

- https://unit42.paloaltonetworks.com/chromeloader-malware/
- https://lolbas-project.github.io/lolbas/Binaries/Tar/
- https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/cicada-apt10-japan-espionage

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_tar_compression.yml)
