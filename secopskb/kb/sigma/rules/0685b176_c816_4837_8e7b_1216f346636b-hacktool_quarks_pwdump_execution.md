---
sigma_id: "0685b176-c816-4837-8e7b-1216f346636b"
title: "HackTool - Quarks PwDump Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_quarks_pwdump.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_quarks_pwdump.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "0685b176-c816-4837-8e7b-1216f346636b"
  - "HackTool - Quarks PwDump Execution"
attack_technique_ids:
  - "T1003.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects usage of the Quarks PwDump tool via commandline arguments

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping#^t1003002-security-account-manager|T1003.002: Security Account Manager]]

## Detection

```yaml
selection_img:
  Image|endswith: \QuarksPwDump.exe
selection_cli:
  CommandLine:
  - ' -dhl'
  - ' --dump-hash-local'
  - ' -dhdc'
  - ' --dump-hash-domain-cached'
  - ' --dump-bitlocker'
  - ' -dhd '
  - ' --dump-hash-domain '
  - --ntds-file
condition: 1 of selection_*
```

## False Positives

- Unlikely

## References

- https://github.com/quarkslab/quarkspwdump
- https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/seedworm-apt-iran-middle-east

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_quarks_pwdump.yml)
