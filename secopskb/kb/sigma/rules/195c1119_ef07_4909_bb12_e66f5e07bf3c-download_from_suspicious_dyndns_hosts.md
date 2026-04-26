---
sigma_id: "195c1119-ef07-4909-bb12-e66f5e07bf3c"
title: "Download from Suspicious Dyndns Hosts"
framework: "sigma"
generated: "true"
source_path: "rules/web/proxy_generic/proxy_download_susp_dyndns.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/web/proxy_generic/proxy_download_susp_dyndns.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "proxy"
aliases:
  - "195c1119-ef07-4909-bb12-e66f5e07bf3c"
  - "Download from Suspicious Dyndns Hosts"
attack_technique_ids:
  - "T1105"
  - "T1568"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Download from Suspicious Dyndns Hosts

Detects download of certain file types from hosts with dynamic DNS names (selected list)

## Metadata

- Rule ID: 195c1119-ef07-4909-bb12-e66f5e07bf3c
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2017-11-08
- Modified: 2023-05-18
- Source Path: rules/web/proxy_generic/proxy_download_susp_dyndns.yml

## Logsource

- category: proxy

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]
- [[kb/attack/techniques/T1568-dynamic_resolution|T1568]]

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
  - .hopto.org
  - .no-ip.org
  - .no-ip.info
  - .no-ip.biz
  - .no-ip.com
  - .noip.com
  - .ddns.name
  - .myftp.org
  - .myftp.biz
  - .serveblog.net
  - .servebeer.com
  - .servemp3.com
  - .serveftp.com
  - .servequake.com
  - .servehalflife.com
  - .servehttp.com
  - .servegame.com
  - .servepics.com
  - .myvnc.com
  - .ignorelist.com
  - .jkub.com
  - .dlinkddns.com
  - .jumpingcrab.com
  - .ddns.info
  - .mooo.com
  - .dns-dns.com
  - .strangled.net
  - .adultdns.net
  - .craftx.biz
  - .ddns01.com
  - .dns53.biz
  - .dnsapi.info
  - .dnsd.info
  - .dnsdynamic.com
  - .dnsdynamic.net
  - .dnsget.org
  - .fe100.net
  - .flashserv.net
  - .ftp21.net
  - .http01.com
  - .http80.info
  - .https443.com
  - .imap01.com
  - .kadm5.com
  - .mysq1.net
  - .ns360.info
  - .ntdll.net
  - .ole32.com
  - .proxy8080.com
  - .sql01.com
  - .ssh01.com
  - .ssh22.net
  - .tempors.com
  - .tftpd.net
  - .ttl60.com
  - .ttl60.org
  - .user32.com
  - .voip01.com
  - .wow64.net
  - .x64.me
  - .xns01.com
  - .dyndns.org
  - .dyndns.info
  - .dyndns.tv
  - .dyndns-at-home.com
  - .dnsomatic.com
  - .zapto.org
  - .webhop.net
  - .25u.com
  - .slyip.net
condition: selection
```

## False Positives

- Software downloads

## References

- https://www.alienvault.com/blogs/security-essentials/dynamic-dns-security-and-potential-threats

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/web/proxy_generic/proxy_download_susp_dyndns.yml)
