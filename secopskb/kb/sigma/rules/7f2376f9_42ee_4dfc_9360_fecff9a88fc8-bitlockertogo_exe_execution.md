---
sigma_id: "7f2376f9-42ee-4dfc-9360-fecff9a88fc8"
title: "BitLockerTogo.EXE Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_bitlockertogo_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_bitlockertogo_execution.yml"
build_date: "2026-04-26 14:14:21"
status: "test"
level: "low"
logsource: "windows / process_creation"
aliases:
  - "7f2376f9-42ee-4dfc-9360-fecff9a88fc8"
  - "BitLockerTogo.EXE Execution"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# BitLockerTogo.EXE Execution

Detects the execution of "BitLockerToGo.EXE".
BitLocker To Go is BitLocker Drive Encryption on removable data drives. This feature includes the encryption of, USB flash drives, SD cards, External hard disk drives, Other drives that are formatted by using the NTFS, FAT16, FAT32, or exFAT file system.
This is a rarely used application and usage of it at all is worth investigating.
Malware such as Lumma stealer has been seen using this process as a target for process hollowing.

## Metadata

- Rule ID: 7f2376f9-42ee-4dfc-9360-fecff9a88fc8
- Status: test
- Level: low
- Author: Josh Nickels, mttaggart
- Date: 2024-07-11
- Source Path: rules/windows/process_creation/proc_creation_win_bitlockertogo_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection:
  Image|endswith: \BitLockerToGo.exe
condition: selection
```

## False Positives

- Legitimate usage of BitLockerToGo.exe to encrypt portable devices.

## References

- https://tria.ge/240521-ynezpagf56/behavioral1
- https://any.run/report/6eea2773c1b4b5c6fb7c142933e220c96f9a4ec89055bf0cf54accdcde7df535/a407f006-ee45-420d-b576-f259094df091
- https://bazaar.abuse.ch/sample/8c75f8e94486f5bbf461505823f5779f328c5b37f1387c18791e0c21f3fdd576/
- https://bazaar.abuse.ch/sample/64e6605496919cd76554915cbed88e56fdec10dec6523918a631754664b8c8d3/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_bitlockertogo_execution.yml)
