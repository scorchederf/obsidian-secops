---
atomic_guid: "cf447677-5a4e-4937-a82c-e47d254afd57"
title: "Add domain to Trusted sites Zone"
framework: "atomic"
generated: "true"
attack_technique_id: "T1112"
attack_technique_name: "Modify Registry"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "cf447677-5a4e-4937-a82c-e47d254afd57"
  - "Add domain to Trusted sites Zone"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Add domain to Trusted sites Zone

Attackers may add a domain to the trusted site zone to bypass defenses. Doing this enables attacks such as c2 over office365.
Upon execution, details of the new registry entries will be displayed.
Additionally, open Registry Editor to view the modified entry in HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\.

https://www.blackhat.com/docs/us-17/wednesday/us-17-Dods-Infecting-The-Enterprise-Abusing-Office365-Powershell-For-Covert-C2.pdf

## Metadata

- Atomic GUID: cf447677-5a4e-4937-a82c-e47d254afd57
- Technique: T1112: Modify Registry
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1112/T1112.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Input Arguments

### bad_domain

- description: Domain to add to trusted site zone
- type: string
- default: bad-domain.com

## Executor

- name: powershell

### Command

```powershell
$key= "HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\Domains\#{bad_domain}\"
$name ="bad-subdomain"
new-item $key -Name $name -Force
new-itemproperty $key$name -Name https -Value 2 -Type DWORD;
new-itemproperty $key$name -Name http  -Value 2 -Type DWORD;
new-itemproperty $key$name -Name *     -Value 2 -Type DWORD;
```

### Cleanup

```powershell
$key = "HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\Domains\#{bad_domain}\"
Remove-item  $key -Recurse -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml)
