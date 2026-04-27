---
atomic_guid: "78b274f8-acb0-428b-b1f7-7b0d0e73330a"
title: "Export Root Certificate with Export-Certificate"
framework: "atomic"
generated: "true"
attack_technique_id: "T1552.004"
attack_technique_name: "Unsecured Credentials: Private Keys"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.004/T1552.004.yaml"
build_date: "2026-04-27 19:12:28"
executor: "powershell"
aliases:
  - "78b274f8-acb0-428b-b1f7-7b0d0e73330a"
  - "Export Root Certificate with Export-Certificate"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Creates a Root certificate and exports it with Export-Certificate PowerShell Cmdlet.
Upon a successful attempt, this will write a pfx to disk and utilize the Cmdlet Export-Certificate.

## ATT&CK Mapping

- [[kb/attack/techniques/T1552-unsecured_credentials#^t1552004-private-keys|T1552.004: Private Keys]]

## Input Arguments

### pfx_path

- description: Path of the certificate
- type: path
- default: $env:Temp\AtomicRedTeam.cer

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
$cert = New-SelfSignedCertificate -DnsName atomicredteam.com -CertStoreLocation cert:\LocalMachine\My
Set-Location Cert:\LocalMachine\My
Export-Certificate -Type CERT -Cert  Cert:\LocalMachine\My\$($cert.Thumbprint) -FilePath #{pfx_path}
```

### Cleanup

```powershell
try {
   $cert = Import-Certificate -FilePath #{pfx_path} -CertStoreLocation Cert:\LocalMachine\My -ErrorAction Ignore
   Get-ChildItem Cert:\LocalMachine\My\$($cert.Thumbprint) -ErrorAction Ignore | Remove-Item -ErrorAction Ignore
   Get-ChildItem Cert:\LocalMachine\Root\$($cert.Thumbprint) -ErrorAction Ignore | Remove-Item -ErrorAction Ignore
}
catch { }
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552.004/T1552.004.yaml)
