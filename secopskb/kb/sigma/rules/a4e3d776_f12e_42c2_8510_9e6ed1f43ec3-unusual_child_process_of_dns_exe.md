---
sigma_id: "a4e3d776-f12e-42c2-8510-9e6ed1f43ec3"
title: "Unusual Child Process of dns.exe"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_dns_susp_child_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_dns_susp_child_process.yml"
build_date: "2026-04-26 15:01:53"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "a4e3d776-f12e-42c2-8510-9e6ed1f43ec3"
  - "Unusual Child Process of dns.exe"
attack_technique_ids:
  - "T1133"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Unusual Child Process of dns.exe

Detects an unexpected process spawning from dns.exe which may indicate activity related to remote code execution or other forms of exploitation as seen in CVE-2020-1350 (SigRed)

## Metadata

- Rule ID: a4e3d776-f12e-42c2-8510-9e6ed1f43ec3
- Status: test
- Level: high
- Author: Tim Rauch, Elastic (idea)
- Date: 2022-09-27
- Modified: 2023-02-05
- Source Path: rules/windows/process_creation/proc_creation_win_dns_susp_child_process.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1133-external_remote_services|T1133]]

## Detection

```yaml
selection:
  ParentImage|endswith: \dns.exe
filter:
  Image|endswith: \conhost.exe
condition: selection and not filter
```

## False Positives

- Unknown

## References

- https://www.elastic.co/guide/en/security/current/unusual-child-process-of-dns-exe.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_dns_susp_child_process.yml)
