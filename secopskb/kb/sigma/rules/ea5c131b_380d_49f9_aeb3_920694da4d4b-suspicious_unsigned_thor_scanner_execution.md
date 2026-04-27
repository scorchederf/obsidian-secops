---
sigma_id: "ea5c131b-380d-49f9-aeb3-920694da4d4b"
title: "Suspicious Unsigned Thor Scanner Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_thor_unsigned_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_thor_unsigned_execution.yml"
build_date: "2026-04-27 19:13:57"
status: "stable"
level: "high"
logsource: "windows / image_load"
aliases:
  - "ea5c131b-380d-49f9-aeb3-920694da4d4b"
  - "Suspicious Unsigned Thor Scanner Execution"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects loading and execution of an unsigned thor scanner binary.

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow#^t1574001-dll|T1574.001: DLL]]

## Detection

```yaml
selection:
  Image|endswith:
  - \thor.exe
  - \thor64.exe
  ImageLoaded|endswith:
  - \thor.exe
  - \thor64.exe
filter_main:
  Signed: 'true'
  SignatureStatus: valid
  Signature: Nextron Systems GmbH
condition: selection and not filter_main
```

## False Positives

- Other legitimate binaries named "thor.exe" that aren't published by Nextron Systems

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_thor_unsigned_execution.yml)
