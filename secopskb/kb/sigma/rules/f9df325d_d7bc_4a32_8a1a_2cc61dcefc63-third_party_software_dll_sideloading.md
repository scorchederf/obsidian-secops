---
sigma_id: "f9df325d-d7bc-4a32-8a1a-2cc61dcefc63"
title: "Third Party Software DLL Sideloading"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_side_load_third_party.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_third_party.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / image_load"
aliases:
  - "f9df325d-d7bc-4a32-8a1a-2cc61dcefc63"
  - "Third Party Software DLL Sideloading"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Third Party Software DLL Sideloading

Detects DLL sideloading of DLLs that are part of third party software (zoom, discord....etc)

## Metadata

- Rule ID: f9df325d-d7bc-4a32-8a1a-2cc61dcefc63
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems), Wietze Beukema (project and research)
- Date: 2022-08-17
- Source Path: rules/windows/image_load/image_load_side_load_third_party.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection_lenovo:
  ImageLoaded|endswith: \commfunc.dll
filter_lenovo:
- ImageLoaded|contains: \AppData\local\Google\Chrome\Application\
- ImageLoaded|startswith:
  - C:\Program Files\Lenovo\Communications Utility\
  - C:\Program Files (x86)\Lenovo\Communications Utility\
selection_toshiba:
  ImageLoaded|endswith: \tosbtkbd.dll
filter_toshiba:
  ImageLoaded|startswith:
  - C:\Program Files\Toshiba\Bluetooth Toshiba Stack\
  - C:\Program Files (x86)\Toshiba\Bluetooth Toshiba Stack\
condition: (selection_lenovo and not filter_lenovo) or (selection_toshiba and not
  filter_toshiba)
```

## False Positives

- Unknown

## References

- https://hijacklibs.net/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_third_party.yml)
