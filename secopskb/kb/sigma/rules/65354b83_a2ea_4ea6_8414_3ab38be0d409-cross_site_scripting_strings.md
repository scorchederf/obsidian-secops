---
sigma_id: "65354b83-a2ea-4ea6-8414-3ab38be0d409"
title: "Cross Site Scripting Strings"
framework: "sigma"
generated: "true"
source_path: "rules/web/webserver_generic/web_xss_in_access_logs.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/web/webserver_generic/web_xss_in_access_logs.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "webserver"
aliases:
  - "65354b83-a2ea-4ea6-8414-3ab38be0d409"
  - "Cross Site Scripting Strings"
attack_technique_ids:
  - "T1189"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Cross Site Scripting Strings

Detects XSS attempts injected via GET requests in access logs

## Metadata

- Rule ID: 65354b83-a2ea-4ea6-8414-3ab38be0d409
- Status: test
- Level: high
- Author: Saw Win Naung, Nasreddine Bencherchali
- Date: 2021-08-15
- Modified: 2022-06-14
- Source Path: rules/web/webserver_generic/web_xss_in_access_logs.yml

## Logsource

- category: webserver

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1189-drive-by_compromise|T1189]]

## Detection

```yaml
select_method:
  cs-method: GET
keywords:
- =<script>
- =%3Cscript%3E
- =%253Cscript%253E
- '<iframe '
- '%3Ciframe '
- '<svg '
- '%3Csvg '
- document.cookie
- document.domain
- ' onerror='
- ' onresize='
- ' onload="'
- onmouseover=
- ${alert
- javascript:alert
- javascript%3Aalert
filter:
  sc-status: 404
condition: select_method and keywords and not filter
```

## False Positives

- JavaScripts,CSS Files and PNG files
- User searches in search boxes of the respective website
- Internal vulnerability scanners can cause some serious FPs when used, if you experience a lot of FPs due to this think of adding more filters such as "User Agent" strings and more response codes

## References

- https://github.com/payloadbox/xss-payload-list
- https://portswigger.net/web-security/cross-site-scripting/contexts

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/web/webserver_generic/web_xss_in_access_logs.yml)
