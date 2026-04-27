---
sigma_id: "bf4fc428-dcc3-4bbd-99fe-2422aeee2544"
title: "ETW Logging Disabled In .NET Processes - Sysmon Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_dot_net_etw_tamper.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_dot_net_etw_tamper.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "bf4fc428-dcc3-4bbd-99fe-2422aeee2544"
  - "ETW Logging Disabled In .NET Processes - Sysmon Registry"
attack_technique_ids:
  - "T1112"
  - "T1562"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# ETW Logging Disabled In .NET Processes - Sysmon Registry

Potential adversaries stopping ETW providers recording loaded .NET assemblies.

## Metadata

- Rule ID: bf4fc428-dcc3-4bbd-99fe-2422aeee2544
- Status: test
- Level: high
- Author: Roberto Rodriguez (Cyb3rWard0g), OTR (Open Threat Research)
- Date: 2020-06-05
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_dot_net_etw_tamper.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1112-modify_registry|T1112]]
- [[kb/attack/techniques/T1562-impair_defenses|T1562]]

## Detection

```yaml
selection_etw_enabled:
  TargetObject|endswith: SOFTWARE\Microsoft\.NETFramework\ETWEnabled
  Details: DWORD (0x00000000)
selection_complus:
  TargetObject|endswith:
  - \COMPlus_ETWEnabled
  - \COMPlus_ETWFlags
  Details:
  - 0
  - DWORD (0x00000000)
condition: 1 of selection_*
```

## False Positives

- Unknown

## References

- https://twitter.com/_xpn_/status/1268712093928378368
- https://social.msdn.microsoft.com/Forums/vstudio/en-US/0878832e-39d7-4eaf-8e16-a729c4c40975/what-can-i-use-e13c0d23ccbc4e12931bd9cc2eee27e4-for?forum=clr
- https://github.com/dotnet/runtime/blob/ee2355c801d892f2894b0f7b14a20e6cc50e0e54/docs/design/coreclr/jit/viewing-jit-dumps.md#setting-configuration-variables
- https://github.com/dotnet/runtime/blob/f62e93416a1799aecc6b0947adad55a0d9870732/src/coreclr/src/inc/clrconfigvalues.h#L35-L38
- https://github.com/dotnet/runtime/blob/7abe42dc1123722ed385218268bb9fe04556e3d3/src/coreclr/src/inc/clrconfig.h#L33-L39
- https://github.com/dotnet/runtime/search?p=1&q=COMPlus_&unscoped_q=COMPlus_
- https://bunnyinside.com/?term=f71e8cb9c76a
- http://managed670.rssing.com/chan-5590147/all_p1.html
- https://github.com/dotnet/runtime/blob/4f9ae42d861fcb4be2fcd5d3d55d5f227d30e723/docs/coding-guidelines/clr-jit-coding-conventions.md#1412-disabling-code
- https://blog.xpnsec.com/hiding-your-dotnet-complus-etwenabled/
- https://i.blackhat.com/EU-21/Wednesday/EU-21-Teodorescu-Veni-No-Vidi-No-Vici-Attacks-On-ETW-Blind-EDRs.pdf

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_dot_net_etw_tamper.yml)
