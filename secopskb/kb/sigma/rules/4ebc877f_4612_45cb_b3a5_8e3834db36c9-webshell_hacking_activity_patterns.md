---
sigma_id: "4ebc877f-4612-45cb-b3a5-8e3834db36c9"
title: "Webshell Hacking Activity Patterns"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_webshell_hacking.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_webshell_hacking.yml"
build_date: "2026-04-27 19:13:59"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "4ebc877f-4612-45cb-b3a5-8e3834db36c9"
  - "Webshell Hacking Activity Patterns"
attack_technique_ids:
  - "T1505.003"
  - "T1018"
  - "T1033"
  - "T1087"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects certain parent child patterns found in cases in which a web shell is used to perform certain credential dumping or exfiltration activities on a compromised system

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1505-server_software_component#^t1505003-web-shell|T1505.003: Web Shell]]
- [[kb/attack/techniques/T1018-remote_system_discovery|T1018: Remote System Discovery]]
- [[kb/attack/techniques/T1033-system_owner_user_discovery|T1033: System Owner/User Discovery]]
- [[kb/attack/techniques/T1087-account_discovery|T1087: Account Discovery]]

## Detection

```yaml
selection_webserver_image:
  ParentImage|endswith:
  - \caddy.exe
  - \httpd.exe
  - \nginx.exe
  - \php-cgi.exe
  - \w3wp.exe
  - \ws_tomcatservice.exe
selection_webserver_characteristics_tomcat1:
  ParentImage|endswith:
  - \java.exe
  - \javaw.exe
  ParentImage|contains:
  - -tomcat-
  - \tomcat
selection_webserver_characteristics_tomcat2:
  ParentImage|endswith:
  - \java.exe
  - \javaw.exe
  CommandLine|contains:
  - catalina.jar
  - CATALINA_HOME
selection_child_1:
  CommandLine|contains|all:
  - rundll32
  - comsvcs
selection_child_2:
  CommandLine|contains|all:
  - ' -hp'
  - ' a '
  - ' -m'
selection_child_3:
  CommandLine|contains|all:
  - net
  - ' user '
  - ' /add'
selection_child_4:
  CommandLine|contains|all:
  - net
  - ' localgroup '
  - ' administrators '
  - /add
selection_child_5:
  Image|endswith:
  - \ntdsutil.exe
  - \ldifde.exe
  - \adfind.exe
  - \procdump.exe
  - \Nanodump.exe
  - \vssadmin.exe
  - \fsutil.exe
selection_child_6:
  CommandLine|contains:
  - ' -decode '
  - ' -NoP '
  - ' -W Hidden '
  - ' /decode '
  - ' /ticket:'
  - ' sekurlsa'
  - .dmp full
  - .downloadfile(
  - .downloadstring(
  - FromBase64String
  - process call create
  - 'reg save '
  - whoami /priv
condition: 1 of selection_webserver_* and 1 of selection_child_*
```

## False Positives

- Unlikely

## References

- https://youtu.be/7aemGhaE9ds?t=641

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_webshell_hacking.yml)
