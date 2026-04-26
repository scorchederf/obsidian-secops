---
sigma_id: "b69888d4-380c-45ce-9cf9-d9ce46e67821"
title: "Hidden Executable In NTFS Alternate Data Stream"
framework: "sigma"
generated: "true"
source_path: "rules/windows/create_stream_hash/create_stream_hash_ads_executable.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/create_stream_hash/create_stream_hash_ads_executable.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "medium"
logsource: "windows / create_stream_hash"
aliases:
  - "b69888d4-380c-45ce-9cf9-d9ce46e67821"
  - "Hidden Executable In NTFS Alternate Data Stream"
attack_technique_ids:
  - "T1564.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Hidden Executable In NTFS Alternate Data Stream

Detects the creation of an ADS (Alternate Data Stream) that contains an executable by looking at a non-empty Imphash

## Metadata

- Rule ID: b69888d4-380c-45ce-9cf9-d9ce46e67821
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems), @0xrawsec
- Date: 2018-06-03
- Modified: 2023-02-10
- Source Path: rules/windows/create_stream_hash/create_stream_hash_ads_executable.yml

## Logsource

- category: create_stream_hash
- definition: Requirements: Sysmon or equivalent configured with Imphash logging
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1564-hide_artifacts|T1564.004]]

### Software Tags

- S0139

## Detection

```yaml
selection:
  Hash|contains: IMPHASH=
filter_main_null:
  Hash|contains: IMPHASH=00000000000000000000000000000000
condition: selection and not 1 of filter_main_*
```

## False Positives

- This rule isn't looking for any particular binary characteristics. As legitimate installers and programs were seen embedding hidden binaries in their ADS. Some false positives are expected from browser processes and similar.

## References

- https://twitter.com/0xrawsec/status/1002478725605273600?s=21

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/create_stream_hash/create_stream_hash_ads_executable.yml)
