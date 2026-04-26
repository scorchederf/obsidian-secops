---
sigma_id: "19aa4f58-94ca-45ff-bc34-92e533c0994a"
title: "Suspicious User-Agents Related To Recon Tools"
framework: "sigma"
generated: "true"
source_path: "rules/web/webserver_generic/web_susp_useragents.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/web/webserver_generic/web_susp_useragents.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "webserver"
aliases:
  - "19aa4f58-94ca-45ff-bc34-92e533c0994a"
  - "Suspicious User-Agents Related To Recon Tools"
attack_technique_ids:
  - "T1190"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious User-Agents Related To Recon Tools

Detects known suspicious (default) user-agents related to scanning/recon tools

## Metadata

- Rule ID: 19aa4f58-94ca-45ff-bc34-92e533c0994a
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems), Tim Shelton
- Date: 2022-07-19
- Modified: 2023-01-02
- Source Path: rules/web/webserver_generic/web_susp_useragents.yml

## Logsource

- category: webserver

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1190-exploit_public-facing_application|T1190]]

## Detection

```yaml
selection:
  cs-user-agent|contains:
  - Wfuzz/
  - WPScan v
  - Recon-ng/v
  - GIS - AppSec Team - Project Vision
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/wpscanteam/wpscan/blob/196fbab5b1ce3870a43515153d4f07878a89d410/lib/wpscan/browser.rb
- https://github.com/xmendez/wfuzz/blob/1b695ee9a87d66a7d7bf6cae70d60a33fae51541/docs/user/basicusage.rst
- https://github.com/lanmaster53/recon-ng/blob/9e907dfe09fce2997f0301d746796408e01a60b7/recon/core/base.py#L92

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/web/webserver_generic/web_susp_useragents.yml)
