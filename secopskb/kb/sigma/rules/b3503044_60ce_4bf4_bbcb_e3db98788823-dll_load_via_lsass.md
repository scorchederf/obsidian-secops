---
sigma_id: "b3503044-60ce-4bf4-bbcb-e3db98788823"
title: "DLL Load via LSASS"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_event/registry_event_susp_lsass_dll_load.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_susp_lsass_dll_load.yml"
build_date: "2026-04-26 15:01:44"
status: "test"
level: "high"
logsource: "windows / registry_event"
aliases:
  - "b3503044-60ce-4bf4-bbcb-e3db98788823"
  - "DLL Load via LSASS"
attack_technique_ids:
  - "T1547.008"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# DLL Load via LSASS

Detects a method to load DLL via LSASS process using an undocumented Registry key

## Metadata

- Rule ID: b3503044-60ce-4bf4-bbcb-e3db98788823
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2019-10-16
- Modified: 2022-04-21
- Source Path: rules/windows/registry/registry_event/registry_event_susp_lsass_dll_load.yml

## Logsource

- category: registry_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.008]]

## Detection

```yaml
selection:
  TargetObject|contains:
  - \CurrentControlSet\Services\NTDS\DirectoryServiceExtPt
  - \CurrentControlSet\Services\NTDS\LsaDbExtPt
filter_domain_controller:
  Image: C:\Windows\system32\lsass.exe
  Details:
  - '%%systemroot%%\system32\ntdsa.dll'
  - '%%systemroot%%\system32\lsadb.dll'
condition: selection and not 1 of filter_*
```

## False Positives

- Unknown

## References

- https://blog.xpnsec.com/exploring-mimikatz-part-1/
- https://twitter.com/SBousseaden/status/1183745981189427200

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_susp_lsass_dll_load.yml)
