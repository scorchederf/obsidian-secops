---
atomic_guid: "b404caaa-12ce-43c7-9214-62a531c044f7"
title: "Decrypt Eicar File and Write to File"
framework: "atomic"
generated: "true"
attack_technique_id: "T1027.013"
attack_technique_name: "Obfuscated Files or Information: Encrypted/Encoded File"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1027.013/T1027.013.yaml"
build_date: "2026-04-27 19:12:25"
executor: "powershell"
aliases:
  - "b404caaa-12ce-43c7-9214-62a531c044f7"
  - "Decrypt Eicar File and Write to File"
platforms:
  - "windows"
  - "macos"
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Decrypt the eicar value, and write it to file, for AV/EDR to try to catch.

## ATT&CK Mapping

- [[kb/attack/techniques/T1027-obfuscated_files_or_information#^t1027013-encrypted-encoded-file|T1027.013: Encrypted/Encoded File]]

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
$encryptedString = "76492d1116743f0423413b16050a5345MgB8AGkASwA0AHMAbwBXAFoAagBkAFoATABXAGIAdAA5AFcAWAB1AFMANABVAEEAPQA9AHwAZQBjAGMANgAwADQAZAA0AGQAMQAwADUAYgA4ADAAMgBmADkAZgBjADEANQBjAGMANQBiAGMANwA2AGYANQBmADUANABhAGIAYgAyAGMANQA1AGQAMgA5ADEANABkADUAMgBiAGMANgA2AGMAMAAxADUAZABjADAAOABjAGIANAA1ADUANwBjADcAZQBlAGQAYgAxADEAOQA4AGIAMwAwADMANwAwADAANQA2ADQAOAA4ADkAZgA4ADMAZQA4ADgAOQBiAGEAMAA2ADMAMQAyADYAMwBiAGUAMAAxADgANAA0ADYAOAAxADQANQAwAGUANwBkADkANABjADcANQAxADgAYQA2ADMANQA4AGIAYgA1ADkANQAzAGIAMwAxADYAOAAwADQAMgBmADcAZQBjADYANQA5AGIANwBkADUAOAAyAGEAMgBiADEAMQAzAGQANABkADkAZgA3ADMAMABiADgAOQAxADAANAA4ADcAOQA5ADEAYQA1ADYAZAAzADQANwA3AGYANgAyADcAMAAwADEAMQA4ADEAZgA5ADUAYgBmAGYANQA3ADQAZQA4AGUAMAAxADUANwAwAGQANABiADMAMwA2ADgANwA0AGIANwAyADMAMQBhADkAZABhADEANQAzADQAMgAzADEANwAxADAAZgAxADkAYQA1ADEAMQA="
$key = [byte]1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32
$decrypt = ConvertTo-SecureString -String $encryptedString -Key $key
$decryptedString = [Runtime.InteropServices.Marshal]::PtrToStringBSTR([Runtime.InteropServices.Marshal]::SecureStringToBSTR($decrypt))
#Write the decrypted eicar string to a file
$decryptedString | Out-File $env:temp\T1027.013_decryptedEicar.txt
```

### Cleanup

```powershell
Remove-Item $env:temp\T1027.013_decryptedEicar.txt -Force -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1027.013/T1027.013.yaml)
