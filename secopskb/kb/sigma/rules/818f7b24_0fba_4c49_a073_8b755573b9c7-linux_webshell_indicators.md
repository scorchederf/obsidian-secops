---
sigma_id: "818f7b24-0fba-4c49-a073-8b755573b9c7"
title: "Linux Webshell Indicators"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_webshell_detection.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_webshell_detection.yml"
build_date: "2026-04-27 19:13:52"
status: "test"
level: "high"
logsource: "linux / process_creation"
aliases:
  - "818f7b24-0fba-4c49-a073-8b755573b9c7"
  - "Linux Webshell Indicators"
attack_technique_ids:
  - "T1505.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects suspicious sub processes of web server processes

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1505-server_software_component#^t1505003-web-shell|T1505.003: Web Shell]]

## Detection

```yaml
selection_general:
  ParentImage|endswith:
  - /httpd
  - /lighttpd
  - /nginx
  - /apache2
  - /node
  - /caddy
selection_tomcat:
  ParentCommandLine|contains|all:
  - /bin/java
  - tomcat
selection_websphere:
  ParentCommandLine|contains|all:
  - /bin/java
  - websphere
sub_processes:
  Image|endswith:
  - /whoami
  - /ifconfig
  - /ip
  - /bin/uname
  - /bin/cat
  - /bin/crontab
  - /hostname
  - /iptables
  - /netstat
  - /pwd
  - /route
condition: 1 of selection_* and sub_processes
```

## False Positives

- Web applications that invoke Linux command line tools

## References

- https://www.acunetix.com/blog/articles/web-shells-101-using-php-introduction-web-shells-part-2/
- https://media.defense.gov/2020/Jun/09/2002313081/-1/-1/0/CSI-DETECT-AND-PREVENT-WEB-SHELL-MALWARE-20200422.PDF

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_webshell_detection.yml)
