---
sigma_id: "174afcfa-6e40-4ae9-af64-496546389294"
title: "Credential Dumping Attempt Via Svchost"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_access/proc_access_win_svchost_credential_dumping.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_access/proc_access_win_svchost_credential_dumping.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "high"
logsource: "windows / process_access"
aliases:
  - "174afcfa-6e40-4ae9-af64-496546389294"
  - "Credential Dumping Attempt Via Svchost"
attack_technique_ids:
  - "T1548"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects when a process tries to access the memory of svchost to potentially dump credentials.

## Logsource

- category: process_access
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548: Abuse Elevation Control Mechanism]]

## Detection

```yaml
selection:
  TargetImage|endswith: \svchost.exe
  GrantedAccess: '0x143a'
filter_main_known_processes:
  SourceImage|endswith:
  - \services.exe
  - \msiexec.exe
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_access/proc_access_win_svchost_credential_dumping.yml)
