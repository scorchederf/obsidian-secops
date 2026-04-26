---
sigma_id: "e76c8240-d68f-4773-8880-5c6f63595aaf"
title: "Time Travel Debugging Utility Usage - Image"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_dll_tttracer_module_load.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_dll_tttracer_module_load.yml"
build_date: "2026-04-26 15:01:53"
status: "test"
level: "high"
logsource: "windows / image_load"
aliases:
  - "e76c8240-d68f-4773-8880-5c6f63595aaf"
  - "Time Travel Debugging Utility Usage - Image"
attack_technique_ids:
  - "T1218"
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Time Travel Debugging Utility Usage - Image

Detects usage of Time Travel Debugging Utility. Adversaries can execute malicious processes and dump processes, such as lsass.exe, via tttracer.exe.

## Metadata

- Rule ID: e76c8240-d68f-4773-8880-5c6f63595aaf
- Status: test
- Level: high
- Author: Ensar Şamil, @sblmsrsn, @oscd_initiative
- Date: 2020-10-06
- Modified: 2022-12-02
- Source Path: rules/windows/image_load/image_load_dll_tttracer_module_load.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]
- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]

## Detection

```yaml
selection:
  ImageLoaded|endswith:
  - \ttdrecord.dll
  - \ttdwriter.dll
  - \ttdloader.dll
condition: selection
```

## False Positives

- Legitimate usage by software developers/testers

## References

- https://lolbas-project.github.io/lolbas/Binaries/Tttracer/
- https://twitter.com/mattifestation/status/1196390321783025666
- https://twitter.com/oulusoyum/status/1191329746069655553

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_dll_tttracer_module_load.yml)
