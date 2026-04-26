---
sigma_id: "fed85bf9-e075-4280-9159-fbe8a023d6fa"
title: "Advanced IP Scanner - File Event"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_advanced_ip_scanner.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_advanced_ip_scanner.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "windows / file_event"
aliases:
  - "fed85bf9-e075-4280-9159-fbe8a023d6fa"
  - "Advanced IP Scanner - File Event"
attack_technique_ids:
  - "T1046"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Advanced IP Scanner - File Event

Detects the use of Advanced IP Scanner. Seems to be a popular tool for ransomware groups.

## Metadata

- Rule ID: fed85bf9-e075-4280-9159-fbe8a023d6fa
- Status: test
- Level: medium
- Author: @ROxPinTeddy
- Date: 2020-05-12
- Modified: 2022-11-29
- Source Path: rules/windows/file/file_event/file_event_win_advanced_ip_scanner.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1046-network_service_discovery|T1046]]

## Detection

```yaml
selection:
  TargetFilename|contains: \AppData\Local\Temp\Advanced IP Scanner 2
condition: selection
```

## False Positives

- Legitimate administrative use

## References

- https://news.sophos.com/en-us/2019/12/09/snatch-ransomware-reboots-pcs-into-safe-mode-to-bypass-protection/
- https://www.fireeye.com/blog/threat-research/2020/05/tactics-techniques-procedures-associated-with-maze-ransomware-incidents.html
- https://labs.f-secure.com/blog/prelude-to-ransomware-systembc
- https://assets.documentcloud.org/documents/20444693/fbi-pin-egregor-ransomware-bc-01062021.pdf
- https://thedfirreport.com/2021/01/18/all-that-for-a-coinminer

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_advanced_ip_scanner.yml)
