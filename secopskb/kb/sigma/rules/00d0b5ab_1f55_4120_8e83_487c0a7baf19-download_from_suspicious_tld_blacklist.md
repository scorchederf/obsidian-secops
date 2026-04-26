---
sigma_id: "00d0b5ab-1f55-4120-8e83-487c0a7baf19"
title: "Download From Suspicious TLD - Blacklist"
framework: "sigma"
generated: "true"
source_path: "rules/web/proxy_generic/proxy_download_susp_tlds_blacklist.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/web/proxy_generic/proxy_download_susp_tlds_blacklist.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "low"
logsource: "proxy"
aliases:
  - "00d0b5ab-1f55-4120-8e83-487c0a7baf19"
  - "Download From Suspicious TLD - Blacklist"
attack_technique_ids:
  - "T1566"
  - "T1203"
  - "T1204.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Download From Suspicious TLD - Blacklist

Detects download of certain file types from hosts in suspicious TLDs

## Metadata

- Rule ID: 00d0b5ab-1f55-4120-8e83-487c0a7baf19
- Status: test
- Level: low
- Author: Florian Roth (Nextron Systems)
- Date: 2017-11-07
- Modified: 2023-05-18
- Source Path: rules/web/proxy_generic/proxy_download_susp_tlds_blacklist.yml

## Logsource

- category: proxy

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1566-phishing|T1566]]
- [[kb/attack/techniques/T1203-exploitation_for_client_execution|T1203]]
- [[kb/attack/techniques/T1204-user_execution|T1204.002]]

## Detection

```yaml
selection:
  c-uri-extension:
  - exe
  - vbs
  - bat
  - rar
  - ps1
  - doc
  - docm
  - xls
  - xlsm
  - pptm
  - rtf
  - hta
  - dll
  - ws
  - wsf
  - sct
  - zip
  cs-host|endswith:
  - .country
  - .stream
  - .gdn
  - .mom
  - .xin
  - .kim
  - .men
  - .loan
  - .download
  - .racing
  - .online
  - .science
  - .ren
  - .gb
  - .win
  - .top
  - .review
  - .vip
  - .party
  - .tech
  - .xyz
  - .date
  - .faith
  - .zip
  - .cricket
  - .space
  - .info
  - .vn
  - .cm
  - .am
  - .cc
  - .asia
  - .ws
  - .tk
  - .biz
  - .su
  - .st
  - .ro
  - .ge
  - .ms
  - .pk
  - .nu
  - .me
  - .ph
  - .to
  - .tt
  - .name
  - .tv
  - .kz
  - .tc
  - .mobi
  - .study
  - .click
  - .link
  - .trade
  - .accountant
  - .cf
  - .gq
  - .ml
  - .ga
  - .pw
condition: selection
```

## False Positives

- All kinds of software downloads

## References

- https://www.symantec.com/connect/blogs/shady-tld-research-gdn-and-our-2016-wrap
- https://promos.mcafee.com/en-US/PDF/MTMW_Report.pdf
- https://www.spamhaus.org/statistics/tlds/
- https://krebsonsecurity.com/2018/06/bad-men-at-work-please-dont-click/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/web/proxy_generic/proxy_download_susp_tlds_blacklist.yml)
