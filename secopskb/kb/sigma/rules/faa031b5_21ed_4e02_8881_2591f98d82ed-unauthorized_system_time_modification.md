---
sigma_id: "faa031b5-21ed-4e02-8881-2591f98d82ed"
title: "Unauthorized System Time Modification"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_susp_time_modification.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_susp_time_modification.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "low"
logsource: "windows / security"
aliases:
  - "faa031b5-21ed-4e02-8881-2591f98d82ed"
  - "Unauthorized System Time Modification"
attack_technique_ids:
  - "T1070.006"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Unauthorized System Time Modification

Detect scenarios where a potentially unauthorized application or user is modifying the system time.

## Metadata

- Rule ID: faa031b5-21ed-4e02-8881-2591f98d82ed
- Status: test
- Level: low
- Author: @neu5ron
- Date: 2019-02-05
- Modified: 2025-12-03
- Source Path: rules/windows/builtin/security/win_security_susp_time_modification.yml

## Logsource

- definition: Requirements: Audit Policy : System > Audit Security State Change, Group Policy : Computer Configuration\Windows Settings\Security Settings\Advanced Audit Policy Configuration\Audit Policies\System\Audit Security State Change
- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal|T1070.006]]

## Detection

```yaml
selection:
  EventID: 4616
filter_main_svchost:
  ProcessName: C:\Windows\System32\svchost.exe
  SubjectUserSid: S-1-5-19
filter_optional_vmtools:
  ProcessName:
  - C:\Program Files\VMware\VMware Tools\vmtoolsd.exe
  - C:\Program Files (x86)\VMware\VMware Tools\vmtoolsd.exe
  - C:\Windows\System32\VBoxService.exe
  - C:\Windows\System32\oobe\msoobe.exe
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- HyperV or other virtualization technologies with binary not listed in filter portion of detection

## References

- Private Cuckoo Sandbox (from many years ago, no longer have hash, NDA as well)
- Live environment caused by malware
- https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4616

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_susp_time_modification.yml)
