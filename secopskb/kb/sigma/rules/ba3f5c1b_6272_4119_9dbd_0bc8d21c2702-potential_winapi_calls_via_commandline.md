---
sigma_id: "ba3f5c1b-6272-4119-9dbd-0bc8d21c2702"
title: "Potential WinAPI Calls Via CommandLine"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_inline_win_api_access.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_inline_win_api_access.yml"
build_date: "2026-04-26 15:01:49"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "ba3f5c1b-6272-4119-9dbd-0bc8d21c2702"
  - "Potential WinAPI Calls Via CommandLine"
attack_technique_ids:
  - "T1106"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potential WinAPI Calls Via CommandLine

Detects the use of WinAPI Functions via the commandline. As seen used by threat actors via the tool winapiexec

## Metadata

- Rule ID: ba3f5c1b-6272-4119-9dbd-0bc8d21c2702
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-09-06
- Modified: 2025-03-06
- Source Path: rules/windows/process_creation/proc_creation_win_susp_inline_win_api_access.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1106-native_api|T1106]]

## Detection

```yaml
selection:
  CommandLine|contains:
  - AddSecurityPackage
  - AdjustTokenPrivileges
  - Advapi32
  - CloseHandle
  - CreateProcessWithToken
  - CreatePseudoConsole
  - CreateRemoteThread
  - CreateThread
  - CreateUserThread
  - DangerousGetHandle
  - DuplicateTokenEx
  - EnumerateSecurityPackages
  - FreeHGlobal
  - FreeLibrary
  - GetDelegateForFunctionPointer
  - GetLogonSessionData
  - GetModuleHandle
  - GetProcAddress
  - GetProcessHandle
  - GetTokenInformation
  - ImpersonateLoggedOnUser
  - kernel32
  - LoadLibrary
  - memcpy
  - MiniDumpWriteDump
  - ntdll
  - OpenDesktop
  - OpenProcess
  - OpenProcessToken
  - OpenThreadToken
  - OpenWindowStation
  - PtrToString
  - QueueUserApc
  - ReadProcessMemory
  - RevertToSelf
  - RtlCreateUserThread
  - secur32
  - SetThreadToken
  - VirtualAlloc
  - VirtualFree
  - VirtualProtect
  - WaitForSingleObject
  - WriteInt32
  - WriteProcessMemory
  - ZeroFreeGlobalAllocUnicode
filter_optional_mpcmdrun:
  Image|endswith: \MpCmdRun.exe
  CommandLine|contains: GetLoadLibraryWAddress32
filter_optional_compatTelRunner:
  ParentImage|endswith: \CompatTelRunner.exe
  CommandLine|contains:
  - FreeHGlobal
  - PtrToString
  - kernel32
  - CloseHandle
condition: selection and not 1 of filter_optional_*
```

## False Positives

- Some legitimate action or applications may use these functions. Investigate further to determine the legitimacy of the activity.

## References

- https://twitter.com/m417z/status/1566674631788007425

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_inline_win_api_access.yml)
