---
sigma_id: "e0565f5d-d420-4e02-8a68-ac00d864f9cf"
title: "Automated Collection Bookmarks Using Get-ChildItem PowerShell"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_get_childitem_bookmarks.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_get_childitem_bookmarks.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "low"
logsource: "windows / ps_script"
aliases:
  - "e0565f5d-d420-4e02-8a68-ac00d864f9cf"
  - "Automated Collection Bookmarks Using Get-ChildItem PowerShell"
attack_technique_ids:
  - "T1217"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Automated Collection Bookmarks Using Get-ChildItem PowerShell

Adversaries may enumerate browser bookmarks to learn more about compromised hosts.
Browser bookmarks may reveal personal information about users (ex: banking sites, interests, social media, etc.) as well as details about
internal network resources such as servers, tools/dashboards, or other related infrastructure.

## Metadata

- Rule ID: e0565f5d-d420-4e02-8a68-ac00d864f9cf
- Status: test
- Level: low
- Author: frack113
- Date: 2021-12-13
- Modified: 2022-12-25
- Source Path: rules/windows/powershell/powershell_script/posh_ps_get_childitem_bookmarks.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1217-browser_information_discovery|T1217]]

## Detection

```yaml
selection:
  ScriptBlockText|contains|all:
  - Get-ChildItem
  - ' -Recurse '
  - ' -Path '
  - ' -Filter Bookmarks'
  - ' -ErrorAction SilentlyContinue'
  - ' -Force'
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1217/T1217.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_get_childitem_bookmarks.yml)
