---
title: "adplus.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/Adplus.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Adplus.yml"
build_date: "2026-04-27 19:14:21"
category: "OtherMSBinaries"
aliases:
  - "adplus.exe"
functions:
  - "Dump"
  - "Execute"
attack_technique_ids:
  - "T1003.001"
  - "T1127"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Debugging tool included with Windows Debugging Tools

## Paths

- `C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\adplus.exe`
- `C:\Program Files (x86)\Windows Kits\10\Debuggers\x86\adplus.exe`

## Commands

### 1. Dump

Creates a memory dump of the lsass process

```cmd
adplus.exe -hang -pn lsass.exe -o {PATH_ABSOLUTE:folder} -quiet
```

- Use Case: Create memory dump and parse it offline
- Privileges: SYSTEM
- Operating System: All Windows
- ATT&CK: [[kb/attack/techniques/T1003-os_credential_dumping#^t1003001-lsass-memory|T1003.001: LSASS Memory]]

### 2. Execute

Execute arbitrary commands using adplus config file (see Resources section for a sample file).

```cmd
adplus.exe -c {PATH:.xml}
```

- Use Case: Run commands under a trusted Microsoft signed binary
- Privileges: User
- Operating System: All Windows
- ATT&CK: [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127: Trusted Developer Utilities Proxy Execution]]

### 3. Dump

Dump process memory using adplus config file (see Resources section for a sample file).

```cmd
adplus.exe -c {PATH:.xml}
```

- Use Case: Run commands under a trusted Microsoft signed binary
- Privileges: SYSTEM
- Operating System: All Windows
- ATT&CK: [[kb/attack/techniques/T1003-os_credential_dumping#^t1003001-lsass-memory|T1003.001: LSASS Memory]]

### 4. Execute

Execute arbitrary commands and binaries from the context of adplus. Note that providing an output directory via '-o' is required.

```cmd
adplus.exe -crash -o "{PATH_ABSOLUTE:folder}" -sc {PATH:.exe}
```

- Use Case: Run commands under a trusted Microsoft signed binary
- Privileges: User
- Operating System: All windows
- ATT&CK: [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127: Trusted Developer Utilities Proxy Execution]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/6199a703221a98ae6ad343c79c558da375203e4e/rules/windows/process_creation/proc_creation_win_lolbin_adplus.yml
- IOC: As a Windows SDK binary, execution on a system may be suspicious

## Resources

- {'Link': 'https://mrd0x.com/adplus-debugging-tool-lsass-dump/'}
- {'Link': 'https://twitter.com/nas_bench/status/1534916659676422152'}
- {'Link': 'https://twitter.com/nas_bench/status/1534915321856917506'}

## Acknowledgements

- {'Person': 'mr.d0x', 'Handle': '@mrd0x'}
- {'Person': 'Nasreddine Bencherchali', 'Handle': '@nas_bench'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Adplus.yml)
