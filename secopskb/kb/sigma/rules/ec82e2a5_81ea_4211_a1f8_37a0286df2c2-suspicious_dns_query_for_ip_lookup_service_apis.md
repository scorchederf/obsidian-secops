---
sigma_id: "ec82e2a5-81ea-4211-a1f8-37a0286df2c2"
title: "Suspicious DNS Query for IP Lookup Service APIs"
framework: "sigma"
generated: "true"
source_path: "rules/windows/dns_query/dns_query_win_susp_external_ip_lookup.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/dns_query/dns_query_win_susp_external_ip_lookup.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "windows / dns_query"
aliases:
  - "ec82e2a5-81ea-4211-a1f8-37a0286df2c2"
  - "Suspicious DNS Query for IP Lookup Service APIs"
attack_technique_ids:
  - "T1590"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious DNS Query for IP Lookup Service APIs

Detects DNS queries for IP lookup services such as "api.ipify.org" originating from a non browser process.

## Metadata

- Rule ID: ec82e2a5-81ea-4211-a1f8-37a0286df2c2
- Status: test
- Level: medium
- Author: Brandon George (blog post), Thomas Patzke
- Date: 2021-07-08
- Modified: 2024-03-22
- Source Path: rules/windows/dns_query/dns_query_win_susp_external_ip_lookup.yml

## Logsource

- category: dns_query
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1590-gather_victim_network_information|T1590]]

## Detection

```yaml
selection:
- QueryName:
  - www.ip.cn
  - l2.io
- QueryName|contains:
  - api.2ip.ua
  - api.bigdatacloud.net
  - api.ipify.org
  - bot.whatismyipaddress.com
  - canireachthe.net
  - checkip.amazonaws.com
  - checkip.dyndns.org
  - curlmyip.com
  - db-ip.com
  - edns.ip-api.com
  - eth0.me
  - freegeoip.app
  - geoipy.com
  - getip.pro
  - icanhazip.com
  - ident.me
  - ifconfig.io
  - ifconfig.me
  - ip-api.com
  - ip.360.cn
  - ip.anysrc.net
  - ip.taobao.com
  - ip.tyk.nu
  - ipaddressworld.com
  - ipapi.co
  - ipconfig.io
  - ipecho.net
  - ipinfo.io
  - ipip.net
  - ipof.in
  - ipv4.icanhazip.com
  - ipv4bot.whatismyipaddress.com
  - ipv6-test.com
  - ipwho.is
  - jsonip.com
  - myexternalip.com
  - seeip.org
  - wgetip.com
  - whatismyip.akamai.com
  - whois.pconline.com.cn
  - wtfismyip.com
filter_optional_brave:
  Image|endswith: \brave.exe
filter_optional_chrome:
  Image:
  - C:\Program Files\Google\Chrome\Application\chrome.exe
  - C:\Program Files (x86)\Google\Chrome\Application\chrome.exe
filter_optional_firefox:
  Image:
  - C:\Program Files\Mozilla Firefox\firefox.exe
  - C:\Program Files (x86)\Mozilla Firefox\firefox.exe
filter_optional_ie:
  Image:
  - C:\Program Files (x86)\Internet Explorer\iexplore.exe
  - C:\Program Files\Internet Explorer\iexplore.exe
filter_optional_maxthon:
  Image|endswith: \maxthon.exe
filter_optional_edge_1:
- Image|startswith: C:\Program Files (x86)\Microsoft\EdgeWebView\Application\
- Image|endswith: \WindowsApps\MicrosoftEdge.exe
- Image:
  - C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe
  - C:\Program Files\Microsoft\Edge\Application\msedge.exe
filter_optional_edge_2:
  Image|startswith:
  - C:\Program Files (x86)\Microsoft\EdgeCore\
  - C:\Program Files\Microsoft\EdgeCore\
  Image|endswith:
  - \msedge.exe
  - \msedgewebview2.exe
filter_optional_opera:
  Image|endswith: \opera.exe
filter_optional_safari:
  Image|endswith: \safari.exe
filter_optional_seamonkey:
  Image|endswith: \seamonkey.exe
filter_optional_vivaldi:
  Image|endswith: \vivaldi.exe
filter_optional_whale:
  Image|endswith: \whale.exe
condition: selection and not 1 of filter_optional_*
```

## False Positives

- Legitimate usage of IP lookup services such as ipify API

## References

- https://www.binarydefense.com/analysis-of-hancitor-when-boring-begets-beacon
- https://twitter.com/neonprimetime/status/1436376497980428318
- https://www.trendmicro.com/en_us/research/23/e/managed-xdr-investigation-of-ducktail-in-trend-micro-vision-one.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/dns_query/dns_query_win_susp_external_ip_lookup.yml)
