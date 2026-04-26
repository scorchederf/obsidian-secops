---
sigma_id: "3ffd6f51-e6c1-47b7-94b4-c1e61d4117c5"
title: "Certificate Exported Via Certutil.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_certutil_export_pfx.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_certutil_export_pfx.yml"
build_date: "2026-04-26 14:14:21"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "3ffd6f51-e6c1-47b7-94b4-c1e61d4117c5"
  - "Certificate Exported Via Certutil.EXE"
attack_technique_ids:
  - "T1027"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Certificate Exported Via Certutil.EXE

Detects the execution of the certutil with the "exportPFX" flag which allows the utility to export certificates.

## Metadata

- Rule ID: 3ffd6f51-e6c1-47b7-94b4-c1e61d4117c5
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems), Jonhnathan Ribeiro, oscd.community, Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-02-15
- Modified: 2024-03-05
- Source Path: rules/windows/process_creation/proc_creation_win_certutil_export_pfx.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027]]

## Detection

```yaml
selection_img:
- Image|endswith: \certutil.exe
- OriginalFileName: CertUtil.exe
selection_cli:
  CommandLine|contains|windash: '-exportPFX '
condition: all of selection_*
```

## False Positives

- There legitimate reasons to export certificates. Investigate the activity to determine if it's benign

## References

- https://www.splunk.com/en_us/blog/security/a-golden-saml-journey-solarwinds-continued.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_certutil_export_pfx.yml)
