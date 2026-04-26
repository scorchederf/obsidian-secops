---
sigma_id: "edf3485d-dac4-4d50-90e4-b0e5813f7e60"
title: "Suspicious Network Connection to IP Lookup Service APIs"
framework: "sigma"
generated: "true"
source_path: "rules/windows/network_connection/net_connection_win_domain_external_ip_lookup.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_domain_external_ip_lookup.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "windows / network_connection"
aliases:
  - "edf3485d-dac4-4d50-90e4-b0e5813f7e60"
  - "Suspicious Network Connection to IP Lookup Service APIs"
attack_technique_ids:
  - "T1016"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Network Connection to IP Lookup Service APIs

Detects external IP address lookups by non-browser processes via services such as "api.ipify.org". This could be indicative of potential post compromise internet test activity.

## Metadata

- Rule ID: edf3485d-dac4-4d50-90e4-b0e5813f7e60
- Status: test
- Level: medium
- Author: Janantha Marasinghe, Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-04-24
- Modified: 2024-03-22
- Source Path: rules/windows/network_connection/net_connection_win_domain_external_ip_lookup.yml

## Logsource

- category: network_connection
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1016-system_network_configuration_discovery|T1016]]

## Detection

```yaml
selection:
- DestinationHostname:
  - www.ip.cn
  - l2.io
- DestinationHostname|contains:
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

- Legitimate use of the external websites for troubleshooting or network monitoring

## References

- https://github.com/rsp/scripts/blob/c8bb272d68164a9836e4f273d8f924927f39b8c6/externalip-benchmark.md
- https://www.cisa.gov/news-events/cybersecurity-advisories/aa20-302a
- https://thedfirreport.com/2022/11/28/emotet-strikes-again-lnk-file-leads-to-domain-wide-ransomware/
- https://www.trendmicro.com/en_us/research/23/e/managed-xdr-investigation-of-ducktail-in-trend-micro-vision-one.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_domain_external_ip_lookup.yml)
