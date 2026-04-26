---
atomic_guid: "7ab0205a-34e4-4a44-9b04-e1541d1a57be"
title: "Enumerate Linked Policies In ADSISearcher Discovery"
framework: "atomic"
generated: "true"
attack_technique_id: "T1087.002"
attack_technique_name: "Account Discovery: Domain Account"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1087.002/T1087.002.yaml"
build_date: "2026-04-26 14:38:39"
executor: "powershell"
aliases:
  - "7ab0205a-34e4-4a44-9b04-e1541d1a57be"
  - "Enumerate Linked Policies In ADSISearcher Discovery"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Enumerate Linked Policies In ADSISearcher Discovery

The following Atomic test will utilize ADSISearcher to enumerate organizational unit within Active Directory.
Upon successful execution a listing of users will output with their paths in AD.
Reference: https://medium.com/@pentesttas/discover-hidden-gpo-s-on-active-directory-using-ps-adsi-a284b6814c81

## Metadata

- Atomic GUID: 7ab0205a-34e4-4a44-9b04-e1541d1a57be
- Technique: T1087.002: Account Discovery: Domain Account
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Source Path: atomics/T1087.002/T1087.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1087-account_discovery|T1087.002]]

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
(([adsisearcher]'(objectcategory=organizationalunit)').FindAll()).Path | %{if(([ADSI]"$_").gPlink){Write-Host "[+] OU Path:"([ADSI]"$_").Path;$a=((([ADSI]"$_").gplink) -replace "[[;]" -split "]");for($i=0;$i -lt $a.length;$i++){if($a[$i]){Write-Host "Policy Path[$i]:"([ADSI]($a[$i]).Substring(0,$a[$i].length-1)).Path;Write-Host "Policy Name[$i]:"([ADSI]($a[$i]).Substring(0,$a[$i].length-1)).DisplayName} };Write-Output "`n" }}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1087.002/T1087.002.yaml)
