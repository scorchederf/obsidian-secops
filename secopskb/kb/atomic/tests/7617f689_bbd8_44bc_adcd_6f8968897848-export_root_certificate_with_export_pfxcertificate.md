---
atomic_guid: "7617f689-bbd8-44bc-adcd-6f8968897848"
title: "Export Root Certificate with Export-PFXCertificate"
framework: "atomic"
generated: "true"
attack_technique_id: "T1552.004"
attack_technique_name: "Unsecured Credentials: Private Keys"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.004/T1552.004.yaml"
build_date: "2026-04-27 19:12:28"
executor: "powershell"
aliases:
  - "7617f689-bbd8-44bc-adcd-6f8968897848"
  - "Export Root Certificate with Export-PFXCertificate"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Creates a Root certificate and exports it with Export-PFXCertificate PowerShell Cmdlet.
Upon a successful attempt, this will write a pfx to disk and utilize the Cmdlet Export-PFXCertificate.

## ATT&CK Mapping

- [[kb/attack/techniques/T1552-unsecured_credentials#^t1552004-private-keys|T1552.004: Private Keys]]

## Input Arguments

### pfx_path

- description: output path of the certificate
- type: string
- default: $env:Temp\atomicredteam.pfx

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
$mypwd = ConvertTo-SecureString -String "AtomicRedTeam" -Force -AsPlainText
$cert = New-SelfSignedCertificate -DnsName atomicredteam.com -CertStoreLocation cert:\LocalMachine\My
Set-Location Cert:\LocalMachine\My
Get-ChildItem -Path $cert.Thumbprint | Export-PfxCertificate -FilePath #{pfx_path} -Password $mypwd
```

### Cleanup

```powershell
try {
$cert = Import-Certificate -FilePath #{pfx_path} -CertStoreLocation Cert:\LocalMachine\My
Get-ChildItem Cert:\LocalMachine\My\$($cert.Thumbprint) -ErrorAction Ignore | Remove-Item -ErrorAction Ignore
Get-ChildItem Cert:\LocalMachine\Root\$($cert.Thumbprint) -ErrorAction Ignore | Remove-Item -ErrorAction Ignore
} catch { }
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.004/T1552.004.yaml)
