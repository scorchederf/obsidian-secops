---
sigma_id: "aac2fd97-bcba-491b-ad66-a6edf89c71bf"
title: "Executable from Webdav"
framework: "sigma"
generated: "true"
source_path: "rules/network/zeek/zeek_http_executable_download_from_webdav.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/network/zeek/zeek_http_executable_download_from_webdav.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "zeek / http"
aliases:
  - "aac2fd97-bcba-491b-ad66-a6edf89c71bf"
  - "Executable from Webdav"
attack_technique_ids:
  - "T1105"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Executable from Webdav

Detects executable access via webdav6. Can be seen in APT 29 such as from the emulated APT 29 hackathon https://github.com/OTRF/detection-hackathon-apt29/

## Metadata

- Rule ID: aac2fd97-bcba-491b-ad66-a6edf89c71bf
- Status: test
- Level: medium
- Author: SOC Prime, Adam Swan
- Date: 2020-05-01
- Modified: 2021-11-27
- Source Path: rules/network/zeek/zeek_http_executable_download_from_webdav.yml

## Logsource

- product: zeek
- service: http

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Detection

```yaml
selection_webdav:
- c-useragent|contains: WebDAV
- c-uri|contains: webdav
selection_executable:
- resp_mime_types|contains: dosexec
- c-uri|endswith: .exe
condition: selection_webdav and selection_executable
```

## False Positives

- Unknown

## References

- http://carnal0wnage.attackresearch.com/2012/06/webdav-server-to-download-custom.html
- https://github.com/OTRF/detection-hackathon-apt29

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/network/zeek/zeek_http_executable_download_from_webdav.yml)
