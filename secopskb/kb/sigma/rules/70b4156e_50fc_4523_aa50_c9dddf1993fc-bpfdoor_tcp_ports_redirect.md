---
sigma_id: "70b4156e-50fc-4523-aa50-c9dddf1993fc"
title: "Bpfdoor TCP Ports Redirect"
framework: "sigma"
generated: "true"
source_path: "rules/linux/auditd/execve/lnx_auditd_bpfdoor_port_redirect.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/execve/lnx_auditd_bpfdoor_port_redirect.yml"
build_date: "2026-04-26 14:14:21"
status: "test"
level: "medium"
logsource: "linux / auditd"
aliases:
  - "70b4156e-50fc-4523-aa50-c9dddf1993fc"
  - "Bpfdoor TCP Ports Redirect"
attack_technique_ids:
  - "T1562.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Bpfdoor TCP Ports Redirect

All TCP traffic on particular port from attacker is routed to different port. ex. '/sbin/iptables -t nat -D PREROUTING -p tcp -s 192.168.1.1 --dport 22 -j REDIRECT --to-ports 42392'
The traffic looks like encrypted SSH communications going to TCP port 22, but in reality is being directed to the shell port once it hits the iptables rule for the attacker host only.

## Metadata

- Rule ID: 70b4156e-50fc-4523-aa50-c9dddf1993fc
- Status: test
- Level: medium
- Author: Rafal Piasecki
- Date: 2022-08-10
- Source Path: rules/linux/auditd/execve/lnx_auditd_bpfdoor_port_redirect.yml

## Logsource

- product: linux
- service: auditd

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.004]]

## Detection

```yaml
cmd:
  type: EXECVE
  a0|endswith: iptables
  a1: -t
  a2: nat
keywords:
- --to-ports 42
- --to-ports 43
condition: cmd and keywords
```

## False Positives

- Legitimate ports redirect

## References

- https://www.sandflysecurity.com/blog/bpfdoor-an-evasive-linux-backdoor-technical-analysis/
- https://www.elastic.co/security-labs/a-peek-behind-the-bpfdoor

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/execve/lnx_auditd_bpfdoor_port_redirect.yml)
