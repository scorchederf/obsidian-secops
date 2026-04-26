---
sigma_id: "a94cdd87-6c54-4678-a6cc-2814ffe5a13d"
title: "Unix Shell Configuration Modification"
framework: "sigma"
generated: "true"
source_path: "rules/linux/auditd/path/lnx_auditd_unix_shell_configuration_modification.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/path/lnx_auditd_unix_shell_configuration_modification.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "linux / auditd"
aliases:
  - "a94cdd87-6c54-4678-a6cc-2814ffe5a13d"
  - "Unix Shell Configuration Modification"
attack_technique_ids:
  - "T1546.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Unix Shell Configuration Modification

Detect unix shell configuration modification. Adversaries may establish persistence through executing malicious commands triggered when a new shell is opened.

## Metadata

- Rule ID: a94cdd87-6c54-4678-a6cc-2814ffe5a13d
- Status: test
- Level: medium
- Author: Peter Matkovski, IAI
- Date: 2023-03-06
- Modified: 2023-03-15
- Source Path: rules/linux/auditd/path/lnx_auditd_unix_shell_configuration_modification.yml

## Logsource

- product: linux
- service: auditd

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.004]]

## Detection

```yaml
selection:
  type: PATH
  name:
  - /etc/shells
  - /etc/profile
  - /etc/profile.d/*
  - /etc/bash.bashrc
  - /etc/bashrc
  - /etc/zsh/zprofile
  - /etc/zsh/zshrc
  - /etc/zsh/zlogin
  - /etc/zsh/zlogout
  - /etc/csh.cshrc
  - /etc/csh.login
  - /root/.bashrc
  - /root/.bash_profile
  - /root/.profile
  - /root/.zshrc
  - /root/.zprofile
  - /home/*/.bashrc
  - /home/*/.zshrc
  - /home/*/.bash_profile
  - /home/*/.zprofile
  - /home/*/.profile
  - /home/*/.bash_login
  - /home/*/.bash_logout
  - /home/*/.zlogin
  - /home/*/.zlogout
condition: selection
```

## False Positives

- Admin or User activity are expected to generate some false positives

## References

- https://objective-see.org/blog/blog_0x68.html
- https://web.archive.org/web/20221204161143/https://www.glitch-cat.com/p/green-lambert-and-attack
- https://www.anomali.com/blog/pulling-linux-rabbit-rabbot-malware-out-of-a-hat

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/auditd/path/lnx_auditd_unix_shell_configuration_modification.yml)
