---
sigma_id: "4508a70e-97ef-4300-b62b-ff27992990ea"
title: "DotNet CLR DLL Loaded By Scripting Applications"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_susp_script_dotnet_clr_dll_load.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_susp_script_dotnet_clr_dll_load.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "windows / image_load"
aliases:
  - "4508a70e-97ef-4300-b62b-ff27992990ea"
  - "DotNet CLR DLL Loaded By Scripting Applications"
attack_technique_ids:
  - "T1055"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# DotNet CLR DLL Loaded By Scripting Applications

Detects .NET CLR DLLs being loaded by scripting applications such as wscript or cscript. This could be an indication of potential suspicious execution.

## Metadata

- Rule ID: 4508a70e-97ef-4300-b62b-ff27992990ea
- Status: test
- Level: high
- Author: omkar72, oscd.community
- Date: 2020-10-14
- Modified: 2023-02-23
- Source Path: rules/windows/image_load/image_load_susp_script_dotnet_clr_dll_load.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1055-process_injection|T1055]]

## Detection

```yaml
selection:
  Image|endswith:
  - \cmstp.exe
  - \cscript.exe
  - \mshta.exe
  - \msxsl.exe
  - \regsvr32.exe
  - \wmic.exe
  - \wscript.exe
  ImageLoaded|endswith:
  - \clr.dll
  - \mscoree.dll
  - \mscorlib.dll
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/tyranid/DotNetToJScript
- https://thewover.github.io/Introducing-Donut/
- https://web.archive.org/web/20230329154538/https://blog.menasec.net/2019/07/interesting-difr-traces-of-net-clr.html
- https://web.archive.org/web/20221026202428/https://gist.github.com/code-scrap/d7f152ffcdb3e0b02f7f394f5187f008

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_susp_script_dotnet_clr_dll_load.yml)
