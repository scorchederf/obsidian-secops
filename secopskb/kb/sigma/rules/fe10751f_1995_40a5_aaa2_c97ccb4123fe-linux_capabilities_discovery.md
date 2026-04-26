---
sigma_id: "fe10751f-1995-40a5-aaa2-c97ccb4123fe"
title: "Linux Capabilities Discovery"
framework: "sigma"
generated: "true"
source_path: "rules/linux/auditd/execve/lnx_auditd_capabilities_discovery.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/execve/lnx_auditd_capabilities_discovery.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "low"
logsource: "linux / auditd"
aliases:
  - "fe10751f-1995-40a5-aaa2-c97ccb4123fe"
  - "Linux Capabilities Discovery"
attack_technique_ids:
  - "T1083"
  - "T1548"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Linux Capabilities Discovery

Detects attempts to discover the files with setuid/setgid capability on them. That would allow adversary to escalate their privileges.

## Metadata

- Rule ID: fe10751f-1995-40a5-aaa2-c97ccb4123fe
- Status: test
- Level: low
- Author: Pawel Mazur
- Date: 2021-11-28
- Modified: 2022-12-25
- Source Path: rules/linux/auditd/execve/lnx_auditd_capabilities_discovery.yml

## Logsource

- product: linux
- service: auditd

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1083-file_and_directory_discovery|T1083]]
- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548]]

## Detection

```yaml
selection:
  type: EXECVE
  a0: getcap
  a1: -r
  a2: /
condition: selection
```

## False Positives

- Unknown

## References

- https://man7.org/linux/man-pages/man8/getcap.8.html
- https://www.hackingarticles.in/linux-privilege-escalation-using-capabilities/
- https://mn3m.info/posts/suid-vs-capabilities/
- https://int0x33.medium.com/day-44-linux-capabilities-privilege-escalation-via-openssl-with-selinux-enabled-and-enforced-74d2bec02099

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/execve/lnx_auditd_capabilities_discovery.yml)
