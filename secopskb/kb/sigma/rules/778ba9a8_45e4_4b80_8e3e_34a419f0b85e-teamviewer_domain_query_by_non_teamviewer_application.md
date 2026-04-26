---
sigma_id: "778ba9a8-45e4-4b80-8e3e-34a419f0b85e"
title: "TeamViewer Domain Query By Non-TeamViewer Application"
framework: "sigma"
generated: "true"
source_path: "rules/windows/dns_query/dns_query_win_teamviewer_domain_query_by_uncommon_app.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/dns_query/dns_query_win_teamviewer_domain_query_by_uncommon_app.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / dns_query"
aliases:
  - "778ba9a8-45e4-4b80-8e3e-34a419f0b85e"
  - "TeamViewer Domain Query By Non-TeamViewer Application"
attack_technique_ids:
  - "T1219.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# TeamViewer Domain Query By Non-TeamViewer Application

Detects DNS queries to a TeamViewer domain only resolved by a TeamViewer client by an image that isn't named TeamViewer (sometimes used by threat actors for obfuscation)

## Metadata

- Rule ID: 778ba9a8-45e4-4b80-8e3e-34a419f0b85e
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2022-01-30
- Modified: 2023-09-18
- Source Path: rules/windows/dns_query/dns_query_win_teamviewer_domain_query_by_uncommon_app.yml

## Logsource

- category: dns_query
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1219-remote_access_tools|T1219.002]]

## Detection

```yaml
selection:
  QueryName:
  - taf.teamviewer.com
  - udp.ping.teamviewer.com
filter_main_teamviewer:
  Image|contains: TeamViewer
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown binary names of TeamViewer
- Depending on the environment the rule might require some initial tuning before usage to avoid FP with third party applications

## References

- https://www.teamviewer.com/en-us/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/dns_query/dns_query_win_teamviewer_domain_query_by_uncommon_app.yml)
