---
sigma_id: "ab9e3b40-0c85-4ba1-aede-455d226fd124"
title: "Suspicious Redirection to Local Admin Share"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_redirect_local_admin_share.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_redirect_local_admin_share.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "ab9e3b40-0c85-4ba1-aede-455d226fd124"
  - "Suspicious Redirection to Local Admin Share"
attack_technique_ids:
  - "T1048"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Redirection to Local Admin Share

Detects a suspicious output redirection to the local admins share, this technique is often found in malicious scripts or hacktool stagers

## Metadata

- Rule ID: ab9e3b40-0c85-4ba1-aede-455d226fd124
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-01-16
- Modified: 2023-12-28
- Source Path: rules/windows/process_creation/proc_creation_win_susp_redirect_local_admin_share.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1048-exfiltration_over_alternative_protocol|T1048]]

## Detection

```yaml
selection_redirect:
  CommandLine|contains: '>'
selection_share:
  CommandLine|contains:
  - \\\\127.0.0.1\\admin$\\
  - \\\\localhost\\admin$\\
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://www.microsoft.com/security/blog/2022/01/15/destructive-malware-targeting-ukrainian-organizations/
- http://blog.talosintelligence.com/2022/09/lazarus-three-rats.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_redirect_local_admin_share.yml)
