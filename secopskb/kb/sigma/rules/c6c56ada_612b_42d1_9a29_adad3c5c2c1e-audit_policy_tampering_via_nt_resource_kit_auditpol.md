---
sigma_id: "c6c56ada-612b-42d1-9a29-adad3c5c2c1e"
title: "Audit Policy Tampering Via NT Resource Kit Auditpol"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_auditpol_nt_resource_kit_usage.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_auditpol_nt_resource_kit_usage.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "c6c56ada-612b-42d1-9a29-adad3c5c2c1e"
  - "Audit Policy Tampering Via NT Resource Kit Auditpol"
attack_technique_ids:
  - "T1562.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Audit Policy Tampering Via NT Resource Kit Auditpol

Threat actors can use an older version of the auditpol binary available inside the NT resource kit to change audit policy configuration to impair detection capability.
This can be carried out by selectively disabling/removing certain audit policies as well as restoring a custom policy owned by the threat actor.

## Metadata

- Rule ID: c6c56ada-612b-42d1-9a29-adad3c5c2c1e
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2021-12-18
- Modified: 2023-02-21
- Source Path: rules/windows/process_creation/proc_creation_win_auditpol_nt_resource_kit_usage.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.002]]

## Detection

```yaml
selection:
  CommandLine|contains:
  - /logon:none
  - /system:none
  - /sam:none
  - /privilege:none
  - /object:none
  - /process:none
  - /policy:none
condition: selection
```

## False Positives

- The old auditpol utility isn't available by default on recent versions of Windows as it was replaced by a newer version. The FP rate should be very low except for tools that use a similar flag structure

## References

- https://github.com/3CORESec/MAL-CL/tree/master/Descriptors/Windows%202000%20Resource%20Kit%20Tools/AuditPol

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_auditpol_nt_resource_kit_usage.yml)
