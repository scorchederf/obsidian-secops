---
title: "Mpiexec.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/Mpiexec.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Mpiexec.yml"
build_date: "2026-04-27 18:39:01"
category: "OtherMSBinaries"
aliases:
  - "Mpiexec.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1127"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Mpiexec.exe

Command-line tool for running Message Passing Interface (MPI) applications.

## Metadata

- Category: OtherMSBinaries
- Created: 2025-09-25
- Author: Avihay Eldad
- Source Path: yml/OtherMSBinaries/Mpiexec.yml

## Paths

- `C:\Program Files\Microsoft MPI\Bin\mpiexec.exe`
- `C:\Program Files (x86)\Microsoft MPI\Bin\mpiexec.exe`

## Commands

### 1. Execute

Executes a command via MPI command-line tool.

```cmd
mpiexec.exe {CMD}
```

- Use Case: Executes commands under a trusted, Microsoft signed binary.
- Privileges: User
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127]]

## Resources

- {'Link': 'https://learn.microsoft.com/en-us/powershell/high-performance-computing/mpiexec'}

## Acknowledgements

- {'Person': 'Avihay Eldad', 'Handle': '@AvihayEldad'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Mpiexec.yml)
