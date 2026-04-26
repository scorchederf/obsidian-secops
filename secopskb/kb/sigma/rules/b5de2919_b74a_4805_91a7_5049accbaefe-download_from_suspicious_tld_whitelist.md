---
sigma_id: "b5de2919-b74a-4805-91a7-5049accbaefe"
title: "Download From Suspicious TLD - Whitelist"
framework: "sigma"
generated: "true"
source_path: "rules/web/proxy_generic/proxy_download_susp_tlds_whitelist.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/web/proxy_generic/proxy_download_susp_tlds_whitelist.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "low"
logsource: "proxy"
aliases:
  - "b5de2919-b74a-4805-91a7-5049accbaefe"
  - "Download From Suspicious TLD - Whitelist"
attack_technique_ids:
  - "T1566"
  - "T1203"
  - "T1204.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Download From Suspicious TLD - Whitelist

Detects executable downloads from suspicious remote systems

## Metadata

- Rule ID: b5de2919-b74a-4805-91a7-5049accbaefe
- Status: test
- Level: low
- Author: Florian Roth (Nextron Systems)
- Date: 2017-03-13
- Modified: 2023-05-18
- Source Path: rules/web/proxy_generic/proxy_download_susp_tlds_whitelist.yml

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
filter:
  cs-host|endswith:
  - .com
  - .org
  - .net
  - .edu
  - .gov
  - .uk
  - .ca
  - .de
  - .jp
  - .fr
  - .au
  - .us
  - .ch
  - .it
  - .nl
  - .se
  - .no
  - .es
condition: selection and not filter
```

## False Positives

- All kind of software downloads

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/web/proxy_generic/proxy_download_susp_tlds_whitelist.yml)
