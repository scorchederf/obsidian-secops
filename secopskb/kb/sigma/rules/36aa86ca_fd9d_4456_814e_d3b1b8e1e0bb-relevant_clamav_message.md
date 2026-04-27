---
sigma_id: "36aa86ca-fd9d-4456-814e-d3b1b8e1e0bb"
title: "Relevant ClamAV Message"
framework: "sigma"
generated: "true"
source_path: "rules/linux/builtin/clamav/lnx_clamav_relevant_message.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/builtin/clamav/lnx_clamav_relevant_message.yml"
build_date: "2026-04-26 17:03:21"
status: "stable"
level: "high"
logsource: "linux / clamav"
aliases:
  - "36aa86ca-fd9d-4456-814e-d3b1b8e1e0bb"
  - "Relevant ClamAV Message"
attack_technique_ids:
  - "T1588.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Relevant ClamAV Message

Detects relevant ClamAV messages

## Metadata

- Rule ID: 36aa86ca-fd9d-4456-814e-d3b1b8e1e0bb
- Status: stable
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2017-03-01
- Source Path: rules/linux/builtin/clamav/lnx_clamav_relevant_message.yml

## Logsource

- product: linux
- service: clamav

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1588-obtain_capabilities|T1588.001]]

## Detection

```yaml
keywords:
- Trojan*FOUND
- VirTool*FOUND
- Webshell*FOUND
- Rootkit*FOUND
- Htran*FOUND
condition: keywords
```

## False Positives

- Unknown

## References

- https://github.com/ossec/ossec-hids/blob/1ecffb1b884607cb12e619f9ab3c04f530801083/etc/rules/clam_av_rules.xml

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/builtin/clamav/lnx_clamav_relevant_message.yml)
