---
sigma_id: "1edd77db-0669-4fef-9598-165bda82826d"
title: "Guacamole Two Users Sharing Session Anomaly"
framework: "sigma"
generated: "true"
source_path: "rules/linux/builtin/guacamole/lnx_guacamole_susp_guacamole.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/builtin/guacamole/lnx_guacamole_susp_guacamole.yml"
build_date: "2026-04-27 19:13:51"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects suspicious session with two users present

## Logsource

- product: linux
- service: guacamole

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1212-exploitation_for_credential_access|T1212: Exploitation for Credential Access]]

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
