---
atomic_guid: "5898902d-c5ad-479a-8545-6f5ab3cfc87f"
title: "Phantom Dll Hijacking - ualapi.dll"
framework: "atomic"
generated: "true"
attack_technique_id: "T1574.001"
attack_technique_name: "Hijack Execution Flow: DLL"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1574.001/T1574.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "5898902d-c5ad-479a-8545-6f5ab3cfc87f"
  - "Phantom Dll Hijacking - ualapi.dll"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Phantom Dll Hijacking - ualapi.dll

Re-starting the Print Spooler service leads to C:\Windows\System32\ualapi.dll being loaded
A malicious ualapi.dll placed in the System32 directory will lead to its execution whenever the system starts

Upon successful execution, amsi.dll will be copied and renamed to ualapi.dll and then ualapi.dll will be copied to system32 folder for loading during system restart.
Print Spooler service is also configured to auto start. Reboot of system is required

## Metadata

- Atomic GUID: 5898902d-c5ad-479a-8545-6f5ab3cfc87f
- Technique: T1574.001: Hijack Execution Flow: DLL
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1574.001/T1574.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
copy %windir%\System32\amsi.dll %APPDATA%\amsi.dll
ren %APPDATA%\amsi.dll ualapi.dll
copy %APPDATA%\ualapi.dll %windir%\System32\ualapi.dll
sc config Spooler start=auto
```

### Cleanup

```cmd
del %windir%\System32\ualapi.dll
del %APPDATA%\ualapi.dll
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1574.001/T1574.001.yaml)
