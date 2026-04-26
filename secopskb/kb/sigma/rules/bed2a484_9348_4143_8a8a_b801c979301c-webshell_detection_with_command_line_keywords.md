---
sigma_id: "bed2a484-9348-4143-8a8a-b801c979301c"
title: "Webshell Detection With Command Line Keywords"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_webshell_recon_commands_and_processes.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_webshell_recon_commands_and_processes.yml"
build_date: "2026-04-26 17:03:24"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "bed2a484-9348-4143-8a8a-b801c979301c"
  - "Webshell Detection With Command Line Keywords"
attack_technique_ids:
  - "T1505.003"
  - "T1018"
  - "T1033"
  - "T1087"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Webshell Detection With Command Line Keywords

Detects certain command line parameters often used during reconnaissance activity via web shells

## Metadata

- Rule ID: bed2a484-9348-4143-8a8a-b801c979301c
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems), Jonhnathan Ribeiro, Anton Kutepov, oscd.community, Chad Hudson, Matt Anderson
- Date: 2017-01-01
- Modified: 2024-12-14
- Source Path: rules/windows/process_creation/proc_creation_win_webshell_recon_commands_and_processes.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1505-server_software_component|T1505.003]]
- [[kb/attack/techniques/T1018-remote_system_discovery|T1018]]
- [[kb/attack/techniques/T1033-system_owner_user_discovery|T1033]]
- [[kb/attack/techniques/T1087-account_discovery|T1087]]

## Detection

```yaml
selection_webserver_image:
  ParentImage|endswith:
  - \w3wp.exe
  - \php-cgi.exe
  - \nginx.exe
  - \httpd.exe
  - \caddy.exe
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
selection_susp_net_utility:
  OriginalFileName:
  - net.exe
  - net1.exe
  CommandLine|contains:
  - ' user '
  - ' use '
  - ' group '
selection_susp_ping_utility:
  OriginalFileName: ping.exe
  CommandLine|contains: ' -n '
selection_susp_change_dir:
  CommandLine|contains:
  - '&cd&echo'
  - 'cd /d '
selection_susp_wmic_utility:
  OriginalFileName: wmic.exe
  CommandLine|contains: ' /node:'
selection_susp_powershell_cli:
  Image|endswith:
  - \cmd.exe
  - \powershell.exe
  - \pwsh.exe
  CommandLine|contains:
  - ' -enc '
  - ' -EncodedCommand '
  - ' -w hidden '
  - ' -windowstyle hidden'
  - .WebClient).Download
selection_susp_misc_discovery_binaries:
- Image|endswith:
  - \dsquery.exe
  - \find.exe
  - \findstr.exe
  - \ipconfig.exe
  - \netstat.exe
  - \nslookup.exe
  - \pathping.exe
  - \quser.exe
  - \schtasks.exe
  - \systeminfo.exe
  - \tasklist.exe
  - \tracert.exe
  - \ver.exe
  - \wevtutil.exe
  - \whoami.exe
- OriginalFileName:
  - dsquery.exe
  - find.exe
  - findstr.exe
  - ipconfig.exe
  - netstat.exe
  - nslookup.exe
  - pathping.exe
  - quser.exe
  - schtasks.exe
  - sysinfo.exe
  - tasklist.exe
  - tracert.exe
  - ver.exe
  - VSSADMIN.EXE
  - wevtutil.exe
  - whoami.exe
selection_susp_misc_discovery_commands:
  CommandLine|contains:
  - ' Test-NetConnection '
  - dir \
condition: 1 of selection_webserver_* and 1 of selection_susp_*
```

## False Positives

- Unknown

## References

- https://www.fireeye.com/blog/threat-research/2013/08/breaking-down-the-china-chopper-web-shell-part-ii.html
- https://unit42.paloaltonetworks.com/bumblebee-webshell-xhunt-campaign/
- https://www.huntress.com/blog/threat-advisory-oh-no-cleo-cleo-software-actively-being-exploited-in-the-wild

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_webshell_recon_commands_and_processes.yml)
