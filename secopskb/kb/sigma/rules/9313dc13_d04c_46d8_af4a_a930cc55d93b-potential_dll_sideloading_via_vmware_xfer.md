---
sigma_id: "9313dc13-d04c-46d8-af4a-a930cc55d93b"
title: "Potential DLL Sideloading Via VMware Xfer"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_side_load_vmware_xfer.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_vmware_xfer.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "windows / image_load"
aliases:
  - "9313dc13-d04c-46d8-af4a-a930cc55d93b"
  - "Potential DLL Sideloading Via VMware Xfer"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potential DLL Sideloading Via VMware Xfer

Detects loading of a DLL by the VMware Xfer utility from the non-default directory which may be an attempt to sideload arbitrary DLL

## Metadata

- Rule ID: 9313dc13-d04c-46d8-af4a-a930cc55d93b
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-02
- Modified: 2023-02-17
- Source Path: rules/windows/image_load/image_load_side_load_vmware_xfer.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection:
  Image|endswith: \VMwareXferlogs.exe
  ImageLoaded|endswith: \glib-2.0.dll
filter:
  ImageLoaded|startswith: C:\Program Files\VMware\
condition: selection and not filter
```

## False Positives

- Unlikely

## References

- https://www.sentinelone.com/labs/lockbit-ransomware-side-loads-cobalt-strike-beacon-with-legitimate-vmware-utility/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_vmware_xfer.yml)
