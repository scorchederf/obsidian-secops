---
atomic_guid: "76f49d86-5eb1-461a-a032-a480f86652f1"
title: "Install root CA on Windows"
framework: "atomic"
generated: "true"
attack_technique_id: "T1553.004"
attack_technique_name: "Subvert Trust Controls: Install Root Certificate"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1553.004/T1553.004.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "76f49d86-5eb1-461a-a032-a480f86652f1"
  - "Install root CA on Windows"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Install root CA on Windows

Creates a root CA with Powershell

## Metadata

- Atomic GUID: 76f49d86-5eb1-461a-a032-a480f86652f1
- Technique: T1553.004: Subvert Trust Controls: Install Root Certificate
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1553.004/T1553.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1553-subvert_trust_controls|T1553.004]]

## Input Arguments

### pfx_path

- description: Path of the certificate
- type: path
- default: rootCA.cer

## Dependencies

Verify the certificate exists. It generates if not on disk.

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
$cert = Import-Certificate -FilePath #{pfx_path} -CertStoreLocation Cert:\LocalMachine\My
Move-Item -Path $cert.PSPath -Destination "Cert:\LocalMachine\Root"
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

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1553.004/T1553.004.yaml)
