---
atomic_guid: "5fdb1a7a-a93c-4fbe-aa29-ddd9ef94ed1f"
title: "Install root CA on Windows with certutil"
framework: "atomic"
generated: "true"
attack_technique_id: "T1553.004"
attack_technique_name: "Subvert Trust Controls: Install Root Certificate"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1553.004/T1553.004.yaml"
build_date: "2026-04-27 19:12:28"
executor: "powershell"
aliases:
  - "5fdb1a7a-a93c-4fbe-aa29-ddd9ef94ed1f"
  - "Install root CA on Windows with certutil"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Creates a root CA with certutil

## ATT&CK Mapping

- [[kb/attack/techniques/T1553-subvert_trust_controls#^t1553004-install-root-certificate|T1553.004: Install Root Certificate]]

## Input Arguments

### pfx_path

- description: Path of the certificate
- type: path
- default: $env:Temp\rootCA2.cer

## Dependencies

Certificate must exist at specified location (#{pfx_path})

### Prerequisite Check

```powershell
if (Test-Path #{pfx_path}) { exit 0 } else { exit 1 }
```

### Get Prerequisite

```powershell
$cert = New-SelfSignedCertificate -DnsName atomicredteam.com -CertStoreLocation cert:\LocalMachine\My
Export-Certificate -Type CERT -Cert  Cert:\LocalMachine\My\$($cert.Thumbprint) -FilePath #{pfx_path}
Get-ChildItem Cert:\LocalMachine\My\$($cert.Thumbprint) | Remove-Item
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
certutil -addstore my #{pfx_path}
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

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1553.004/T1553.004.yaml)
