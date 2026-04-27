---
atomic_guid: "962a6017-1c09-45a6-880b-adc9c57cb22e"
title: "Enumerate domain computers within Active Directory using DirectorySearcher"
framework: "atomic"
generated: "true"
attack_technique_id: "T1018"
attack_technique_name: "Remote System Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1018/T1018.yaml"
build_date: "2026-04-27 19:12:25"
executor: "powershell"
aliases:
  - "962a6017-1c09-45a6-880b-adc9c57cb22e"
  - "Enumerate domain computers within Active Directory using DirectorySearcher"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This test is a Powershell script that enumerates Active Directory to determine computers that are joined to the domain. 
This test is designed to mimic how SessionGopher can determine the additional systems within a domain, which has been used before by threat actors to aid in lateral movement. 
Reference: [Head Fake: Tackling Disruptive Ransomware Attacks](https://www.mandiant.com/resources/head-fake-tackling-disruptive-ransomware-attacks). 
Upon successful execution, this test will output the names of the computers that reside on the domain to the console window.

## ATT&CK Mapping

- [[kb/attack/techniques/T1018-remote_system_discovery|T1018: Remote System Discovery]]

## Dependencies

This PC must be joined to a domain.

### Prerequisite Check

```powershell
if ((Get-WmiObject -Class Win32_ComputerSystem).partofdomain -eq $true) {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
write-host "This PC must be manually added to a domain."
```

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
$DirectorySearcher = New-Object System.DirectoryServices.DirectorySearcher("(ObjectCategory=Computer)")
$DirectorySearcher.PropertiesToLoad.Add("Name")
$Computers = $DirectorySearcher.findall()
foreach ($Computer in $Computers) {
  $Computer = $Computer.Properties.name
  if (!$Computer) { Continue }
  Write-Host $Computer}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1018/T1018.yaml)
