---
sigma_id: "91a2c315-9ee6-4052-a853-6f6a8238f90d"
title: "Findstr GPP Passwords"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_findstr_gpp_passwords.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_findstr_gpp_passwords.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "91a2c315-9ee6-4052-a853-6f6a8238f90d"
  - "Findstr GPP Passwords"
attack_technique_ids:
  - "T1552.006"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Look for the encrypted cpassword value within Group Policy Preference files on the Domain Controller. This value can be decrypted with gpp-decrypt.

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1552-unsecured_credentials#^t1552006-group-policy-preferences|T1552.006: Group Policy Preferences]]

## Detection

```yaml
selection_img:
- Image|endswith:
  - \find.exe
  - \findstr.exe
- OriginalFileName:
  - FIND.EXE
  - FINDSTR.EXE
selection_cli:
  CommandLine|contains|all:
  - cpassword
  - \sysvol\
  - .xml
condition: all of selection_*
```

## False Positives

- Unknown

## Simulation

### GPP Passwords (findstr)

- Atomic Test: [[kb/atomic/tests/870fe8fb_5e23_4f5f_b89d_dd7fe26f3b5f-gpp_passwords_findstr|870fe8fb-5e23-4f5f-b89d-dd7fe26f3b5f]]
- atomic_guid: 870fe8fb-5e23-4f5f-b89d-dd7fe26f3b5f
- name: GPP Passwords (findstr)
- technique: T1552.006
- type: atomic-red-team

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1552.006/T1552.006.md#atomic-test-1---gpp-passwords-findstr

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_findstr_gpp_passwords.yml)
