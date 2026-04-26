---
sigma_id: "cd3d1298-eb3b-476c-ac67-12847de55813"
title: "DLL Execution via Rasautou.exe"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_lolbin_rasautou_dll_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_rasautou_dll_execution.yml"
build_date: "2026-04-26 14:14:23"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "cd3d1298-eb3b-476c-ac67-12847de55813"
  - "DLL Execution via Rasautou.exe"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# DLL Execution via Rasautou.exe

Detects using Rasautou.exe for loading arbitrary .DLL specified in -d option and executes the export specified in -p.

## Metadata

- Rule ID: cd3d1298-eb3b-476c-ac67-12847de55813
- Status: test
- Level: medium
- Author: Julia Fomina, oscd.community
- Date: 2020-10-09
- Source Path: rules/windows/process_creation/proc_creation_win_lolbin_rasautou_dll_execution.yml

## Logsource

- category: process_creation
- definition: Since options '-d' and '-p' were removed in Windows 10 this rule is relevant only for Windows before 10. And as Windows 7 doesn't log command line in 4688 by default, to detect this attack you need Sysmon 1 configured or KB3004375 installed for command-line auditing (https://support.microsoft.com/en-au/help/3004375/microsoft-security-advisory-update-to-improve-windows-command-line-aud)
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection_img:
- Image|endswith: \rasautou.exe
- OriginalFileName: rasdlui.exe
selection_cli:
  CommandLine|contains|all:
  - ' -d '
  - ' -p '
condition: all of selection*
```

## False Positives

- Unlikely

## References

- https://lolbas-project.github.io/lolbas/Binaries/Rasautou/
- https://github.com/fireeye/DueDLLigence
- https://www.fireeye.com/blog/threat-research/2019/10/staying-hidden-on-the-endpoint-evading-detection-with-shellcode.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_rasautou_dll_execution.yml)
