---
sigma_id: "8023f872-3f1d-4301-a384-801889917ab4"
title: "Usage of Renamed Sysinternals Tools - RegistrySet"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_renamed_sysinternals_eula_accepted.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_renamed_sysinternals_eula_accepted.yml"
build_date: "2026-04-27 19:13:58"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "8023f872-3f1d-4301-a384-801889917ab4"
  - "Usage of Renamed Sysinternals Tools - RegistrySet"
attack_technique_ids:
  - "T1588.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects non-sysinternals tools setting the "accepteula" key which normally is set on sysinternals tool execution

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
  - \PsExec
  - \ProcDump
  - \Handle
  - \LiveKd
  - \Process Explorer
  - \PsLoglist
  - \PsPasswd
  - \Active Directory Explorer
  TargetObject|endswith: \EulaAccepted
filter_main_image_names:
  Image|endswith:
  - \PsExec.exe
  - \PsExec64.exe
  - \procdump.exe
  - \procdump64.exe
  - \handle.exe
  - \handle64.exe
  - \livekd.exe
  - \livekd64.exe
  - \procexp.exe
  - \procexp64.exe
  - \psloglist.exe
  - \psloglist64.exe
  - \pspasswd.exe
  - \pspasswd64.exe
  - \ADExplorer.exe
  - \ADExplorer64.exe
filter_optional_null:
  Image: null
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Unlikely

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_renamed_sysinternals_eula_accepted.yml)
