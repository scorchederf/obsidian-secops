---
sigma_id: "28036918-04d3-423d-91c0-55ecf99fb892"
title: "NET NGenAssemblyUsageLog Registry Key Tamper"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_net_cli_ngenassemblyusagelog.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_net_cli_ngenassemblyusagelog.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "28036918-04d3-423d-91c0-55ecf99fb892"
  - "NET NGenAssemblyUsageLog Registry Key Tamper"
attack_technique_ids:
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# NET NGenAssemblyUsageLog Registry Key Tamper

Detects changes to the NGenAssemblyUsageLog registry key.
.NET Usage Log output location can be controlled by setting the NGenAssemblyUsageLog CLR configuration knob in the Registry or by configuring an environment variable (as described in the next section).
By simplify specifying an arbitrary value (e.g. fake output location or junk data) for the expected value, a Usage Log file for the .NET execution context will not be created.

## Metadata

- Rule ID: 28036918-04d3-423d-91c0-55ecf99fb892
- Status: test
- Level: high
- Author: frack113
- Date: 2022-11-18
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_net_cli_ngenassemblyusagelog.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Detection

```yaml
selection:
  TargetObject|endswith: SOFTWARE\Microsoft\.NETFramework\NGenAssemblyUsageLog
condition: selection
```

## False Positives

- Unknown

## References

- https://bohops.com/2021/03/16/investigating-net-clr-usage-log-tampering-techniques-for-edr-evasion/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_net_cli_ngenassemblyusagelog.yml)
