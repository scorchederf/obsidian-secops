---
sigma_id: "f50f3c09-557d-492d-81db-9064a8d4e211"
title: "Suspicious Execution Of Renamed Sysinternals Tools - Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_pua_sysinternals_renamed_execution_via_eula.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_pua_sysinternals_renamed_execution_via_eula.yml"
build_date: "2026-04-27 19:13:56"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "f50f3c09-557d-492d-81db-9064a8d4e211"
  - "Suspicious Execution Of Renamed Sysinternals Tools - Registry"
attack_technique_ids:
  - "T1588.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the creation of the "accepteula" key related to the Sysinternals tools being created from executables with the wrong name (e.g. a renamed Sysinternals tool)

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1588-obtain_capabilities#^t1588002-tool|T1588.002: Tool]]

## Detection

```yaml
selection:
  TargetObject|contains:
  - \Active Directory Explorer
  - \Handle
  - \LiveKd
  - \ProcDump
  - \Process Explorer
  - \PsExec
  - \PsLoggedon
  - \PsLoglist
  - \PsPasswd
  - \PsPing
  - \PsService
  - \SDelete
  TargetObject|endswith: \EulaAccepted
filter:
  Image|endswith:
  - \ADExplorer.exe
  - \ADExplorer64.exe
  - \handle.exe
  - \handle64.exe
  - \livekd.exe
  - \livekd64.exe
  - \procdump.exe
  - \procdump64.exe
  - \procexp.exe
  - \procexp64.exe
  - \PsExec.exe
  - \PsExec64.exe
  - \PsLoggedon.exe
  - \PsLoggedon64.exe
  - \psloglist.exe
  - \psloglist64.exe
  - \pspasswd.exe
  - \pspasswd64.exe
  - \PsPing.exe
  - \PsPing64.exe
  - \PsService.exe
  - \PsService64.exe
  - \sdelete.exe
condition: selection and not filter
```

## False Positives

- Unlikely

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_pua_sysinternals_renamed_execution_via_eula.yml)
