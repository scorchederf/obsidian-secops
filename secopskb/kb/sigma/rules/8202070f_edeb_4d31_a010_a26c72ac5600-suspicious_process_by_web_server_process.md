---
sigma_id: "8202070f-edeb-4d31-a010-a26c72ac5600"
title: "Suspicious Process By Web Server Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_webshell_susp_process_spawned_from_webserver.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_webshell_susp_process_spawned_from_webserver.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "8202070f-edeb-4d31-a010-a26c72ac5600"
  - "Suspicious Process By Web Server Process"
attack_technique_ids:
  - "T1505.003"
  - "T1190"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Process By Web Server Process

Detects potentially suspicious processes being spawned by a web server process which could be the result of a successfully placed web shell or exploitation

## Metadata

- Rule ID: 8202070f-edeb-4d31-a010-a26c72ac5600
- Status: test
- Level: high
- Author: Thomas Patzke, Florian Roth (Nextron Systems), Zach Stanford @svch0st, Tim Shelton, Nasreddine Bencherchali (Nextron Systems)
- Date: 2019-01-16
- Modified: 2024-11-26
- Source Path: rules/windows/process_creation/proc_creation_win_webshell_susp_process_spawned_from_webserver.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1505-server_software_component|T1505.003]]
- [[kb/attack/techniques/T1190-exploit_public-facing_application|T1190]]

## Detection

```yaml
selection_webserver_image:
  ParentImage|endswith:
  - \caddy.exe
  - \httpd.exe
  - \nginx.exe
  - \php-cgi.exe
  - \php.exe
  - \tomcat.exe
  - \UMWorkerProcess.exe
  - \w3wp.exe
  - \ws_TomcatService.exe
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
  ParentCommandLine|contains:
  - CATALINA_HOME
  - catalina.home
  - catalina.jar
selection_anomaly_children:
  Image|endswith:
  - \arp.exe
  - \at.exe
  - \bash.exe
  - \bitsadmin.exe
  - \certutil.exe
  - \cmd.exe
  - \cscript.exe
  - \dsget.exe
  - \hostname.exe
  - \nbtstat.exe
  - \net.exe
  - \net1.exe
  - \netdom.exe
  - \netsh.exe
  - \nltest.exe
  - \ntdsutil.exe
  - \powershell_ise.exe
  - \powershell.exe
  - \pwsh.exe
  - \qprocess.exe
  - \query.exe
  - \qwinsta.exe
  - \reg.exe
  - \rundll32.exe
  - \sc.exe
  - \sh.exe
  - \wmic.exe
  - \wscript.exe
  - \wusa.exe
filter_main_fp_1:
  ParentImage|endswith: \java.exe
  CommandLine|endswith: Windows\system32\cmd.exe /c C:\ManageEngine\ADManager "Plus\ES\bin\elasticsearch.bat
    -Enode.name=RMP-NODE1 -pelasticsearch-pid.txt
filter_main_fp_2:
  ParentImage|endswith: \java.exe
  CommandLine|contains|all:
  - sc query
  - ADManager Plus
condition: 1 of selection_webserver_* and selection_anomaly_children and not 1 of
  filter_main_*
```

## False Positives

- Particular web applications may spawn a shell process legitimately

## References

- https://media.defense.gov/2020/Jun/09/2002313081/-1/-1/0/CSI-DETECT-AND-PREVENT-WEB-SHELL-MALWARE-20200422.PDF

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_webshell_susp_process_spawned_from_webserver.yml)
