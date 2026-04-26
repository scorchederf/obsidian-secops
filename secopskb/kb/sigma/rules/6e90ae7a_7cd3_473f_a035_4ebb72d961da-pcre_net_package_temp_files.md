---
sigma_id: "6e90ae7a-7cd3-473f-a035-4ebb72d961da"
title: "PCRE.NET Package Temp Files"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_pcre_net_temp_file.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_pcre_net_temp_file.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "6e90ae7a-7cd3-473f-a035-4ebb72d961da"
  - "PCRE.NET Package Temp Files"
attack_technique_ids:
  - "T1059"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PCRE.NET Package Temp Files

Detects processes creating temp files related to PCRE.NET package

## Metadata

- Rule ID: 6e90ae7a-7cd3-473f-a035-4ebb72d961da
- Status: test
- Level: high
- Author: Roberto Rodriguez (Cyb3rWard0g), OTR (Open Threat Research)
- Date: 2020-10-29
- Modified: 2022-10-09
- Source Path: rules/windows/file/file_event/file_event_win_pcre_net_temp_file.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]

## Detection

```yaml
selection:
  TargetFilename|contains: \AppData\Local\Temp\ba9ea7344a4a5f591d6e5dc32a13494b\
condition: selection
```

## False Positives

- Unknown

## References

- https://twitter.com/rbmaslen/status/1321859647091970051
- https://twitter.com/tifkin_/status/1321916444557365248

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_pcre_net_temp_file.yml)
