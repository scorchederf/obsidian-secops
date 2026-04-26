---
sigma_id: "571498c8-908e-40b4-910b-d2369159a3da"
title: "Password Protected ZIP File Opened (Email Attachment)"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_susp_opened_encrypted_zip_outlook.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_susp_opened_encrypted_zip_outlook.yml"
build_date: "2026-04-26 15:01:47"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "571498c8-908e-40b4-910b-d2369159a3da"
  - "Password Protected ZIP File Opened (Email Attachment)"
attack_technique_ids:
  - "T1027"
  - "T1566.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Password Protected ZIP File Opened (Email Attachment)

Detects the extraction of password protected ZIP archives. See the filename variable for more details on which file has been opened.

## Metadata

- Rule ID: 571498c8-908e-40b4-910b-d2369159a3da
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-05-09
- Source Path: rules/windows/builtin/security/win_security_susp_opened_encrypted_zip_outlook.yml

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027]]
- [[kb/attack/techniques/T1566-phishing|T1566.001]]

## Detection

```yaml
selection:
  EventID: 5379
  TargetName|contains|all:
  - Microsoft_Windows_Shell_ZipFolder:filename
  - \Temporary Internet Files\Content.Outlook
condition: selection
```

## False Positives

- Legitimate used of encrypted ZIP files

## References

- https://twitter.com/sbousseaden/status/1523383197513379841

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_susp_opened_encrypted_zip_outlook.yml)
