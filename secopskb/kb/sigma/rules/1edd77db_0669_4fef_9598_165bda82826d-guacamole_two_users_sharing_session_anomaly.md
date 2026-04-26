---
sigma_id: "1edd77db-0669-4fef-9598-165bda82826d"
title: "Guacamole Two Users Sharing Session Anomaly"
framework: "sigma"
generated: "true"
source_path: "rules/linux/builtin/guacamole/lnx_guacamole_susp_guacamole.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/builtin/guacamole/lnx_guacamole_susp_guacamole.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "linux / guacamole"
aliases:
  - "1edd77db-0669-4fef-9598-165bda82826d"
  - "Guacamole Two Users Sharing Session Anomaly"
attack_technique_ids:
  - "T1212"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Guacamole Two Users Sharing Session Anomaly

Detects suspicious session with two users present

## Metadata

- Rule ID: 1edd77db-0669-4fef-9598-165bda82826d
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2020-07-03
- Modified: 2021-11-27
- Source Path: rules/linux/builtin/guacamole/lnx_guacamole_susp_guacamole.yml

## Logsource

- product: linux
- service: guacamole

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1212-exploitation_for_credential_access|T1212]]

## Detection

```yaml
selection:
- (2 users now present)
condition: selection
```

## False Positives

- Unknown

## References

- https://research.checkpoint.com/2020/apache-guacamole-rce/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/builtin/guacamole/lnx_guacamole_susp_guacamole.yml)
