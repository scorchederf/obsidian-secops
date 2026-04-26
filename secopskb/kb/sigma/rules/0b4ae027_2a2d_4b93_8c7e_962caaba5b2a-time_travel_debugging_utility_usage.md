---
sigma_id: "0b4ae027-2a2d-4b93-8c7e-962caaba5b2a"
title: "Time Travel Debugging Utility Usage"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_lolbin_tttracer_mod_load.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_tttracer_mod_load.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "0b4ae027-2a2d-4b93-8c7e-962caaba5b2a"
  - "Time Travel Debugging Utility Usage"
attack_technique_ids:
  - "T1218"
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Time Travel Debugging Utility Usage

Detects usage of Time Travel Debugging Utility. Adversaries can execute malicious processes and dump processes, such as lsass.exe, via tttracer.exe.

## Metadata

- Rule ID: 0b4ae027-2a2d-4b93-8c7e-962caaba5b2a
- Status: test
- Level: high
- Author: Ensar Şamil, @sblmsrsn, @oscd_initiative
- Date: 2020-10-06
- Modified: 2022-10-09
- Source Path: rules/windows/process_creation/proc_creation_win_lolbin_tttracer_mod_load.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]
- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]

## Detection

```yaml
selection:
  ParentImage|endswith: \tttracer.exe
condition: selection
```

## False Positives

- Legitimate usage by software developers/testers

## References

- https://lolbas-project.github.io/lolbas/Binaries/Tttracer/
- https://twitter.com/mattifestation/status/1196390321783025666
- https://twitter.com/oulusoyum/status/1191329746069655553

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_tttracer_mod_load.yml)
