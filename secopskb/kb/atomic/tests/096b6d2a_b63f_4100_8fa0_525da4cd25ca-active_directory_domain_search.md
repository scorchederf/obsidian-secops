---
atomic_guid: "096b6d2a-b63f-4100-8fa0-525da4cd25ca"
title: "Active Directory Domain Search"
framework: "atomic"
generated: "true"
attack_technique_id: "T1087.002"
attack_technique_name: "Account Discovery: Domain Account"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1087.002/T1087.002.yaml"
build_date: "2026-04-26 14:38:39"
executor: "sh"
aliases:
  - "096b6d2a-b63f-4100-8fa0-525da4cd25ca"
  - "Active Directory Domain Search"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Active Directory Domain Search

Output information from LDAPSearch. LDAP Password is the admin-user password on Active Directory

## Metadata

- Atomic GUID: 096b6d2a-b63f-4100-8fa0-525da4cd25ca
- Technique: T1087.002: Account Discovery: Domain Account
- Platforms: linux
- Executor: sh
- Elevation Required: False
- Dependency Executor: sh
- Source Path: atomics/T1087.002/T1087.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1087-account_discovery|T1087.002]]

## Input Arguments

### domain

- description: The domain to be tested
- type: string
- default: example

### password

- description: password of the user with admin privileges referenced in admin_user
- type: string
- default: s3CurePssw0rD!

### top_level_domain

- description: The top level domain (.com, .test, .remote, etc... following domain, minus the .)
- type: string
- default: test

### user

- description: username@domain of a user within the ad database
- type: string
- default: user@example.test

## Dependencies

Packages sssd-ad sssd-tools realmd adcli installed and realm available, ldapsearch

### Prerequisite Check

```text
which ldapsearch
```

### Get Prerequisite

```text
echo ldapsearch not found
```

## Executor

- elevation_required: False
- name: sh

### Command

```sh
ldapsearch -H ldap://#{domain}.#{top_level_domain}:389 -x -D #{user} -w #{password} -b "CN=Users,DC=#{domain},DC=#{top_level_domain}" -s sub -a always -z 1000 dn
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1087.002/T1087.002.yaml)
