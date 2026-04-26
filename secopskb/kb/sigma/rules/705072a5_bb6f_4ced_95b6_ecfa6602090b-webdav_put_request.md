---
sigma_id: "705072a5-bb6f-4ced-95b6-ecfa6602090b"
title: "WebDav Put Request"
framework: "sigma"
generated: "true"
source_path: "rules/network/zeek/zeek_http_webdav_put_request.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/network/zeek/zeek_http_webdav_put_request.yml"
build_date: "2026-04-26 14:14:39"
status: "test"
level: "low"
logsource: "zeek / http"
aliases:
  - "705072a5-bb6f-4ced-95b6-ecfa6602090b"
  - "WebDav Put Request"
attack_technique_ids:
  - "T1048.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# WebDav Put Request

A General detection for WebDav user-agent being used to PUT files on a WebDav network share. This could be an indicator of exfiltration.

## Metadata

- Rule ID: 705072a5-bb6f-4ced-95b6-ecfa6602090b
- Status: test
- Level: low
- Author: Roberto Rodriguez (Cyb3rWard0g), OTR (Open Threat Research)
- Date: 2020-05-02
- Modified: 2024-03-13
- Source Path: rules/network/zeek/zeek_http_webdav_put_request.yml

## Logsource

- product: zeek
- service: http

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1048-exfiltration_over_alternative_protocol|T1048.003]]

## Detection

```yaml
selection:
  user_agent|contains: WebDAV
  method: PUT
filter:
  id.resp_h|cidr:
  - 10.0.0.0/8
  - 127.0.0.0/8
  - 172.16.0.0/12
  - 192.168.0.0/16
  - 169.254.0.0/16
condition: selection and not filter
```

## False Positives

- Unknown

## References

- https://github.com/OTRF/detection-hackathon-apt29/issues/17

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/network/zeek/zeek_http_webdav_put_request.yml)
