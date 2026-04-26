---
sigma_id: "fa935401-513b-467b-81f4-f9e77aa0dd78"
title: "Crypto Miner User Agent"
framework: "sigma"
generated: "true"
source_path: "rules/web/proxy_generic/proxy_ua_cryptominer.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/web/proxy_generic/proxy_ua_cryptominer.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "proxy"
aliases:
  - "fa935401-513b-467b-81f4-f9e77aa0dd78"
  - "Crypto Miner User Agent"
attack_technique_ids:
  - "T1071.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Crypto Miner User Agent

Detects suspicious user agent strings used by crypto miners in proxy logs

## Metadata

- Rule ID: fa935401-513b-467b-81f4-f9e77aa0dd78
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2019-10-21
- Modified: 2021-11-27
- Source Path: rules/web/proxy_generic/proxy_ua_cryptominer.yml

## Logsource

- category: proxy

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1071-application_layer_protocol|T1071.001]]

## Detection

```yaml
selection:
  c-useragent|startswith:
  - 'XMRig '
  - ccminer
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/xmrig/xmrig/blob/da22b3e6c45825f3ac1f208255126cb8585cd4fc/src/base/kernel/Platform_win.cpp#L65
- https://github.com/xmrig/xmrig/blob/427b6516e0550200c17ca28675118f0fffcc323f/src/version.h

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/web/proxy_generic/proxy_ua_cryptominer.yml)
