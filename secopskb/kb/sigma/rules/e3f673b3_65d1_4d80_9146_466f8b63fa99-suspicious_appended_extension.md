---
sigma_id: "e3f673b3-65d1-4d80-9146-466f8b63fa99"
title: "Suspicious Appended Extension"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_rename/file_rename_win_ransomware.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_rename/file_rename_win_ransomware.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "windows / file_rename"
aliases:
  - "e3f673b3-65d1-4d80-9146-466f8b63fa99"
  - "Suspicious Appended Extension"
attack_technique_ids:
  - "T1486"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Appended Extension

Detects file renames where the target filename uses an uncommon double extension. Could indicate potential ransomware activity renaming files and adding a custom extension to the encrypted files, such as ".jpg.crypted", ".docx.locky", etc.

## Metadata

- Rule ID: e3f673b3-65d1-4d80-9146-466f8b63fa99
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-07-16
- Modified: 2023-11-11
- Source Path: rules/windows/file/file_rename/file_rename_win_ransomware.yml

## Logsource

- category: file_rename
- definition: Requirements: Microsoft-Windows-Kernel-File Provider with at least the KERNEL_FILE_KEYWORD_RENAME_SETLINK_PATH keyword
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1486-data_encrypted_for_impact|T1486]]

## Detection

```yaml
selection:
  SourceFilename|endswith:
  - .doc
  - .docx
  - .jpeg
  - .jpg
  - .lnk
  - .pdf
  - .png
  - .pst
  - .rtf
  - .xls
  - .xlsx
  TargetFilename|contains:
  - .doc.
  - .docx.
  - .jpeg.
  - .jpg.
  - .lnk.
  - .pdf.
  - .png.
  - .pst.
  - .rtf.
  - .xls.
  - .xlsx.
filter_main_generic:
  TargetFilename|endswith:
  - .backup
  - .bak
  - .old
  - .orig
  - .temp
  - .tmp
filter_optional_anaconda:
  TargetFilename|contains: :\ProgramData\Anaconda3\
  TargetFilename|endswith: .c~
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Backup software

## References

- https://app.any.run/tasks/d66ead5a-faf4-4437-93aa-65785afaf9e5/
- https://blog.cyble.com/2022/08/10/onyx-ransomware-renames-its-leak-site-to-vsop/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_rename/file_rename_win_ransomware.yml)
