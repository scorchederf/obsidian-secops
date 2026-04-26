---
sigma_id: "68c2c604-92ad-468b-bf4a-aac49adad08c"
title: "HTTP Request to Low Reputation TLD or Suspicious File Extension"
framework: "sigma"
generated: "true"
source_path: "rules/network/zeek/zeek_http_susp_file_ext_from_susp_tld.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/network/zeek/zeek_http_susp_file_ext_from_susp_tld.yml"
build_date: "2026-04-26 14:14:26"
status: "experimental"
level: "medium"
logsource: "zeek / http"
aliases:
  - "68c2c604-92ad-468b-bf4a-aac49adad08c"
  - "HTTP Request to Low Reputation TLD or Suspicious File Extension"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# HTTP Request to Low Reputation TLD or Suspicious File Extension

Detects HTTP requests to low reputation TLDs (e.g. .xyz, .top, .ru) or ending in suspicious file extensions (.exe, .dll, .hta), which may indicate malicious activity.

## Metadata

- Rule ID: 68c2c604-92ad-468b-bf4a-aac49adad08c
- Status: experimental
- Level: medium
- Author: @signalblur, Corelight
- Date: 2025-02-26
- Source Path: rules/network/zeek/zeek_http_susp_file_ext_from_susp_tld.yml

## Logsource

- product: zeek
- service: http

## Detection

```yaml
selection_suspicious_tld:
  host|endswith:
  - .bid
  - .by
  - .cf
  - .click
  - .cm
  - .ga
  - .gq
  - .ir
  - .kp
  - .loan
  - .ml
  - .mm
  - .party
  - .pw
  - .ru
  - .su
  - .sy
  - .tk
  - .top
  - .tv
  - .ve
  - .work
  - .xyz
selection_malicious_ext:
  uri|endswith:
  - .bat
  - .bin
  - .cmd
  - .cpl
  - .dll
  - .dylib
  - .elf
  - .exe
  - .hta
  - .iso
  - .jar
  - .js
  - .lnk
  - .msi
  - .pif
  - .ps1
  - .py
  - .reg
  - .scr
  - .sh
  - .so
  - .vbs
  - .wsf
selection_malicious_mime:
  resp_mime_types:
  - application/vnd.microsoft.portable-executable
  - application/x-bat
  - application/x-dosexec
  - application/x-elf
  - application/x-iso9660-image
  - application/x-java-archive
  - application/x-ms-shortcut
  - application/x-msdos-program
  - application/x-msdownload
  - application/x-python-code
  - application/x-sh
condition: selection_suspicious_tld and 1 of selection_malicious_*
```

## False Positives

- Rare legitimate software downloads from low quality TLDs

## References

- https://www.howtogeek.com/137270/50-file-extensions-that-are-potentially-dangerous-on-windows
- https://www.spamhaus.org/reputation-statistics/cctlds/domains/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/network/zeek/zeek_http_susp_file_ext_from_susp_tld.yml)
