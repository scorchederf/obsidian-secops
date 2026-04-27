---
sigma_id: "e09eb557-96d2-4de9-ba2d-30f712a5afd3"
title: "Commands to Clear or Remove the Syslog - Builtin"
framework: "sigma"
generated: "true"
source_path: "rules/linux/builtin/lnx_clear_syslog.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/builtin/lnx_clear_syslog.yml"
build_date: "2026-04-27 19:13:50"
status: "test"
level: "high"
logsource: "linux"
aliases:
  - "e09eb557-96d2-4de9-ba2d-30f712a5afd3"
  - "Commands to Clear or Remove the Syslog - Builtin"
attack_technique_ids:
  - "T1565.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects specific commands commonly used to remove or empty the syslog

## Logsource

- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1565-data_manipulation#^t1565001-stored-data-manipulation|T1565.001: Stored Data Manipulation]]

## Detection

```yaml
selection:
- rm /var/log/syslog
- rm -r /var/log/syslog
- rm -f /var/log/syslog
- rm -rf /var/log/syslog
- mv /var/log/syslog
- ' >/var/log/syslog'
- ' > /var/log/syslog'
falsepositives:
- /syslog.
condition: selection and not falsepositives
```

## False Positives

- Log rotation

## References

- https://www.virustotal.com/gui/file/fc614fb4bda24ae8ca2c44e812d12c0fab6dd7a097472a35dd12ded053ab8474

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/builtin/lnx_clear_syslog.yml)
