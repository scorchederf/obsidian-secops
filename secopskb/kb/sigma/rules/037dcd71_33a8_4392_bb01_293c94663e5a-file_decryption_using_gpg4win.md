---
sigma_id: "037dcd71-33a8-4392-bb01-293c94663e5a"
title: "File Decryption Using Gpg4win"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_gpg4win_decryption.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_gpg4win_decryption.yml"
build_date: "2026-04-26 14:14:25"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "037dcd71-33a8-4392-bb01-293c94663e5a"
  - "File Decryption Using Gpg4win"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# File Decryption Using Gpg4win

Detects usage of Gpg4win to decrypt files

## Metadata

- Rule ID: 037dcd71-33a8-4392-bb01-293c94663e5a
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-08-09
- Source Path: rules/windows/process_creation/proc_creation_win_gpg4win_decryption.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_metadata:
- Image|endswith:
  - \gpg.exe
  - \gpg2.exe
- Description: GnuPG’s OpenPGP tool
selection_cli:
  CommandLine|contains|all:
  - ' -d '
  - passphrase
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://blogs.vmware.com/security/2022/11/batloader-the-evasive-downloader-malware.html
- https://www.gpg4win.de/documentation.html
- https://news.sophos.com/en-us/2022/01/19/zloader-installs-remote-access-backdoors-and-delivers-cobalt-strike/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_gpg4win_decryption.yml)
