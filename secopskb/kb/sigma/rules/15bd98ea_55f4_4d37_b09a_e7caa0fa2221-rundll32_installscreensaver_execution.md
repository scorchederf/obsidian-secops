---
sigma_id: "15bd98ea-55f4-4d37-b09a-e7caa0fa2221"
title: "Rundll32 InstallScreenSaver Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_rundll32_installscreensaver.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_installscreensaver.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "15bd98ea-55f4-4d37-b09a-e7caa0fa2221"
  - "Rundll32 InstallScreenSaver Execution"
attack_technique_ids:
  - "T1218.011"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Rundll32 InstallScreenSaver Execution

An attacker may execute an application as a SCR File using rundll32.exe desk.cpl,InstallScreenSaver

## Metadata

- Rule ID: 15bd98ea-55f4-4d37-b09a-e7caa0fa2221
- Status: test
- Level: medium
- Author: Christopher Peacock @securepeacock, SCYTHE @scythe_io, TactiKoolSec
- Date: 2022-04-28
- Modified: 2023-02-09
- Source Path: rules/windows/process_creation/proc_creation_win_rundll32_installscreensaver.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.011]]

## Detection

```yaml
selection_img:
- Image|endswith: \rundll32.exe
- OriginalFileName: RUNDLL32.EXE
selection_cli:
  CommandLine|contains: InstallScreenSaver
condition: all of selection_*
```

## False Positives

- Legitimate installation of a new screensaver

## References

- https://lolbas-project.github.io/lolbas/Libraries/Desk/
- https://github.com/redcanaryco/atomic-red-team/blob/0f229c0e42bfe7ca736a14023836d65baa941ed2/atomics/T1218.011/T1218.011.md#atomic-test-13---rundll32-with-deskcpl

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_installscreensaver.yml)
