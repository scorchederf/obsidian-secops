---
atomic_guid: "a54d497e-8dbe-4558-9895-44944baa395f"
title: "Account Enumeration with LDAPDomainDump"
framework: "atomic"
generated: "true"
attack_technique_id: "T1087.002"
attack_technique_name: "Account Discovery: Domain Account"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1087.002/T1087.002.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "a54d497e-8dbe-4558-9895-44944baa395f"
  - "Account Enumeration with LDAPDomainDump"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Account Enumeration with LDAPDomainDump

This test uses LDAPDomainDump to perform account enumeration on a domain.
[Reference](https://securityonline.info/ldapdomaindump-active-directory-information-dumper-via-ldap/)

## Metadata

- Atomic GUID: a54d497e-8dbe-4558-9895-44944baa395f
- Technique: T1087.002: Account Discovery: Domain Account
- Platforms: linux
- Executor: sh
- Elevation Required: False
- Dependency Executor: sh
- Source Path: atomics/T1087.002/T1087.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1087-account_discovery|T1087.002]]

## Input Arguments

### password

- description: Password to authenticate with
- type: string
- default: password

### target_ip

- description: IP to connect to
- type: string
- default: 127.0.0.1

### username

- description: Username and domain to authenticate with
- type: string
- default: domain\user

## Dependencies

Python3 must be installed

### Prerequisite Check

```bash
if [ -x "$(command -v python3 --version)" ]; then exit 0; else exit 1; fi;
```

### Get Prerequisite

```bash
sudo apt-get -y install python3
```

Pip must be installed

### Prerequisite Check

```bash
if [ -x "$(command -v pip --version)" ]; then exit 0; else exit 1; fi;
```

### Get Prerequisite

```bash
wget -O /tmp/get-pip.py https://bootstrap.pypa.io/pip/3.6/get-pip.py
python3 /tmp/get-pip.py
```

The ldapdomaindump module must be installed

### Prerequisite Check

```bash
python3 -c 'import ldapdomaindump' 2>/dev/null
```

### Get Prerequisite

```bash
pip install ldapdomaindump
```

The future module must be installed

### Prerequisite Check

```bash
python3 -c 'import future' 2>/dev/null
```

### Get Prerequisite

```bash
pip install future
```

## Executor

- elevation_required: False
- name: sh

### Command

```bash
ldapdomaindump -u #{username} -p #{password} #{target_ip} -o /tmp/T1087
```

### Cleanup

```bash
rm -rf /tmp/T1087/ 2>/dev/null
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1087.002/T1087.002.yaml)
