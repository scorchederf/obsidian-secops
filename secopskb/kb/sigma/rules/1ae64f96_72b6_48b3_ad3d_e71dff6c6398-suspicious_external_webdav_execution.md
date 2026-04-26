---
sigma_id: "1ae64f96-72b6-48b3-ad3d-e71dff6c6398"
title: "Suspicious External WebDAV Execution"
framework: "sigma"
generated: "true"
source_path: "rules/web/proxy_generic/proxy_webdav_external_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/web/proxy_generic/proxy_webdav_external_execution.yml"
build_date: "2026-04-26 15:01:51"
status: "test"
level: "high"
logsource: "proxy"
aliases:
  - "1ae64f96-72b6-48b3-ad3d-e71dff6c6398"
  - "Suspicious External WebDAV Execution"
attack_technique_ids:
  - "T1584"
  - "T1566"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious External WebDAV Execution

Detects executables launched from external WebDAV shares using the WebDAV Explorer integration, commonly seen in initial access campaigns.

## Metadata

- Rule ID: 1ae64f96-72b6-48b3-ad3d-e71dff6c6398
- Status: test
- Level: high
- Author: Ahmed Farouk
- Date: 2024-05-10
- Source Path: rules/web/proxy_generic/proxy_webdav_external_execution.yml

## Logsource

- category: proxy

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1584-compromise_infrastructure|T1584]]
- [[kb/attack/techniques/T1566-phishing|T1566]]

## Detection

```yaml
selection_webdav:
  c-useragent|startswith: Microsoft-WebDAV-MiniRedir/
  cs-method: GET
selection_execution:
  c-uri|endswith:
  - .7z
  - .bat
  - .dat
  - .cmd
  - .exe
  - .js
  - .lnk
  - .ps1
  - .rar
  - .url
  - .vbe
  - .vbs
  - .zip
filter_main_local_ips:
  dst_ip|cidr:
  - 127.0.0.0/8
  - 10.0.0.0/8
  - 172.16.0.0/12
  - 192.168.0.0/16
  - 169.254.0.0/16
  - ::1/128
  - fe80::/10
  - fc00::/7
condition: all of selection_* and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://dear-territory-023.notion.site/WebDav-Share-Testing-e4950fa0c00149c3aa430d779b9b1d0f?pvs=4
- https://micahbabinski.medium.com/search-ms-webdav-and-chill-99c5b23ac462
- https://www.trendmicro.com/en_no/research/24/b/cve202421412-water-hydra-targets-traders-with-windows-defender-s.html
- https://www.trellix.com/en-us/about/newsroom/stories/research/beyond-file-search-a-novel-method.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/web/proxy_generic/proxy_webdav_external_execution.yml)
