---
sigma_id: "9e099d99-44c2-42b6-a6d8-54c3545cab29"
title: "HackTool - Mimikatz Kirbi File Creation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_hktl_mimikatz_files.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_hktl_mimikatz_files.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "critical"
logsource: "windows / file_event"
aliases:
  - "9e099d99-44c2-42b6-a6d8-54c3545cab29"
  - "HackTool - Mimikatz Kirbi File Creation"
attack_technique_ids:
  - "T1558"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# HackTool - Mimikatz Kirbi File Creation

Detects the creation of files created by mimikatz such as ".kirbi", "mimilsa.log", etc.

## Metadata

- Rule ID: 9e099d99-44c2-42b6-a6d8-54c3545cab29
- Status: test
- Level: critical
- Author: Florian Roth (Nextron Systems), David ANDRE
- Date: 2021-11-08
- Modified: 2024-06-27
- Source Path: rules/windows/file/file_event/file_event_win_hktl_mimikatz_files.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1558-steal_or_forge_kerberos_tickets|T1558]]

## Detection

```yaml
selection:
  TargetFilename|endswith:
  - .kirbi
  - mimilsa.log
condition: selection
```

## False Positives

- Unlikely

## References

- https://cobalt.io/blog/kerberoast-attack-techniques
- https://pentestlab.blog/2019/10/21/persistence-security-support-provider/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_hktl_mimikatz_files.yml)
