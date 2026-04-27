---
sigma_id: "0bb4bbeb-fe52-4044-b40c-430a04577ebe"
title: "Potentially Suspicious File Download From ZIP TLD"
framework: "sigma"
generated: "true"
source_path: "rules/windows/create_stream_hash/create_stream_hash_zip_tld_download.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/create_stream_hash/create_stream_hash_zip_tld_download.yml"
build_date: "2026-04-27 19:13:54"
status: "test"
level: "high"
logsource: "windows / create_stream_hash"
aliases:
  - "0bb4bbeb-fe52-4044-b40c-430a04577ebe"
  - "Potentially Suspicious File Download From ZIP TLD"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the download of a file with a potentially suspicious extension from a .zip top level domain.

## Logsource

- category: create_stream_hash
- product: windows

## Detection

```yaml
selection:
  Contents|contains: .zip/
  TargetFilename|contains:
  - .bat:Zone
  - .dat:Zone
  - .dll:Zone
  - .doc:Zone
  - .docm:Zone
  - .exe:Zone
  - .hta:Zone
  - .pptm:Zone
  - .ps1:Zone
  - .rar:Zone
  - .rtf:Zone
  - .sct:Zone
  - .vbe:Zone
  - .vbs:Zone
  - .ws:Zone
  - .wsf:Zone
  - .xll:Zone
  - .xls:Zone
  - .xlsm:Zone
  - .zip:Zone
condition: selection
```

## False Positives

- Legitimate file downloads from a websites and web services that uses the ".zip" top level domain.

## References

- https://twitter.com/cyb3rops/status/1659175181695287297
- https://fabian-voith.de/2020/06/25/sysmon-v11-1-reads-alternate-data-streams/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/create_stream_hash/create_stream_hash_zip_tld_download.yml)
