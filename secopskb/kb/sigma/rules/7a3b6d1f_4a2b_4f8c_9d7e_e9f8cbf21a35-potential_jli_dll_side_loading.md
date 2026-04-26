---
sigma_id: "7a3b6d1f-4a2b-4f8c-9d7e-e9f8cbf21a35"
title: "Potential JLI.dll Side-Loading"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_side_load_jli.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_jli.yml"
build_date: "2026-04-26 14:14:32"
status: "experimental"
level: "high"
logsource: "windows / image_load"
aliases:
  - "7a3b6d1f-4a2b-4f8c-9d7e-e9f8cbf21a35"
  - "Potential JLI.dll Side-Loading"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential JLI.dll Side-Loading

Detects potential DLL side-loading of jli.dll.
JLI.dll has been observed being side-loaded by Java processes by various threat actors, including APT41, XWorm,
and others in order to load malicious payloads in context of legitimate Java processes.

## Metadata

- Rule ID: 7a3b6d1f-4a2b-4f8c-9d7e-e9f8cbf21a35
- Status: experimental
- Level: high
- Author: Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2025-07-25
- Modified: 2025-10-06
- Source Path: rules/windows/image_load/image_load_side_load_jli.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection:
  ImageLoaded|endswith: \jli.dll
filter_main_legitimate_install_paths:
  ImageLoaded|startswith:
  - C:\Program Files\
  - C:\Program Files (x86)\
  Description: OpenJDK Platform binary
  OriginalFileName: jli.dll
  Product|startswith: OpenJDK Platform
  Signed: 'true'
filter_optional_eclipse:
  ImageLoaded|startswith: C:\eclipse\plugins\
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Unknown

## References

- https://securelist.com/apt41-in-africa/116986/
- https://lab52.io/blog/snake-keylogger-in-geopolitical-affairs-abuse-of-trusted-java-utilities-in-cybercrime-operations/
- https://hijacklibs.net/entries/3rd_party/oracle/jli.html
- https://www.proofpoint.com/us/blog/threat-insight/phish-china-aligned-espionage-actors-ramp-up-taiwan-semiconductor-targeting

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_jli.yml)
