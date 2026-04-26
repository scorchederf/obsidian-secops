---
sigma_id: "55e29995-75e7-451a-bef0-6225e2f13597"
title: "Potential Credential Dumping Via LSASS SilentProcessExit Technique"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_event/registry_event_silentprocessexit_lsass.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_silentprocessexit_lsass.yml"
build_date: "2026-04-26 15:01:48"
status: "test"
level: "critical"
logsource: "windows / registry_event"
aliases:
  - "55e29995-75e7-451a-bef0-6225e2f13597"
  - "Potential Credential Dumping Via LSASS SilentProcessExit Technique"
attack_technique_ids:
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potential Credential Dumping Via LSASS SilentProcessExit Technique

Detects changes to the Registry in which a monitor program gets registered to dump the memory of the lsass.exe process

## Metadata

- Rule ID: 55e29995-75e7-451a-bef0-6225e2f13597
- Status: test
- Level: critical
- Author: Florian Roth (Nextron Systems)
- Date: 2021-02-26
- Modified: 2022-12-19
- Source Path: rules/windows/registry/registry_event/registry_event_silentprocessexit_lsass.yml

## Logsource

- category: registry_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]

## Detection

```yaml
selection:
  TargetObject|contains: Microsoft\Windows NT\CurrentVersion\SilentProcessExit\lsass.exe
condition: selection
```

## False Positives

- Unlikely

## References

- https://www.deepinstinct.com/2021/02/16/lsass-memory-dumps-are-stealthier-than-ever-before-part-2/
- https://oddvar.moe/2018/04/10/persistence-using-globalflags-in-image-file-execution-options-hidden-from-autoruns-exe/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_silentprocessexit_lsass.yml)
