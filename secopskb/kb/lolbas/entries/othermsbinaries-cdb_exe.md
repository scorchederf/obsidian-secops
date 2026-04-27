---
title: "Cdb.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/Cdb.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Cdb.yml"
build_date: "2026-04-27 19:14:21"
category: "OtherMSBinaries"
aliases:
  - "Cdb.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1127"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Debugging tool included with Windows Debugging Tools.

## Paths

- `C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\cdb.exe`
- `C:\Program Files (x86)\Windows Kits\10\Debuggers\x86\cdb.exe`

## Commands

### 1. Execute

Launch 64-bit shellcode from the specified .wds file using cdb.exe.

```cmd
cdb.exe -cf {PATH:.wds} -o notepad.exe
```

- Use Case: Local execution of assembly shellcode.
- Privileges: User
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127: Trusted Developer Utilities Proxy Execution]]

### 2. Execute

Attaching to any process and executing shell commands.

```cmd
cdb.exe -pd -pn {process_name}
.shell {CMD}
```

- Use Case: Run a shell command under a trusted Microsoft signed binary
- Privileges: User
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127: Trusted Developer Utilities Proxy Execution]]

### 3. Execute

Execute arbitrary commands and binaries using a debugging script (see Resources section for a sample file).

```cmd
cdb.exe -c {PATH:.txt} "{CMD}"
```

- Use Case: Run commands under a trusted Microsoft signed binary
- Privileges: User
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127: Trusted Developer Utilities Proxy Execution]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_cdb.yml
- Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_unusual_process_network_connection.toml
- Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_network_connection_from_windows_binary.toml
- BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules

## Resources

- {'Link': 'http://www.exploit-monday.com/2016/08/windbg-cdb-shellcode-runner.html'}
- {'Link': 'https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/cdb-command-line-options'}
- {'Link': 'https://gist.github.com/mattifestation/94e2b0a9e3fe1ac0a433b5c3e6bd0bda'}
- {'Link': 'https://mrd0x.com/the-power-of-cdb-debugging-tool/'}
- {'Link': 'https://twitter.com/nas_bench/status/1534957360032120833'}

## Acknowledgements

- {'Person': 'Matt Graeber', 'Handle': '@mattifestation'}
- {'Person': 'mr.d0x', 'Handle': '@mrd0x'}
- {'Person': 'Spooky Sec', 'Handle': '@sec_spooky'}
- {'Person': 'Nasreddine Bencherchali', 'Handle': '@nas_bench'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Cdb.yml)
