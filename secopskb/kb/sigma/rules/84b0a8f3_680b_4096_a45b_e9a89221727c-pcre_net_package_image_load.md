---
sigma_id: "84b0a8f3-680b-4096-a45b-e9a89221727c"
title: "PCRE.NET Package Image Load"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_dll_pcre_dotnet_dll_load.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_dll_pcre_dotnet_dll_load.yml"
build_date: "2026-04-27 19:13:53"
status: "test"
level: "high"
logsource: "windows / image_load"
aliases:
  - "84b0a8f3-680b-4096-a45b-e9a89221727c"
  - "PCRE.NET Package Image Load"
attack_technique_ids:
  - "T1059"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects processes loading modules related to PCRE.NET package

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059: Command and Scripting Interpreter]]

## Detection

```yaml
selection:
  ImageLoaded|contains: \AppData\Local\Temp\ba9ea7344a4a5f591d6e5dc32a13494b\
condition: selection
```

## False Positives

- Unknown

## References

- https://twitter.com/rbmaslen/status/1321859647091970051
- https://twitter.com/tifkin_/status/1321916444557365248

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_dll_pcre_dotnet_dll_load.yml)
