---
sigma_id: "9e3357ba-09d4-4fbd-a7c5-ad6386314513"
title: "Change the Fax Dll"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_fax_dll_persistance.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_fax_dll_persistance.yml"
build_date: "2026-04-27 19:13:50"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "9e3357ba-09d4-4fbd-a7c5-ad6386314513"
  - "Change the Fax Dll"
attack_technique_ids:
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detect possible persistence using Fax DLL load when service restart

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1112-modify_registry|T1112: Modify Registry]]

## Detection

```yaml
selection:
  TargetObject|contains|all:
  - \Software\Microsoft\Fax\Device Providers\
  - \ImageName
filter:
  Details: '%systemroot%\system32\fxst30.dll'
condition: selection and not filter
```

## False Positives

- Unknown

## References

- https://twitter.com/dottor_morte/status/1544652325570191361
- https://raw.githubusercontent.com/RiccardoAncarani/talks/master/F-Secure/unorthodox-lateral-movement.pdf

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_fax_dll_persistance.yml)
