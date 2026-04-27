---
sigma_id: "0a13e132-651d-11eb-ae93-0242ac130002"
title: "Audit Policy Tampering Via Auditpol"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_auditpol_susp_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_auditpol_susp_execution.yml"
build_date: "2026-04-27 19:13:50"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "0a13e132-651d-11eb-ae93-0242ac130002"
  - "Audit Policy Tampering Via Auditpol"
attack_technique_ids:
  - "T1562.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Threat actors can use auditpol binary to change audit policy configuration to impair detection capability.
This can be carried out by selectively disabling/removing certain audit policies as well as restoring a custom policy owned by the threat actor.

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses#^t1562002-disable-windows-event-logging|T1562.002: Disable Windows Event Logging]]

## Detection

```yaml
selection_img:
- Image|endswith: \auditpol.exe
- OriginalFileName: AUDITPOL.EXE
selection_cli:
  CommandLine|contains:
  - disable
  - clear
  - remove
  - restore
condition: all of selection_*
```

## False Positives

- Administrator or administrator scripts might leverage the flags mentioned in the detection section. Either way, it should always be monitored

## References

- https://www.microsoft.com/security/blog/2021/01/20/deep-dive-into-the-solorigate-second-stage-activation-from-sunburst-to-teardrop-and-raindrop/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_auditpol_susp_execution.yml)
