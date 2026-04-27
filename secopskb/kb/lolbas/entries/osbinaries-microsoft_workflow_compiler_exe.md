---
title: "Microsoft.Workflow.Compiler.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Microsoft.Workflow.Compiler.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Microsoft.Workflow.Compiler.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "Microsoft.Workflow.Compiler.exe"
functions:
  - "Execute"
  - "AWL Bypass"
attack_technique_ids:
  - "T1127"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Microsoft.Workflow.Compiler.exe

A utility included with .NET that is capable of compiling and executing C# or VB.net code.

## Metadata

- Category: OSBinaries
- Created: 2018-10-22
- Author: Conor Richard
- Source Path: yml/OSBinaries/Microsoft.Workflow.Compiler.yml

## Paths

- `C:\Windows\Microsoft.Net\Framework64\v4.0.30319\Microsoft.Workflow.Compiler.exe`

## Commands

### 1. Execute

Compile and execute C# or VB.net code in a XOML file referenced in the first argument (any extension accepted).

```cmd
Microsoft.Workflow.Compiler.exe {PATH} {PATH:.log}
```

- Use Case: Compile and run code
- Privileges: User
- Operating System: Windows 10S, Windows 11
- ATT&CK: [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127]]

### 2. Execute

Compile and execute C# or VB.net code in a XOML file referenced in the test.txt file.

```cmd
Microsoft.Workflow.Compiler.exe {PATH} {PATH:.log}
```

- Use Case: Compile and run code
- Privileges: User
- Operating System: Windows 10S, Windows 11
- ATT&CK: [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127]]

### 3. AWL Bypass

Compile and execute C# or VB.net code in a XOML file referenced in the test.txt file.

```cmd
Microsoft.Workflow.Compiler.exe {PATH} {PATH:.log}
```

- Use Case: Compile and run code
- Privileges: User
- Operating System: Windows 10S, Windows 11
- ATT&CK: [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_workflow_compiler.yml
- Splunk: https://github.com/splunk/security_content/blob/961a81d4a5cb5c5febec4894d6d812497171a85c/detections/endpoint/suspicious_microsoft_workflow_compiler_usage.yml
- Splunk: https://github.com/splunk/security_content/blob/18f63553a9dc1a34122fa123deae2b2f9b9ea391/detections/endpoint/suspicious_microsoft_workflow_compiler_rename.yml
- Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_unusual_process_network_connection.toml
- Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_network_connection_from_windows_binary.toml
- BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
- IOC: Microsoft.Workflow.Compiler.exe would not normally be run on workstations.
- IOC: The presence of csc.exe or vbc.exe as child processes of Microsoft.Workflow.Compiler.exe
- IOC: Presence of "<CompilerInput" in a text file.

## Resources

- {'Link': 'https://twitter.com/mattifestation/status/1030445200475185154'}
- {'Link': 'https://posts.specterops.io/arbitrary-unsigned-code-execution-vector-in-microsoft-workflow-compiler-exe-3d9294bc5efb'}
- {'Link': 'https://gist.github.com/mattifestation/3e28d391adbd7fe3e0c722a107a25aba#file-workflowcompilerdetectiontests-ps1'}
- {'Link': 'https://gist.github.com/mattifestation/7ba8fc8f724600a9f525714c9cf767fd#file-createcompilerinputxml-ps1'}
- {'Link': 'https://www.forcepoint.com/blog/security-labs/using-c-post-powershell-attacks'}
- {'Link': 'https://www.fortynorthsecurity.com/microsoft-workflow-compiler-exe-veil-and-cobalt-strike/'}
- {'Link': 'https://medium.com/@Bank_Security/undetectable-c-c-reverse-shells-fab4c0ec4f15'}

## Acknowledgements

- {'Person': 'Matt Graeber', 'Handle': '@mattifestation'}
- {'Person': 'John Bergbom', 'Handle': '@BergbomJohn'}
- {'Person': 'FortyNorth Security', 'Handle': '@FortyNorthSec'}
- {'Person': 'Bank Security', 'Handle': '@Bank_Security'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Microsoft.Workflow.Compiler.yml)
