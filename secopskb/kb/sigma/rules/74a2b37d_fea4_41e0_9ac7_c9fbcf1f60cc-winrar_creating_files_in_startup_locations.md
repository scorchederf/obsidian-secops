---
sigma_id: "74a2b37d-fea4-41e0-9ac7-c9fbcf1f60cc"
title: "WinRAR Creating Files in Startup Locations"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_winrar_file_creation_in_startup_folder.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_winrar_file_creation_in_startup_folder.yml"
build_date: "2026-04-27 19:13:59"
status: "experimental"
level: "high"
logsource: "windows / file_event"
aliases:
  - "74a2b37d-fea4-41e0-9ac7-c9fbcf1f60cc"
  - "WinRAR Creating Files in Startup Locations"
attack_technique_ids:
  - "T1547.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects WinRAR creating files in Windows startup locations, which may indicate an attempt to establish persistence by adding malicious files to the Startup folder.
This kind of behaviour has been associated with exploitation of WinRAR path traversal vulnerability CVE-2025-6218 or CVE-2025-8088.

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution#^t1547001-registry-run-keys---startup-folder|T1547.001: Registry Run Keys / Startup Folder]]

## Detection

```yaml
selection:
  Image|endswith:
  - \WinRAR.exe
  - \Rar.exe
  TargetFilename|contains: \Start Menu\Programs\Startup\
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/mulwareX/CVE-2025-6218-POC
- https://x.com/0x534c/status/1944694507787710685
- https://www.welivesecurity.com/en/eset-research/update-winrar-tools-now-romcom-and-others-exploiting-zero-day-vulnerability/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_winrar_file_creation_in_startup_folder.yml)
