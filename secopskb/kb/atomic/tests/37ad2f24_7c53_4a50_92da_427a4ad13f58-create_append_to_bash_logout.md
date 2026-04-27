---
atomic_guid: "37ad2f24-7c53-4a50-92da-427a4ad13f58"
title: "Create/Append to .bash_logout"
framework: "atomic"
generated: "true"
attack_technique_id: "T1546.004"
attack_technique_name: "Event Triggered Execution: .bash_profile .bashrc and .shrc"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.004/T1546.004.yaml"
build_date: "2026-04-27 19:12:27"
executor: "bash"
aliases:
  - "37ad2f24-7c53-4a50-92da-427a4ad13f58"
  - "Create/Append to .bash_logout"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

The Bash shell runs ~/.bash_logout "if it exists" to run commands on user logout. An adversary may create or append to a .bash_logout to clear history, start processes etc. Note the ~/.bash_logout is only run if you explicitly exit or log out of an "interactive login shell session" i.e. via the console, SSH, /bin/bash -l or su -l <username>. 

This test creates the art user, logs in, creates a .bash_logout which will echo some text into the art.txt file on logout and logs out and the /home/art/art.txt is created.

## ATT&CK Mapping

- [[kb/attack/techniques/T1546-event_triggered_execution#^t1546004-unix-shell-configuration-modification|T1546.004: Unix Shell Configuration Modification]]

## Executor

- elevation_required: True
- name: bash

### Command

```bash
useradd --create-home --shell /bin/bash art
su -l art -c "echo 'echo \"Atomic Red Team was here... T1546.004\" >> /home/art/art.txt' >> /home/art/.bash_logout; exit"
```

### Cleanup

```bash
userdel -fr art
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.004/T1546.004.yaml)
