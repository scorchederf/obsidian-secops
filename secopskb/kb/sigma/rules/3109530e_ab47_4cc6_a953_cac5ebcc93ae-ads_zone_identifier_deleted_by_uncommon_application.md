---
sigma_id: "3109530e-ab47-4cc6-a953-cac5ebcc93ae"
title: "ADS Zone.Identifier Deleted By Uncommon Application"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_delete/file_delete_win_zone_identifier_ads_uncommon.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_delete/file_delete_win_zone_identifier_ads_uncommon.yml"
build_date: "2026-04-26 14:14:19"
status: "test"
level: "medium"
logsource: "windows / file_delete"
aliases:
  - "3109530e-ab47-4cc6-a953-cac5ebcc93ae"
  - "ADS Zone.Identifier Deleted By Uncommon Application"
attack_technique_ids:
  - "T1070.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# ADS Zone.Identifier Deleted By Uncommon Application

Detects the deletion of the "Zone.Identifier" ADS by an uncommon process. Attackers can leverage this in order to bypass security restrictions that make use of the ADS such as Microsoft Office apps.

## Metadata

- Rule ID: 3109530e-ab47-4cc6-a953-cac5ebcc93ae
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-09-04
- Modified: 2025-07-04
- Source Path: rules/windows/file/file_delete/file_delete_win_zone_identifier_ads_uncommon.yml

## Logsource

- category: file_delete
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal|T1070.004]]

## Detection

```yaml
selection:
  TargetFilename|endswith: :Zone.Identifier
filter_main_generic:
  Image:
  - C:\Program Files\PowerShell\7-preview\pwsh.exe
  - C:\Program Files\PowerShell\7\pwsh.exe
  - C:\Windows\explorer.exe
  - C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
  - C:\Windows\SysWOW64\explorer.exe
  - C:\Windows\SysWOW64\WindowsPowerShell\v1.0\powershell.exe
filter_optional_browsers_chrome:
  Image:
  - C:\Program Files (x86)\Google\Chrome\Application\chrome.exe
  - C:\Program Files\Google\Chrome\Application\chrome.exe
filter_optional_browsers_firefox:
  Image:
  - C:\Program Files (x86)\Mozilla Firefox\firefox.exe
  - C:\Program Files\Mozilla Firefox\firefox.exe
filter_optional_browsers_msedge:
  Image:
  - C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe
  - C:\Program Files\Microsoft\Edge\Application\msedge.exe
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Other third party applications not listed.

## References

- https://securityliterate.com/how-malware-abuses-the-zone-identifier-to-circumvent-detection-and-analysis/
- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_delete/file_delete_win_zone_identifier_ads_uncommon.yml)
