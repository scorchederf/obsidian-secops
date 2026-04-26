---
sigma_id: "a39d7fa7-3fbd-4dc2-97e1-d87f546b1bbc"
title: "Program Executions in Suspicious Folders"
framework: "sigma"
generated: "true"
source_path: "rules/linux/auditd/syscall/lnx_auditd_susp_exe_folders.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/syscall/lnx_auditd_susp_exe_folders.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "linux / auditd"
aliases:
  - "a39d7fa7-3fbd-4dc2-97e1-d87f546b1bbc"
  - "Program Executions in Suspicious Folders"
attack_technique_ids:
  - "T1587"
  - "T1584"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Program Executions in Suspicious Folders

Detects program executions in suspicious non-program folders related to malware or hacking activity

## Metadata

- Rule ID: a39d7fa7-3fbd-4dc2-97e1-d87f546b1bbc
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2018-01-23
- Modified: 2021-11-27
- Source Path: rules/linux/auditd/syscall/lnx_auditd_susp_exe_folders.yml

## Logsource

- product: linux
- service: auditd

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1587-develop_capabilities|T1587]]
- [[kb/attack/techniques/T1584-compromise_infrastructure|T1584]]

## Detection

```yaml
selection:
  type: SYSCALL
  exe|startswith:
  - /tmp/
  - /var/www/
  - /home/*/public_html/
  - /usr/local/apache2/
  - /usr/local/httpd/
  - /var/apache/
  - /srv/www/
  - /home/httpd/html/
  - /srv/http/
  - /usr/share/nginx/html/
  - /var/lib/pgsql/data/
  - /usr/local/mysql/data/
  - /var/lib/mysql/
  - /var/vsftpd/
  - /etc/bind/
  - /var/named/
condition: selection
```

## False Positives

- Admin activity (especially in /tmp folders)
- Crazy web applications

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/syscall/lnx_auditd_susp_exe_folders.yml)
