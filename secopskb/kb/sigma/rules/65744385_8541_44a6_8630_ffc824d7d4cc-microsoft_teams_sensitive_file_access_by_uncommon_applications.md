---
sigma_id: "65744385-8541-44a6-8630-ffc824d7d4cc"
title: "Microsoft Teams Sensitive File Access By Uncommon Applications"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_access/file_access_win_teams_sensitive_files.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_access/file_access_win_teams_sensitive_files.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "medium"
logsource: "windows / file_access"
aliases:
  - "65744385-8541-44a6-8630-ffc824d7d4cc"
  - "Microsoft Teams Sensitive File Access By Uncommon Applications"
attack_technique_ids:
  - "T1528"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Microsoft Teams Sensitive File Access By Uncommon Applications

Detects file access attempts to sensitive Microsoft teams files (leveldb, cookies) by an uncommon process.

## Metadata

- Rule ID: 65744385-8541-44a6-8630-ffc824d7d4cc
- Status: test
- Level: medium
- Author: @SerkinValery
- Date: 2024-07-22
- Source Path: rules/windows/file/file_access/file_access_win_teams_sensitive_files.yml

## Logsource

- category: file_access
- definition: Requirements: Microsoft-Windows-Kernel-File ETW provider
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1528-steal_application_access_token|T1528]]

## Detection

```yaml
selection:
  FileName|contains:
  - \Microsoft\Teams\Cookies
  - \Microsoft\Teams\Local Storage\leveldb
filter_main_legit_location:
  Image|endswith: \Microsoft\Teams\current\Teams.exe
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://www.bleepingcomputer.com/news/security/microsoft-teams-stores-auth-tokens-as-cleartext-in-windows-linux-macs/
- https://www.vectra.ai/blog/undermining-microsoft-teams-security-by-mining-tokens

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_access/file_access_win_teams_sensitive_files.yml)
