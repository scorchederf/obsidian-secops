---
sigma_id: "2ea44a60-cfda-11ea-87d0-0242ac130003"
title: "Webshell ReGeorg Detection Via Web Logs"
framework: "sigma"
generated: "true"
source_path: "rules/web/webserver_generic/web_webshell_regeorg.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/web/webserver_generic/web_webshell_regeorg.yml"
build_date: "2026-04-26 17:03:24"
status: "test"
level: "high"
logsource: "webserver"
aliases:
  - "2ea44a60-cfda-11ea-87d0-0242ac130003"
  - "Webshell ReGeorg Detection Via Web Logs"
attack_technique_ids:
  - "T1505.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Webshell ReGeorg Detection Via Web Logs

Certain strings in the uri_query field when combined with null referer and null user agent can indicate activity associated with the webshell ReGeorg.

## Metadata

- Rule ID: 2ea44a60-cfda-11ea-87d0-0242ac130003
- Status: test
- Level: high
- Author: Cian Heasley
- Date: 2020-08-04
- Modified: 2023-01-02
- Source Path: rules/web/webserver_generic/web_webshell_regeorg.yml

## Logsource

- category: webserver

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1505-server_software_component|T1505.003]]

## Detection

```yaml
selection:
  cs-uri-query|contains:
  - cmd=read
  - connect&target
  - cmd=connect
  - cmd=disconnect
  - cmd=forward
filter:
  cs-referer: null
  cs-user-agent: null
  cs-method: POST
condition: selection and filter
```

## False Positives

- Web applications that use the same URL parameters as ReGeorg

## References

- https://community.rsa.com/community/products/netwitness/blog/2019/02/19/web-shells-and-netwitness-part-3
- https://github.com/sensepost/reGeorg

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/web/webserver_generic/web_webshell_regeorg.yml)
