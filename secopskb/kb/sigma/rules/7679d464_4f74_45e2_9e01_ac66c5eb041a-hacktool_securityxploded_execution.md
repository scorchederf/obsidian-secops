---
sigma_id: "7679d464-4f74-45e2-9e01-ac66c5eb041a"
title: "HackTool - SecurityXploded Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_secutyxploded.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_secutyxploded.yml"
build_date: "2026-04-26 15:01:45"
status: "stable"
level: "critical"
logsource: "windows / process_creation"
aliases:
  - "7679d464-4f74-45e2-9e01-ac66c5eb041a"
  - "HackTool - SecurityXploded Execution"
attack_technique_ids:
  - "T1555"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# HackTool - SecurityXploded Execution

Detects the execution of SecurityXploded Tools

## Metadata

- Rule ID: 7679d464-4f74-45e2-9e01-ac66c5eb041a
- Status: stable
- Level: critical
- Author: Florian Roth (Nextron Systems)
- Date: 2018-12-19
- Modified: 2023-02-04
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_secutyxploded.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1555-credentials_from_password_stores|T1555]]

## Detection

```yaml
selection:
- Company: SecurityXploded
- Image|endswith: PasswordDump.exe
- OriginalFileName|endswith: PasswordDump.exe
condition: selection
```

## False Positives

- Unlikely

## References

- https://securityxploded.com/
- https://web.archive.org/web/20200601000524/https://cyberx-labs.com/blog/gangnam-industrial-style-apt-campaign-targets-korean-industrial-companies/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_secutyxploded.yml)
