---
sigma_id: "cb39d16b-b3b6-4a7a-8222-1cf24b686ffc"
title: "Data Exfiltration with Wget"
framework: "sigma"
generated: "true"
source_path: "rules/linux/auditd/execve/lnx_auditd_data_exfil_wget.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/execve/lnx_auditd_data_exfil_wget.yml"
build_date: "2026-04-26 14:14:23"
status: "test"
level: "medium"
logsource: "linux / auditd"
aliases:
  - "cb39d16b-b3b6-4a7a-8222-1cf24b686ffc"
  - "Data Exfiltration with Wget"
attack_technique_ids:
  - "T1048.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Data Exfiltration with Wget

Detects attempts to post the file with the usage of wget utility.
The adversary can bypass the permission restriction with the misconfigured sudo permission for wget utility which could allow them to read files like /etc/shadow.

## Metadata

- Rule ID: cb39d16b-b3b6-4a7a-8222-1cf24b686ffc
- Status: test
- Level: medium
- Author: Pawel Mazur
- Date: 2021-11-18
- Modified: 2022-12-25
- Source Path: rules/linux/auditd/execve/lnx_auditd_data_exfil_wget.yml

## Logsource

- product: linux
- service: auditd

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1048-exfiltration_over_alternative_protocol|T1048.003]]

## Detection

```yaml
selection:
  type: EXECVE
  a0: wget
  a1|startswith: --post-file=
condition: selection
```

## False Positives

- Legitimate usage of wget utility to post a file

## References

- https://linux.die.net/man/1/wget
- https://gtfobins.github.io/gtfobins/wget/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/execve/lnx_auditd_data_exfil_wget.yml)
