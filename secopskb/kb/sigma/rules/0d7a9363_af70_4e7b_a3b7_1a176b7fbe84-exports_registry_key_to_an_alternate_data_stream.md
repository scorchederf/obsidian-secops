---
sigma_id: "0d7a9363-af70-4e7b-a3b7-1a176b7fbe84"
title: "Exports Registry Key To an Alternate Data Stream"
framework: "sigma"
generated: "true"
source_path: "rules/windows/create_stream_hash/create_stream_hash_regedit_export_to_ads.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/create_stream_hash/create_stream_hash_regedit_export_to_ads.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / create_stream_hash"
aliases:
  - "0d7a9363-af70-4e7b-a3b7-1a176b7fbe84"
  - "Exports Registry Key To an Alternate Data Stream"
attack_technique_ids:
  - "T1564.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Exports Registry Key To an Alternate Data Stream

Exports the target Registry key and hides it in the specified alternate data stream.

## Metadata

- Rule ID: 0d7a9363-af70-4e7b-a3b7-1a176b7fbe84
- Status: test
- Level: high
- Author: Oddvar Moe, Sander Wiebing, oscd.community
- Date: 2020-10-07
- Modified: 2021-11-27
- Source Path: rules/windows/create_stream_hash/create_stream_hash_regedit_export_to_ads.yml

## Logsource

- category: create_stream_hash
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1564-hide_artifacts|T1564.004]]

## Detection

```yaml
selection:
  Image|endswith: \regedit.exe
condition: selection
```

## False Positives

- Unknown

## References

- https://lolbas-project.github.io/lolbas/Binaries/Regedit/
- https://gist.github.com/api0cradle/cdd2d0d0ec9abb686f0e89306e277b8f

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/create_stream_hash/create_stream_hash_regedit_export_to_ads.yml)
