---
sigma_id: "6d44fb93-e7d2-475c-9d3d-54c9c1e33427"
title: "BITS Transfer Job With Uncommon Or Suspicious Remote TLD"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/bits_client/win_bits_client_new_transfer_via_uncommon_tld.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/bits_client/win_bits_client_new_transfer_via_uncommon_tld.yml"
build_date: "2026-04-26 14:14:21"
status: "test"
level: "medium"
logsource: "windows / bits-client"
aliases:
  - "6d44fb93-e7d2-475c-9d3d-54c9c1e33427"
  - "BITS Transfer Job With Uncommon Or Suspicious Remote TLD"
attack_technique_ids:
  - "T1197"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# BITS Transfer Job With Uncommon Or Suspicious Remote TLD

Detects a suspicious download using the BITS client from a FQDN that is unusual. Adversaries may abuse BITS jobs to persistently execute or clean up after malicious payloads.

## Metadata

- Rule ID: 6d44fb93-e7d2-475c-9d3d-54c9c1e33427
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2022-06-10
- Modified: 2025-02-28
- Source Path: rules/windows/builtin/bits_client/win_bits_client_new_transfer_via_uncommon_tld.yml

## Logsource

- product: windows
- service: bits-client

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1197-bits_jobs|T1197]]

## Detection

```yaml
selection:
  EventID: 16403
filter_main_generic:
  RemoteName|contains:
  - .azureedge.net/
  - .com/
  - .sfx.ms/
  - download.mozilla.org/
  - cdn.onenote.net/
  - cdn.office.net/
  - tscdn.m365.static.microsoft/
condition: selection and not 1 of filter_main_*
```

## False Positives

- This rule doesn't exclude other known TLDs such as ".org" or ".net". It's recommended to apply additional filters for software and scripts that leverage the BITS service

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1197/T1197.md
- https://twitter.com/malmoeb/status/1535142803075960832

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/bits_client/win_bits_client_new_transfer_via_uncommon_tld.yml)
