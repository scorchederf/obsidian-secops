---
sigma_id: "c6c56ada-612b-42d1-9a29-adad3c5c2c1e"
title: "Audit Policy Tampering Via NT Resource Kit Auditpol"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_auditpol_nt_resource_kit_usage.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_auditpol_nt_resource_kit_usage.yml"
build_date: "2026-04-27 19:13:50"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Threat actors can use an older version of the auditpol binary available inside the NT resource kit to change audit policy configuration to impair detection capability.
This can be carried out by selectively disabling/removing certain audit policies as well as restoring a custom policy owned by the threat actor.

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses#^t1562002-disable-windows-event-logging|T1562.002: Disable Windows Event Logging]]

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
