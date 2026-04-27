---
sigma_id: "9f383dc0-fdeb-4d56-acbc-9f9f4f8f20f3"
title: "Unusual File Modification by dns.exe"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_change/file_change_win_unusual_modification_by_dns_exe.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_change/file_change_win_unusual_modification_by_dns_exe.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / file_change"
aliases:
  - "9f383dc0-fdeb-4d56-acbc-9f9f4f8f20f3"
  - "Unusual File Modification by dns.exe"
attack_technique_ids:
  - "T1133"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Unusual File Modification by dns.exe

Detects an unexpected file being modified by dns.exe which my indicate activity related to remote code execution or other forms of exploitation as seen in CVE-2020-1350 (SigRed)

## Metadata

- Rule ID: 9f383dc0-fdeb-4d56-acbc-9f9f4f8f20f3
- Status: test
- Level: high
- Author: Tim Rauch (Nextron Systems), Elastic (idea)
- Date: 2022-09-27
- Source Path: rules/windows/file/file_change/file_change_win_unusual_modification_by_dns_exe.yml

## Logsource

- category: file_change
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1133-external_remote_services|T1133]]

## Detection

```yaml
selection:
  Image|endswith: \dns.exe
filter:
  TargetFilename|endswith: \dns.log
condition: selection and not filter
```

## False Positives

- Unknown

## References

- https://www.elastic.co/guide/en/security/current/unusual-file-modification-by-dns-exe.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_change/file_change_win_unusual_modification_by_dns_exe.yml)
