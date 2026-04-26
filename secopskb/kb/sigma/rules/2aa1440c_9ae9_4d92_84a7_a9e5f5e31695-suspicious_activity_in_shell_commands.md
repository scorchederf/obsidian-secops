---
sigma_id: "2aa1440c-9ae9-4d92-84a7-a9e5f5e31695"
title: "Suspicious Activity in Shell Commands"
framework: "sigma"
generated: "true"
source_path: "rules/linux/builtin/lnx_shell_susp_commands.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/builtin/lnx_shell_susp_commands.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "high"
logsource: "linux"
aliases:
  - "2aa1440c-9ae9-4d92-84a7-a9e5f5e31695"
  - "Suspicious Activity in Shell Commands"
attack_technique_ids:
  - "T1059.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious Activity in Shell Commands

Detects suspicious shell commands used in various exploit codes (see references)

## Metadata

- Rule ID: 2aa1440c-9ae9-4d92-84a7-a9e5f5e31695
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2017-08-21
- Modified: 2021-11-27
- Source Path: rules/linux/builtin/lnx_shell_susp_commands.yml

## Logsource

- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.004]]

## Detection

```yaml
keywords:
- wget * - http* | perl
- wget * - http* | sh
- wget * - http* | bash
- python -m SimpleHTTPServer
- -m http.server
- import pty; pty.spawn*
- socat exec:*
- socat -O /tmp/*
- socat tcp-connect*
- '*echo binary >>*'
- '*wget *; chmod +x*'
- '*wget *; chmod 777 *'
- '*cd /tmp || cd /var/run || cd /mnt*'
- '*stop;service iptables stop;*'
- '*stop;SuSEfirewall2 stop;*'
- chmod 777 2020*
- '*>>/etc/rc.local'
- '*base64 -d /tmp/*'
- '* | base64 -d *'
- '*/chmod u+s *'
- '*chmod +s /tmp/*'
- '*chmod u+s /tmp/*'
- '* /tmp/haxhax*'
- '* /tmp/ns_sploit*'
- nc -l -p *
- cp /bin/ksh *
- cp /bin/sh *
- '* /tmp/*.b64 *'
- '*/tmp/ysocereal.jar*'
- '*/tmp/x *'
- '*; chmod +x /tmp/*'
- '*;chmod +x /tmp/*'
condition: keywords
```

## False Positives

- Unknown

## References

- https://web.archive.org/web/20170319121015/http://www.threatgeek.com/2017/03/widespread-exploitation-attempts-using-cve-2017-5638.html
- https://github.com/rapid7/metasploit-framework/blob/eb6535009f5fdafa954525687f09294918b5398d/modules/exploits/multi/http/struts_code_exec_exception_delegator.rb
- http://pastebin.com/FtygZ1cg
- https://artkond.com/2017/03/23/pivoting-guide/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/builtin/lnx_shell_susp_commands.yml)
