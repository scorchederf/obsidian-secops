---
sigma_id: "c7da8edc-49ae-45a2-9e61-9fd860e4e73d"
title: "PUA - Sysinternals Tools Execution - Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_pua_sysinternals_susp_execution_via_eula.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_pua_sysinternals_susp_execution_via_eula.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "c7da8edc-49ae-45a2-9e61-9fd860e4e73d"
  - "PUA - Sysinternals Tools Execution - Registry"
attack_technique_ids:
  - "T1588.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PUA - Sysinternals Tools Execution - Registry

Detects the execution of some potentially unwanted tools such as PsExec, Procdump, etc. (part of the Sysinternals suite) via the creation of the "accepteula" registry key.

## Metadata

- Rule ID: c7da8edc-49ae-45a2-9e61-9fd860e4e73d
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-24
- Modified: 2025-10-26
- Source Path: rules/windows/registry/registry_set/registry_set_pua_sysinternals_susp_execution_via_eula.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1588-obtain_capabilities|T1588.002]]

## Detection

```yaml
selection:
  TargetObject|contains:
  - \Active Directory Explorer
  - \Handle
  - \LiveKd
  - \Process Explorer
  - \ProcDump
  - \PsExec
  - \PsLoglist
  - \PsPasswd
  - \SDelete
  - \Sysinternals
  TargetObject|endswith: \EulaAccepted
condition: selection
```

## False Positives

- Legitimate use of SysInternals tools. Filter the legitimate paths used in your environment

## References

- https://twitter.com/Moti_B/status/1008587936735035392

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_pua_sysinternals_susp_execution_via_eula.yml)
