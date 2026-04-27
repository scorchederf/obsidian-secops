---
sigma_id: "3eaf6218-3bed-4d8a-8707-274096f12a18"
title: "Wannacry Killswitch Domain"
framework: "sigma"
generated: "true"
source_path: "rules/network/dns/net_dns_wannacry_killswitch_domain.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/network/dns/net_dns_wannacry_killswitch_domain.yml"
build_date: "2026-04-27 19:13:59"
status: "test"
level: "high"
logsource: "dns"
aliases:
  - "3eaf6218-3bed-4d8a-8707-274096f12a18"
  - "Wannacry Killswitch Domain"
attack_technique_ids:
  - "T1071.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects wannacry killswitch domain dns queries

## Logsource

- category: dns

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1071-application_layer_protocol#^t1071001-web-protocols|T1071.001: Web Protocols]]

## Detection

```yaml
selection:
  query:
  - ifferfsodp9ifjaposdfjhgosurijfaewrwergwea.testing
  - ifferfsodp9ifjaposdfjhgosurijfaewrwergwea.test
  - ifferfsodp9ifjaposdfjhgosurijfaewrwergwea.com
  - ayylmaotjhsstasdfasdfasdfasdfasdfasdfasdf.com
  - iuqssfsodp9ifjaposdfjhgosurijfaewrwergwea.com
condition: selection
```

## False Positives

- Analyst testing

## References

- https://www.mandiant.com/resources/blog/wannacry-ransomware-campaign

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/network/dns/net_dns_wannacry_killswitch_domain.yml)
