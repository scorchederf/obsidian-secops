---
sigma_id: "68654bf0-4412-43d5-bfe8-5eaa393cd939"
title: "Potential DLL Sideloading Via JsSchHlp"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_side_load_jsschhlp.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_jsschhlp.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "medium"
logsource: "windows / image_load"
aliases:
  - "68654bf0-4412-43d5-bfe8-5eaa393cd939"
  - "Potential DLL Sideloading Via JsSchHlp"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential DLL Sideloading Via JsSchHlp

Detects potential DLL sideloading using JUSTSYSTEMS Japanese word processor

## Metadata

- Rule ID: 68654bf0-4412-43d5-bfe8-5eaa393cd939
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-12-14
- Source Path: rules/windows/image_load/image_load_side_load_jsschhlp.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection:
  ImageLoaded|endswith: \JSESPR.dll
filter:
  ImageLoaded|startswith: C:\Program Files\Common Files\Justsystem\JsSchHlp\
condition: selection and not filter
```

## False Positives

- Unknown

## References

- https://www.welivesecurity.com/2022/12/14/unmasking-mirrorface-operation-liberalface-targeting-japanese-political-entities/
- http://www.windowexe.com/bbs/board.php?q=jsschhlp-exe-c-program-files-common-files-justsystem-jsschhlp-jsschhlp

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_jsschhlp.yml)
