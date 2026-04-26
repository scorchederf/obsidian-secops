---
sigma_id: "72a0369a-2576-4aaf-bfc9-6bb24a574ac6"
title: "Delete Defender Scan ShellEx Context Menu Registry Key"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_delete/registry_delete_defender_context_menu.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_delete/registry_delete_defender_context_menu.yml"
build_date: "2026-04-26 14:14:23"
status: "experimental"
level: "medium"
logsource: "windows / registry_delete"
aliases:
  - "72a0369a-2576-4aaf-bfc9-6bb24a574ac6"
  - "Delete Defender Scan ShellEx Context Menu Registry Key"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Delete Defender Scan ShellEx Context Menu Registry Key

Detects deletion of registry key that adds 'Scan with Defender' option in context menu. Attackers may use this to make it harder for users to scan files that are suspicious.

## Metadata

- Rule ID: 72a0369a-2576-4aaf-bfc9-6bb24a574ac6
- Status: experimental
- Level: medium
- Author: Matt Anderson (Huntress)
- Date: 2025-07-11
- Modified: 2025-10-07
- Source Path: rules/windows/registry/registry_delete/registry_delete_defender_context_menu.yml

## Logsource

- category: registry_delete
- product: windows

## Detection

```yaml
selection:
  TargetObject|contains: shellex\ContextMenuHandlers\EPP
filter_main_defender:
  Image|startswith:
  - C:\ProgramData\Microsoft\Windows Defender\Platform\
  - C:\Program Files\Windows Defender\
  - C:\Program Files (x86)\Windows Defender\
  Image|endswith: \MsMpEng.exe
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unlikely as this weakens defenses and normally would not be done even if using another AV.

## References

- https://research.splunk.com/endpoint/395ed5fe-ad13-4366-9405-a228427bdd91/
- https://winaero.com/how-to-delete-scan-with-windows-defender-from-context-menu-in-windows-10/
- https://thedfirreport.com/2021/10/18/icedid-to-xinglocker-ransomware-in-24-hours/
- https://blog.malwarebytes.com/malwarebytes-news/2021/02/lazyscripter-from-empire-to-double-rat/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_delete/registry_delete_defender_context_menu.yml)
