---
atomic_guid: "d58d749c-4450-4975-a9e9-8b1d562755c2"
title: "Active Directory Domain Search Using LDAP - Linux (Ubuntu)/macOS"
framework: "atomic"
generated: "true"
attack_technique_id: "T1069.002"
attack_technique_name: "Permission Groups Discovery: Domain Groups"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1069.002/T1069.002.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "d58d749c-4450-4975-a9e9-8b1d562755c2"
  - "Active Directory Domain Search Using LDAP - Linux (Ubuntu)/macOS"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Active Directory Domain Search Using LDAP - Linux (Ubuntu)/macOS

Output information from LDAPSearch. LDAP Password is the admin-user password on Active Directory

## Metadata

- Atomic GUID: d58d749c-4450-4975-a9e9-8b1d562755c2
- Technique: T1069.002: Permission Groups Discovery: Domain Groups
- Platforms: linux
- Executor: sh
- Elevation Required: False
- Dependency Executor: sh
- Source Path: atomics/T1069.002/T1069.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1069-permission_groups_discovery|T1069.002]]

## Input Arguments

### domain

- description: The domain to be tested
- type: string
- default: example

### password

- description: password of the user referenced inside user
- type: string
- default: s3CurePssw0rD!

### top_level_domain

- description: The top level domain (.com, .test, .remote, etc... following domain, minus the .)
- type: string
- default: com

### user

- description: username@domain of a user
- type: string
- default: user@example.com

## Dependencies

Packages sssd-ad sssd-tools realmd adcli installed and realm available, ldapsearch

### Prerequisite Check

```bash
which ldapsearch
```

### Get Prerequisite

```bash
echo missing ldapsearch command; exit 1
```

## Executor

- elevation_required: False
- name: sh

### Command

```bash
ldapsearch -H ldap://#{domain}.#{top_level_domain}:389 -x -D #{user} -w #{password} -b "CN=Users,DC=#{domain},DC=#{top_level_domain}" "(objectClass=group)" -s sub -a always -z 1000 dn
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1069.002/T1069.002.yaml)
