---
sigma_id: "c64c5175-5189-431b-a55e-6d9882158251"
title: "Telegram Bot API Request"
framework: "sigma"
generated: "true"
source_path: "rules/network/dns/net_dns_susp_telegram_api.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/network/dns/net_dns_susp_telegram_api.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "dns"
aliases:
  - "c64c5175-5189-431b-a55e-6d9882158251"
  - "Telegram Bot API Request"
attack_technique_ids:
  - "T1102.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Telegram Bot API Request

Detects suspicious DNS queries to api.telegram.org used by Telegram Bots of any kind

## Metadata

- Rule ID: c64c5175-5189-431b-a55e-6d9882158251
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2018-06-05
- Modified: 2022-10-09
- Source Path: rules/network/dns/net_dns_susp_telegram_api.yml

## Logsource

- category: dns

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1102-web_service|T1102.002]]

## Detection

```yaml
selection:
  query: api.telegram.org
condition: selection
```

## False Positives

- Legitimate use of Telegram bots in the company

## References

- https://core.telegram.org/bots/faq
- https://researchcenter.paloaltonetworks.com/2018/03/unit42-telerat-another-android-trojan-leveraging-telegrams-bot-api-to-target-iranian-users/
- https://blog.malwarebytes.com/threat-analysis/2016/11/telecrypt-the-ransomware-abusing-telegram-api-defeated/
- https://www.welivesecurity.com/2016/12/13/rise-telebots-analyzing-disruptive-killdisk-attacks/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/network/dns/net_dns_susp_telegram_api.yml)
