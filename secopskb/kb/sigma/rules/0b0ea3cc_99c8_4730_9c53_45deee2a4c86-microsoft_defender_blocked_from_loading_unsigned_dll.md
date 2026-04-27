---
sigma_id: "0b0ea3cc-99c8-4730-9c53-45deee2a4c86"
title: "Microsoft Defender Blocked from Loading Unsigned DLL"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security_mitigations/win_security_mitigations_defender_load_unsigned_dll.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security_mitigations/win_security_mitigations_defender_load_unsigned_dll.yml"
build_date: "2026-04-27 19:13:53"
status: "test"
level: "high"
logsource: "windows / security-mitigations"
aliases:
  - "0b0ea3cc-99c8-4730-9c53-45deee2a4c86"
  - "Microsoft Defender Blocked from Loading Unsigned DLL"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects Code Integrity (CI) engine blocking Microsoft Defender's processes (MpCmdRun and NisSrv) from loading unsigned DLLs which may be an attempt to sideload arbitrary DLL

## Logsource

- product: windows
- service: security-mitigations

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow#^t1574001-dll|T1574.001: DLL]]

## Detection

```yaml
selection:
  EventID:
  - 11
  - 12
  ProcessPath|endswith:
  - \MpCmdRun.exe
  - \NisSrv.exe
condition: selection
```

## False Positives

- Unknown

## References

- https://www.sentinelone.com/blog/living-off-windows-defender-lockbit-ransomware-sideloads-cobalt-strike-through-microsoft-security-tool

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security_mitigations/win_security_mitigations_defender_load_unsigned_dll.yml)
