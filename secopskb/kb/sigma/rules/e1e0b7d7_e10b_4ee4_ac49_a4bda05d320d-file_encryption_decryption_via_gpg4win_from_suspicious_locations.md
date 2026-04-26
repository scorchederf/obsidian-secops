---
sigma_id: "e1e0b7d7-e10b-4ee4-ac49-a4bda05d320d"
title: "File Encryption/Decryption Via Gpg4win From Suspicious Locations"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_gpg4win_susp_location.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_gpg4win_susp_location.yml"
build_date: "2026-04-26 15:01:44"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "e1e0b7d7-e10b-4ee4-ac49-a4bda05d320d"
  - "File Encryption/Decryption Via Gpg4win From Suspicious Locations"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# File Encryption/Decryption Via Gpg4win From Suspicious Locations

Detects usage of Gpg4win to encrypt/decrypt files located in potentially suspicious locations.

## Metadata

- Rule ID: e1e0b7d7-e10b-4ee4-ac49-a4bda05d320d
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems), X__Junior (Nextron Systems)
- Date: 2022-11-30
- Modified: 2023-08-09
- Source Path: rules/windows/process_creation/proc_creation_win_gpg4win_susp_location.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_metadata:
- Image|endswith:
  - \gpg.exe
  - \gpg2.exe
- Product: GNU Privacy Guard (GnuPG)
- Description: GnuPG’s OpenPGP tool
selection_cli:
  CommandLine|contains: -passphrase
selection_paths:
  CommandLine|contains:
  - :\PerfLogs\
  - :\Temp\
  - :\Users\Public\
  - :\Windows\Temp\
  - \AppData\Local\Temp\
  - \AppData\Roaming\
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://blogs.vmware.com/security/2022/11/batloader-the-evasive-downloader-malware.html
- https://news.sophos.com/en-us/2022/01/19/zloader-installs-remote-access-backdoors-and-delivers-cobalt-strike/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_gpg4win_susp_location.yml)
