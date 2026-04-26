---
sigma_id: "7d6d30b8-5b91-4b90-a891-46cccaf29598"
title: "Program Executed Using Proxy/Local Command Via SSH.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_ssh_proxy_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_ssh_proxy_execution.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "7d6d30b8-5b91-4b90-a891-46cccaf29598"
  - "Program Executed Using Proxy/Local Command Via SSH.EXE"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Program Executed Using Proxy/Local Command Via SSH.EXE

Detect usage of the "ssh.exe" binary as a proxy to launch other programs.

## Metadata

- Rule ID: 7d6d30b8-5b91-4b90-a891-46cccaf29598
- Status: test
- Level: medium
- Author: frack113, Nasreddine Bencherchali
- Date: 2022-12-29
- Modified: 2025-10-16
- Source Path: rules/windows/process_creation/proc_creation_win_ssh_proxy_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection_parent:
  ParentImage: C:\Windows\System32\OpenSSH\sshd.exe
selection_cli_img:
- Image|endswith: \ssh.exe
- Product: OpenSSH for Windows
- Hashes|contains:
  - IMPHASH=55b4964d29aad5438b9e950052dbbbc0
  - IMPHASH=334d66c33503ccbf647c15b47c27eef4
  - IMPHASH=27b0da080ef92afb37983d30d839141e
  - IMPHASH=977eb4c263d384e47daa0712d34713ab
  - IMPHASH=3eaadce9ae43d5a918bb082065815c3b
  - IMPHASH=980fe6cf0d996ab1eedf877222e722aa
  - IMPHASH=5f959422308ac3d721010d66647e100e
  - IMPHASH=a49aaa3d03d1cd9c8dc7fca60f7f480b
  - IMPHASH=dd335f759b6d5d6a8382b71dd9d65791
selection_cli_flags:
- CommandLine|contains: ProxyCommand=
- CommandLine|contains|all:
  - PermitLocalCommand=yes
  - ' LocalCommand'
condition: selection_parent or all of selection_cli_*
```

## False Positives

- Legitimate usage for administration purposes

## References

- https://lolbas-project.github.io/lolbas/Binaries/Ssh/
- https://github.com/LOLBAS-Project/LOLBAS/pull/211/files
- https://gtfobins.github.io/gtfobins/ssh/
- https://man.openbsd.org/ssh_config#ProxyCommand
- https://man.openbsd.org/ssh_config#LocalCommand

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_ssh_proxy_execution.yml)
