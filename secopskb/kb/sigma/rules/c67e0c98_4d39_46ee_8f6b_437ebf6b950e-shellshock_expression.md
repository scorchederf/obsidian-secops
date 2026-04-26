---
sigma_id: "c67e0c98-4d39-46ee-8f6b-437ebf6b950e"
title: "Shellshock Expression"
framework: "sigma"
generated: "true"
source_path: "rules/linux/builtin/lnx_shellshock.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/builtin/lnx_shellshock.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "high"
logsource: "linux"
aliases:
  - "c67e0c98-4d39-46ee-8f6b-437ebf6b950e"
  - "Shellshock Expression"
attack_technique_ids:
  - "T1505.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Shellshock Expression

Detects shellshock expressions in log files

## Metadata

- Rule ID: c67e0c98-4d39-46ee-8f6b-437ebf6b950e
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2017-03-14
- Modified: 2022-10-09
- Source Path: rules/linux/builtin/lnx_shellshock.yml

## Logsource

- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1505-server_software_component|T1505.003]]

## Detection

```yaml
keywords:
- (){:;};
- () {:;};
- () { :;};
- () { :; };
condition: keywords
```

## False Positives

- Unknown

## References

- https://owasp.org/www-pdf-archive/Shellshock_-_Tudor_Enache.pdf

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/builtin/lnx_shellshock.yml)
