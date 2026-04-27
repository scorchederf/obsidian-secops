---
title: "Msbuild.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Msbuild.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Msbuild.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "Msbuild.exe"
functions:
  - "AWL Bypass"
  - "Execute"
attack_technique_ids:
  - "T1127.001"
  - "T1036"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Msbuild.exe

Used to compile and execute code

## Metadata

- Category: OSBinaries
- Created: 2018-05-25
- Author: Oddvar Moe
- Source Path: yml/OSBinaries/Msbuild.yml

## Paths

- `C:\Windows\Microsoft.NET\Framework\v2.0.50727\Msbuild.exe`
- `C:\Windows\Microsoft.NET\Framework64\v2.0.50727\Msbuild.exe`
- `C:\Windows\Microsoft.NET\Framework\v3.5\Msbuild.exe`
- `C:\Windows\Microsoft.NET\Framework64\v3.5\Msbuild.exe`
- `C:\Windows\Microsoft.NET\Framework\v4.0.30319\Msbuild.exe`
- `C:\Windows\Microsoft.NET\Framework64\v4.0.30319\Msbuild.exe`
- `C:\Program Files (x86)\MSBuild\14.0\bin\MSBuild.exe`

## Commands

### 1. AWL Bypass

Build and execute a C# project stored in the target XML file.

```cmd
msbuild.exe {PATH:.xml}
```

- Use Case: Compile and run code
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127.001]]

### 2. Execute

Build and execute a C# project stored in the target csproj file.

```cmd
msbuild.exe {PATH:.csproj}
```

- Use Case: Compile and run code
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127.001]]

### 3. Execute

Executes generated Logger DLL file with TargetLogger export.

```cmd
msbuild.exe /logger:TargetLogger,{PATH_ABSOLUTE:.dll};MyParameters,Foo
```

- Use Case: Execute DLL
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127.001]]

### 4. Execute

Execute JScript/VBScript code through XML/XSL Transformation. Requires Visual Studio MSBuild v14.0+.

```cmd
msbuild.exe {PATH:.proj}
```

- Use Case: Execute project file that contains XslTransformation tag parameters
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127.001]]

### 5. Execute

By putting any valid msbuild.exe command-line options in an RSP file and calling it as above will interpret the options as if they were passed on the command line.

```cmd
msbuild.exe @{PATH:.rsp}
```

- Use Case: Bypass command-line based detections
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1036-masquerading|T1036]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/file/file_event/file_event_win_shell_write_susp_directory.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_msbuild_susp_parent_process.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/network_connection/net_connection_win_silenttrinity_stager_msbuild_activity.yml
- Splunk: https://github.com/splunk/security_content/blob/18f63553a9dc1a34122fa123deae2b2f9b9ea391/detections/endpoint/suspicious_msbuild_spawn.yml
- Splunk: https://github.com/splunk/security_content/blob/18f63553a9dc1a34122fa123deae2b2f9b9ea391/detections/endpoint/suspicious_msbuild_rename.yml
- Splunk: https://github.com/splunk/security_content/blob/a1afa0fa605639cbef7d528dec46ce7c8112194a/detections/endpoint/msbuild_suspicious_spawned_by_script_process.yml
- Elastic: https://github.com/elastic/detection-rules/blob/61afb1c1c0c3f50637b1bb194f3e6fb09f476e50/rules/windows/defense_evasion_msbuild_beacon_sequence.toml
- Elastic: https://github.com/elastic/detection-rules/blob/61afb1c1c0c3f50637b1bb194f3e6fb09f476e50/rules/windows/defense_evasion_msbuild_making_network_connections.toml
- Elastic: https://github.com/elastic/detection-rules/blob/ef7548f04c4341e0d1a172810330d59453f46a21/rules/windows/defense_evasion_execution_msbuild_started_by_script.toml
- Elastic: https://github.com/elastic/detection-rules/blob/61afb1c1c0c3f50637b1bb194f3e6fb09f476e50/rules/windows/defense_evasion_execution_msbuild_started_by_office_app.toml
- Elastic: https://github.com/elastic/detection-rules/blob/61afb1c1c0c3f50637b1bb194f3e6fb09f476e50/rules/windows/defense_evasion_execution_msbuild_started_renamed.toml
- BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
- IOC: Msbuild.exe should not normally be executed on workstations

## Resources

- {'Link': 'https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1127/T1127.md'}
- {'Link': 'https://github.com/Cn33liz/MSBuildShell'}
- {'Link': 'https://pentestlab.blog/2017/05/29/applocker-bypass-msbuild/'}
- {'Link': 'https://oddvar.moe/2017/12/13/applocker-case-study-how-insecure-is-it-really-part-1/'}
- {'Link': 'https://gist.github.com/bohops/4ffc43a281e87d108875f07614324191'}
- {'Link': 'https://github.com/LOLBAS-Project/LOLBAS/issues/165'}
- {'Link': 'https://docs.microsoft.com/en-us/visualstudio/msbuild/msbuild-response-files'}
- {'Link': 'https://www.daveaglick.com/posts/msbuild-loggers-and-logging-events'}

## Acknowledgements

- {'Person': 'Casey Smith', 'Handle': '@subtee'}
- {'Person': 'Cn33liz', 'Handle': '@Cneelis'}
- {'Person': 'Jimmy', 'Handle': '@bohops'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Msbuild.yml)
