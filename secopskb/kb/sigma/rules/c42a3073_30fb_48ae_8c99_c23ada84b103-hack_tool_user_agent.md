---
sigma_id: "c42a3073-30fb-48ae-8c99-c23ada84b103"
title: "Hack Tool User Agent"
framework: "sigma"
generated: "true"
source_path: "rules/web/proxy_generic/proxy_ua_hacktool.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/web/proxy_generic/proxy_ua_hacktool.yml"
build_date: "2026-04-26 14:14:26"
status: "test"
level: "high"
logsource: "proxy"
aliases:
  - "c42a3073-30fb-48ae-8c99-c23ada84b103"
  - "Hack Tool User Agent"
attack_technique_ids:
  - "T1190"
  - "T1110"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Hack Tool User Agent

Detects suspicious user agent strings user by hack tools in proxy logs

## Metadata

- Rule ID: c42a3073-30fb-48ae-8c99-c23ada84b103
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2017-07-08
- Modified: 2022-07-07
- Source Path: rules/web/proxy_generic/proxy_ua_hacktool.yml

## Logsource

- category: proxy

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1190-exploit_public-facing_application|T1190]]
- [[kb/attack/techniques/T1110-brute_force|T1110]]

## Detection

```yaml
selection:
  c-useragent|contains:
  - (hydra)
  - ' arachni/'
  - ' BFAC '
  - ' brutus '
  - ' cgichk '
  - core-project/1.0
  - ' crimscanner/'
  - datacha0s
  - dirbuster
  - domino hunter
  - dotdotpwn
  - FHScan Core
  - floodgate
  - get-minimal
  - gootkit auto-rooter scanner
  - grendel-scan
  - ' inspath '
  - internet ninja
  - jaascois
  - ' zmeu '
  - masscan
  - ' metis '
  - morfeus fucking scanner
  - n-stealth
  - nsauditor
  - pmafind
  - security scan
  - springenwerk
  - teh forest lobster
  - toata dragostea
  - ' vega/'
  - voideye
  - webshag
  - webvulnscan
  - ' whcc/'
  - ' Havij'
  - absinthe
  - bsqlbf
  - mysqloit
  - pangolin
  - sql power injector
  - sqlmap
  - sqlninja
  - uil2pn
  - ruler
  - Mozilla/5.0 (Windows; U; Windows NT 5.1; pt-PT; rv:1.9.1.2) Gecko/20090729 Firefox/3.5.2
    (.NET CLR 3.5.30729)
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/fastly/waf_testbed/blob/8bfc406551f3045e418cbaad7596cff8da331dfc/templates/default/scanners-user-agents.data.erb
- http://rules.emergingthreats.net/open/snort-2.9.0/rules/emerging-user_agents.rules

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/web/proxy_generic/proxy_ua_hacktool.yml)
