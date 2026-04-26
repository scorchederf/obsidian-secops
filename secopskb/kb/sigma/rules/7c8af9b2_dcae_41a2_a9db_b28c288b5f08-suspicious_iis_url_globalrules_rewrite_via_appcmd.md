---
sigma_id: "7c8af9b2-dcae-41a2-a9db-b28c288b5f08"
title: "Suspicious IIS URL GlobalRules Rewrite Via AppCmd"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_iis_appcmd_susp_rewrite_rule.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_iis_appcmd_susp_rewrite_rule.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "7c8af9b2-dcae-41a2-a9db-b28c288b5f08"
  - "Suspicious IIS URL GlobalRules Rewrite Via AppCmd"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious IIS URL GlobalRules Rewrite Via AppCmd

Detects usage of "appcmd" to create new global URL rewrite rules. This behaviour has been observed being used by threat actors to add new rules so they can access their webshells.

## Metadata

- Rule ID: 7c8af9b2-dcae-41a2-a9db-b28c288b5f08
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-01-22
- Source Path: rules/windows/process_creation/proc_creation_win_iis_appcmd_susp_rewrite_rule.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_img:
- Image|endswith: \appcmd.exe
- OriginalFileName: appcmd.exe
selection_cli:
  CommandLine|contains|all:
  - set
  - config
  - section:system.webServer/rewrite/globalRules
  - 'commit:'
condition: all of selection_*
```

## False Positives

- Legitimate usage of appcmd to add new URL rewrite rules

## References

- https://twitter.com/malmoeb/status/1616702107242971144
- https://learn.microsoft.com/en-us/answers/questions/739120/how-to-add-re-write-global-rule-with-action-type-r

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_iis_appcmd_susp_rewrite_rule.yml)
