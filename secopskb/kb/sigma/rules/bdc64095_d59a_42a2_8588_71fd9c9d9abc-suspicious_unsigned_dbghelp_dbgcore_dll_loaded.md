---
sigma_id: "bdc64095-d59a-42a2-8588-71fd9c9d9abc"
title: "Suspicious Unsigned Dbghelp/Dbgcore DLL Loaded"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_dll_dbghelp_dbgcore_unsigned_load.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_dll_dbghelp_dbgcore_unsigned_load.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / image_load"
aliases:
  - "bdc64095-d59a-42a2-8588-71fd9c9d9abc"
  - "Suspicious Unsigned Dbghelp/Dbgcore DLL Loaded"
attack_technique_ids:
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Suspicious Unsigned Dbghelp/Dbgcore DLL Loaded

Detects the load of dbghelp/dbgcore DLL (used to make memory dumps) by suspicious processes.
Tools like ProcessHacker and some attacker tradecract use MiniDumpWriteDump API found in dbghelp.dll or dbgcore.dll.
As an example, SilentTrynity C2 Framework has a module that leverages this API to dump the contents of Lsass.exe and transfer it over the network back to the attacker's machine.

## Metadata

- Rule ID: bdc64095-d59a-42a2-8588-71fd9c9d9abc
- Status: test
- Level: high
- Author: Perez Diego (@darkquassar), oscd.community, Ecco
- Date: 2019-10-27
- Modified: 2022-12-09
- Source Path: rules/windows/image_load/image_load_dll_dbghelp_dbgcore_unsigned_load.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]

## Detection

```yaml
selection:
  ImageLoaded|endswith:
  - \dbghelp.dll
  - \dbgcore.dll
  Signed: 'false'
condition: selection
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/windows/win32/api/minidumpapiset/nf-minidumpapiset-minidumpwritedump
- https://www.pinvoke.net/default.aspx/dbghelp/MiniDumpWriteDump.html
- https://medium.com/@fsx30/bypass-edrs-memory-protection-introduction-to-hooking-2efb21acffd6

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_dll_dbghelp_dbgcore_unsigned_load.yml)
