---
sigma_id: "00ba9da1-b510-4f6b-b258-8d338836180f"
title: "Password Protected ZIP File Opened"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_susp_opened_encrypted_zip.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_susp_opened_encrypted_zip.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "windows / security"
aliases:
  - "00ba9da1-b510-4f6b-b258-8d338836180f"
  - "Password Protected ZIP File Opened"
attack_technique_ids:
  - "T1027"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Password Protected ZIP File Opened

Detects the extraction of password protected ZIP archives. See the filename variable for more details on which file has been opened.

## Metadata

- Rule ID: 00ba9da1-b510-4f6b-b258-8d338836180f
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2022-05-09
- Source Path: rules/windows/builtin/security/win_security_susp_opened_encrypted_zip.yml

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027]]

## Detection

```yaml
selection:
  EventID: 5379
  TargetName|contains: Microsoft_Windows_Shell_ZipFolder:filename
filter:
  TargetName|contains: \Temporary Internet Files\Content.Outlook
condition: selection and not filter
```

## False Positives

- Legitimate used of encrypted ZIP files

## References

- https://twitter.com/sbousseaden/status/1523383197513379841

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_susp_opened_encrypted_zip.yml)
