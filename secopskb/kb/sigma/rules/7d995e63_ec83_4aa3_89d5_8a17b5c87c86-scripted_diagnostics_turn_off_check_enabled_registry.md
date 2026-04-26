---
sigma_id: "7d995e63-ec83-4aa3-89d5-8a17b5c87c86"
title: "Scripted Diagnostics Turn Off Check Enabled - Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_enabling_turnoffcheck.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_enabling_turnoffcheck.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "7d995e63-ec83-4aa3-89d5-8a17b5c87c86"
  - "Scripted Diagnostics Turn Off Check Enabled - Registry"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Scripted Diagnostics Turn Off Check Enabled - Registry

Detects enabling TurnOffCheck which can be used to bypass defense of MSDT Follina vulnerability

## Metadata

- Rule ID: 7d995e63-ec83-4aa3-89d5-8a17b5c87c86
- Status: test
- Level: medium
- Author: Christopher Peacock @securepeacock, SCYTHE @scythe_io
- Date: 2022-06-15
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_enabling_turnoffcheck.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection:
  TargetObject|endswith: \Policies\Microsoft\Windows\ScriptedDiagnostics\TurnOffCheck
  Details: DWORD (0x00000001)
condition: selection
```

## False Positives

- Administrator actions

## References

- https://twitter.com/wdormann/status/1537075968568877057?s=20&t=0lr18OAnmAGoGpma6grLUw

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_enabling_turnoffcheck.yml)
