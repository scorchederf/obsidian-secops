---
sigma_id: "f64e5c19-879c-4bae-b471-6d84c8339677"
title: "Webshell Tool Reconnaissance Activity"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_webshell_tool_recon.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_webshell_tool_recon.yml"
build_date: "2026-04-26 17:03:24"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "f64e5c19-879c-4bae-b471-6d84c8339677"
  - "Webshell Tool Reconnaissance Activity"
attack_technique_ids:
  - "T1505.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Webshell Tool Reconnaissance Activity

Detects processes spawned from web servers (PHP, Tomcat, IIS, etc.) that perform reconnaissance looking for the existence of popular scripting tools (perl, python, wget) on the system via the help commands

## Metadata

- Rule ID: f64e5c19-879c-4bae-b471-6d84c8339677
- Status: test
- Level: high
- Author: Cian Heasley, Florian Roth (Nextron Systems)
- Date: 2020-07-22
- Modified: 2023-11-09
- Source Path: rules/windows/process_creation/proc_creation_win_webshell_tool_recon.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1505-server_software_component|T1505.003]]

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
  - CATALINA_HOME
  - catalina.jar
selection_recon:
  CommandLine|contains:
  - perl --help
  - perl -h
  - python --help
  - python -h
  - python3 --help
  - python3 -h
  - wget --help
condition: 1 of selection_webserver_* and selection_recon
```

## False Positives

- Unknown

## References

- https://ragged-lab.blogspot.com/2020/07/webshells-automating-reconnaissance.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_webshell_tool_recon.yml)
