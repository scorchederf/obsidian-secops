---
sigma_id: "4922a5dd-6743-4fc2-8e81-144374280997"
title: "Flash Player Update from Suspicious Location"
framework: "sigma"
generated: "true"
source_path: "rules/web/proxy_generic/proxy_susp_flash_download_loc.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/web/proxy_generic/proxy_susp_flash_download_loc.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "proxy"
aliases:
  - "4922a5dd-6743-4fc2-8e81-144374280997"
  - "Flash Player Update from Suspicious Location"
attack_technique_ids:
  - "T1189"
  - "T1204.002"
  - "T1036.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Flash Player Update from Suspicious Location

Detects a flashplayer update from an unofficial location

## Metadata

- Rule ID: 4922a5dd-6743-4fc2-8e81-144374280997
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2017-10-25
- Modified: 2022-08-08
- Source Path: rules/web/proxy_generic/proxy_susp_flash_download_loc.yml

## Logsource

- category: proxy

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1189-drive-by_compromise|T1189]]
- [[kb/attack/techniques/T1204-user_execution|T1204.002]]
- [[kb/attack/techniques/T1036-masquerading|T1036.005]]

## Detection

```yaml
selection:
- c-uri|contains: /flash_install.php
- c-uri|endswith: /install_flash_player.exe
filter:
  cs-host|endswith: .adobe.com
condition: selection and not filter
```

## False Positives

- Unknown flash download locations

## References

- https://gist.github.com/roycewilliams/a723aaf8a6ac3ba4f817847610935cfb

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/web/proxy_generic/proxy_susp_flash_download_loc.yml)
