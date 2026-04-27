---
atomic_guid: "02f35d62-9fdc-4a97-b899-a5d9a876d295"
title: "Potentially Unwanted Applications (PUA)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1204.002"
attack_technique_name: "User Execution: Malicious File"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1204.002/T1204.002.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "02f35d62-9fdc-4a97-b899-a5d9a876d295"
  - "Potentially Unwanted Applications (PUA)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

The Potentially Unwanted Applications (PUA) protection feature in antivirus software can identify and block PUAs from downloading and installing on endpoints in your network. These applications are not considered viruses, malware, or other types of threats, but might perform actions on endpoints that adversely affect their performance or use. This file is similar to EICAR test virus file, but is considered a Potentially Unwanted Application (PUA) instead of a VIRUS (i.e. not actually malicious, but is flagged as it to verify anti-pua protection).

## ATT&CK Mapping

- [[kb/attack/techniques/T1204-user_execution#^t1204002-malicious-file|T1204.002: Malicious File]]

## Input Arguments

### pua_file

- description: path to PotentiallyUnwanted.exe
- type: path
- default: $env:TEMP/PotentiallyUnwanted.exe

### pua_url

- description: url to PotentiallyUnwanted.exe
- type: url
- default: http://amtso.eicar.org/PotentiallyUnwanted.exe

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
Invoke-WebRequest #{pua_url} -OutFile #{pua_file}
& "#{pua_file}"
```

### Cleanup

```powershell
Stop-Process -name PotentiallyUnwanted
Remove-Item #{pua_file} -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1204.002/T1204.002.yaml)
