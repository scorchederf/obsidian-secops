---
sigma_id: "7dbbcac2-57a0-45ac-b306-ff30a8bd2981"
title: "Windows AMSI Related Registry Tampering Via CommandLine"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_amsi_registry_tampering.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_amsi_registry_tampering.yml"
build_date: "2026-04-26 15:01:54"
status: "experimental"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "7dbbcac2-57a0-45ac-b306-ff30a8bd2981"
  - "Windows AMSI Related Registry Tampering Via CommandLine"
attack_technique_ids:
  - "T1562.001"
  - "T1562.006"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Windows AMSI Related Registry Tampering Via CommandLine

Detects tampering of AMSI (Anti-Malware Scan Interface) related registry values via command line tools such as reg.exe or PowerShell.
AMSI provides a generic interface for applications and services to integrate with antimalware products.
Adversaries may disable AMSI to evade detection of malicious scripts and code execution.

## Metadata

- Rule ID: 7dbbcac2-57a0-45ac-b306-ff30a8bd2981
- Status: experimental
- Level: high
- Author: Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2025-12-25
- Source Path: rules/windows/process_creation/proc_creation_win_amsi_registry_tampering.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]
- [[kb/attack/techniques/T1562-impair_defenses|T1562.006]]

## Detection

```yaml
selection_key:
  CommandLine|contains|all:
  - \Software\Microsoft\Windows Script\Settings
  - AmsiEnable
selection_reg_img:
- Image|endswith: \reg.exe
- OriginalFileName: reg.exe
selection_reg_cmd:
  CommandLine|contains: add
selection_powershell_img:
- Image|endswith:
  - \powershell.exe
  - \pwsh.exe
- OriginalFileName:
  - PowerShell.EXE
  - pwsh.dll
selection_powershell_cmd:
  CommandLine|contains:
  - Set-ItemProperty
  - New-ItemProperty
  - 'sp '
condition: selection_key and (all of selection_powershell_* or all of selection_reg_*)
```

## False Positives

- Unknown

## Simulation

### AMSI Bypass - Create AMSIEnable Reg Key

- Atomic Test: [[kb/atomic/tests/728eca7b_0444_4f6f_ac36_437e3d751dc0-amsi_bypass_create_amsienable_reg_key|728eca7b-0444-4f6f-ac36-437e3d751dc0]]
- atomic_guid: 728eca7b-0444-4f6f-ac36-437e3d751dc0
- name: AMSI Bypass - Create AMSIEnable Reg Key
- technique: T1562.001
- type: atomic-red-team

## References

- https://github.com/arttoolkit/arttoolkit.github.io/blob/16d6230d009e58fd6f773f5317fd4d14c1f26004/_wadcoms/AMSI-Bypass-Jscript_amsienable.md
- https://mostafayahiax.medium.com/hunting-for-amsi-bypassing-methods-9886dda0bf9d
- https://www.mdsec.co.uk/2019/02/macros-and-more-with-sharpshooter-v2-0/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_amsi_registry_tampering.yml)
