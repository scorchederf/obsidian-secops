---
sigma_id: "025bd229-fd1f-4fdb-97ab-20006e1a5368"
title: "Unusual File Download from Direct IP Address"
framework: "sigma"
generated: "true"
source_path: "rules/windows/create_stream_hash/create_stream_hash_susp_ip_domains.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/create_stream_hash/create_stream_hash_susp_ip_domains.yml"
build_date: "2026-04-27 19:13:58"
status: "test"
level: "high"
logsource: "windows / create_stream_hash"
aliases:
  - "025bd229-fd1f-4fdb-97ab-20006e1a5368"
  - "Unusual File Download from Direct IP Address"
attack_technique_ids:
  - "T1564.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the download of suspicious file type from URLs with IP

## Logsource

- category: create_stream_hash
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1564-hide_artifacts#^t1564004-ntfs-file-attributes|T1564.004: NTFS File Attributes]]

## Detection

```yaml
selection:
  Contents|re: http[s]?://[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}
  TargetFilename|contains:
  - .ps1:Zone
  - .bat:Zone
  - .exe:Zone
  - .vbe:Zone
  - .vbs:Zone
  - .dll:Zone
  - .one:Zone
  - .cmd:Zone
  - .hta:Zone
  - .xll:Zone
  - .lnk:Zone
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/trustedsec/SysmonCommunityGuide/blob/adcdfee20999f422b974c8d4149bf4c361237db7/chapters/file-stream-creation-hash.md
- https://labs.withsecure.com/publications/detecting-onenote-abuse

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/create_stream_hash/create_stream_hash_susp_ip_domains.yml)
