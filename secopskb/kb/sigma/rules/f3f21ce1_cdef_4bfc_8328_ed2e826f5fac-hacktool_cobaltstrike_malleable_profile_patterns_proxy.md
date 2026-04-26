---
sigma_id: "f3f21ce1-cdef-4bfc-8328-ed2e826f5fac"
title: "HackTool - CobaltStrike Malleable Profile Patterns - Proxy"
framework: "sigma"
generated: "true"
source_path: "rules/web/proxy_generic/proxy_hktl_cobalt_strike_malleable_c2_requests.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/web/proxy_generic/proxy_hktl_cobalt_strike_malleable_c2_requests.yml"
build_date: "2026-04-26 14:14:26"
status: "test"
level: "high"
logsource: "proxy"
aliases:
  - "f3f21ce1-cdef-4bfc-8328-ed2e826f5fac"
  - "HackTool - CobaltStrike Malleable Profile Patterns - Proxy"
attack_technique_ids:
  - "T1071.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# HackTool - CobaltStrike Malleable Profile Patterns - Proxy

Detects cobalt strike malleable profiles patterns (URI, User-Agents, Methods).

## Metadata

- Rule ID: f3f21ce1-cdef-4bfc-8328-ed2e826f5fac
- Status: test
- Level: high
- Author: Markus Neis, Florian Roth (Nextron Systems)
- Date: 2024-02-15
- Source Path: rules/web/proxy_generic/proxy_hktl_cobalt_strike_malleable_c2_requests.yml

## Logsource

- category: proxy

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1071-application_layer_protocol|T1071.001]]

## Detection

```yaml
selection_amazon_1:
  c-useragent: Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko
  cs-method: GET
  c-uri: /s/ref=nb_sb_noss_1/167-3294888-0262949/field-keywords=books
  cs-host: www.amazon.com
  cs-cookie|endswith: =csm-hit=s-24KU11BB82RZSYGJ3BDK|1419899012996
selection_amazon_2:
  c-useragent: Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko
  cs-method: POST
  c-uri: /N4215/adj/amzn.us.sr.aps
  cs-host: www.amazon.com
selection_generic_1:
  c-useragent:
  - Mozilla/4.0 (compatible; MSIE 6.0;Windows NT 5.1)
  - Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2;
    .NET CLR 3.0.30729; .NET4.0C; .NET4.0E )
  - Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 5.2) Java/1.5.0_08
selection_generic_2:
  c-useragent|endswith: ; MANM; MANM)
selection_oscp:
  c-uri|contains: /oscp/
  cs-host: ocsp.verisign.com
selection_onedrive:
  cs-method: GET
  c-uri|endswith: \?manifest=wac
  cs-host: onedrive.live.com
filter_main_onedrive:
  c-uri|startswith: http
  c-uri|contains: ://onedrive.live.com/
condition: 1 of selection_* and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://github.com/rsmudge/Malleable-C2-Profiles/blob/26323784672913923d20c5a638c6ca79459e8529/normal/amazon.profile
- https://www.hybrid-analysis.com/sample/ee5eca8648e45e2fea9dac0d920ef1a1792d8690c41ee7f20343de1927cc88b9?environmentId=100
- https://github.com/rsmudge/Malleable-C2-Profiles/blob/26323784672913923d20c5a638c6ca79459e8529/normal/ocsp.profile
- https://github.com/yeyintminthuhtut/Malleable-C2-Profiles-Collection/
- https://github.com/rsmudge/Malleable-C2-Profiles/blob/26323784672913923d20c5a638c6ca79459e8529/normal/onedrive_getonly.profile

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/web/proxy_generic/proxy_hktl_cobalt_strike_malleable_c2_requests.yml)
