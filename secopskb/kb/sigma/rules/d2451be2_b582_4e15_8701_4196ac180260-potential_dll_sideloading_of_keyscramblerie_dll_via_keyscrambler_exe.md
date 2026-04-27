---
sigma_id: "d2451be2-b582-4e15-8701-4196ac180260"
title: "Potential DLL Sideloading Of KeyScramblerIE.DLL Via KeyScrambler.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_side_load_keyscrambler.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_keyscrambler.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "windows / image_load"
aliases:
  - "d2451be2-b582-4e15-8701-4196ac180260"
  - "Potential DLL Sideloading Of KeyScramblerIE.DLL Via KeyScrambler.EXE"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Potential DLL Sideloading Of KeyScramblerIE.DLL Via KeyScrambler.EXE

Detects potential DLL side loading of "KeyScramblerIE.dll" by "KeyScrambler.exe".
Various threat actors and malware have been found side loading a masqueraded "KeyScramblerIE.dll" through "KeyScrambler.exe".

## Metadata

- Rule ID: d2451be2-b582-4e15-8701-4196ac180260
- Status: test
- Level: high
- Author: Swachchhanda Shrawan Poudel
- Date: 2024-04-15
- Source Path: rules/windows/image_load/image_load_side_load_keyscrambler.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection:
  Image|endswith:
  - \KeyScrambler.exe
  - \KeyScramblerLogon.exe
  ImageLoaded|endswith: \KeyScramblerIE.dll
filter_main_legitimate_path:
  Image|contains:
  - C:\Program Files (x86)\KeyScrambler\
  - C:\Program Files\KeyScrambler\
  ImageLoaded|contains:
  - C:\Program Files (x86)\KeyScrambler\
  - C:\Program Files\KeyScrambler\
filter_main_signature:
  Signature: QFX Software Corporation
  SignatureStatus: Valid
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://thehackernews.com/2024/03/two-chinese-apt-groups-ramp-up-cyber.html
- https://csirt-cti.net/2024/02/01/stately-taurus-continued-new-information-on-cyberespionage-attacks-against-myanmar-military-junta/
- https://bazaar.abuse.ch/sample/5cb9876681f78d3ee8a01a5aaa5d38b05ec81edc48b09e3865b75c49a2187831/
- https://twitter.com/Max_Mal_/status/1775222576639291859
- https://twitter.com/DTCERT/status/1712785426895839339

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_keyscrambler.yml)
