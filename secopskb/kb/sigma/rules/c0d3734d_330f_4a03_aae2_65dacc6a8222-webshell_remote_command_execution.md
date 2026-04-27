---
sigma_id: "c0d3734d-330f-4a03-aae2-65dacc6a8222"
title: "Webshell Remote Command Execution"
framework: "sigma"
generated: "true"
source_path: "rules/linux/auditd/syscall/lnx_auditd_web_rce.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/syscall/lnx_auditd_web_rce.yml"
build_date: "2026-04-27 19:13:59"
status: "test"
level: "critical"
logsource: "linux / auditd"
aliases:
  - "c0d3734d-330f-4a03-aae2-65dacc6a8222"
  - "Webshell Remote Command Execution"
attack_technique_ids:
  - "T1505.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects possible command execution by web application/web shell

## Logsource

- definition: Required auditd configuration:
-a always,exit -F arch=b32 -S execve -F euid=33 -k detect_execve_www
-a always,exit -F arch=b64 -S execve -F euid=33 -k detect_execve_www
-a always,exit -F arch=b32 -S execveat -F euid=33 -k detect_execve_www
-a always,exit -F arch=b64 -S execveat -F euid=33 -k detect_execve_www
Change the number "33" to the ID of your WebServer user. Default: www-data:x:33:33

- product: linux
- service: auditd

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1505-server_software_component#^t1505003-web-shell|T1505.003: Web Shell]]

## Detection

```yaml
selection:
  type: SYSCALL
  SYSCALL:
  - execve
  - execveat
  euid: 33
condition: selection
```

## False Positives

- Admin activity
- Crazy web applications

## References

- Personal Experience of the Author
- https://www.vaadata.com/blog/what-is-command-injection-exploitations-and-security-best-practices/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/syscall/lnx_auditd_web_rce.yml)
