---
sigma_id: "54f0434b-726f-48a1-b2aa-067df14516e4"
title: "Password Protected ZIP File Opened (Suspicious Filenames)"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_susp_opened_encrypted_zip_filename.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_susp_opened_encrypted_zip_filename.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "54f0434b-726f-48a1-b2aa-067df14516e4"
  - "Password Protected ZIP File Opened (Suspicious Filenames)"
attack_technique_ids:
  - "T1027"
  - "T1105"
  - "T1036"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Password Protected ZIP File Opened (Suspicious Filenames)

Detects the extraction of password protected ZIP archives with suspicious file names. See the filename variable for more details on which file has been opened.

## Metadata

- Rule ID: 54f0434b-726f-48a1-b2aa-067df14516e4
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-05-09
- Source Path: rules/windows/builtin/security/win_security_susp_opened_encrypted_zip_filename.yml

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027]]
- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]
- [[kb/attack/techniques/T1036-masquerading|T1036]]

## Detection

```yaml
selection:
  EventID: 5379
  TargetName|contains: Microsoft_Windows_Shell_ZipFolder:filename
selection_filename:
  TargetName|contains:
  - invoice
  - new order
  - rechnung
  - factura
  - delivery
  - purchase
  - order
  - payment
condition: selection and selection_filename
```

## False Positives

- Legitimate used of encrypted ZIP files

## References

- https://twitter.com/sbousseaden/status/1523383197513379841

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_susp_opened_encrypted_zip_filename.yml)
