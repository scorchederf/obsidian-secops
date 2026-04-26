---
sigma_id: "a2ea3ae7-d3d0-40a0-a55c-25a45c87cac1"
title: "Suspicious Driver Install by pnputil.exe"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_lolbin_susp_driver_installed_by_pnputil.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_susp_driver_installed_by_pnputil.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "a2ea3ae7-d3d0-40a0-a55c-25a45c87cac1"
  - "Suspicious Driver Install by pnputil.exe"
attack_technique_ids:
  - "T1547"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Driver Install by pnputil.exe

Detects when a possible suspicious driver is being installed via pnputil.exe lolbin

## Metadata

- Rule ID: a2ea3ae7-d3d0-40a0-a55c-25a45c87cac1
- Status: test
- Level: medium
- Author: Hai Vaknin @LuxNoBulIshit, Avihay eldad  @aloneliassaf, Austin Songer @austinsonger
- Date: 2021-09-30
- Modified: 2022-10-09
- Source Path: rules/windows/process_creation/proc_creation_win_lolbin_susp_driver_installed_by_pnputil.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547]]

## Detection

```yaml
selection:
  CommandLine|contains:
  - -i
  - /install
  - -a
  - /add-driver
  - '.inf'
  Image|endswith: \pnputil.exe
condition: selection
```

## False Positives

- Pnputil.exe being used may be performed by a system administrator.
- Verify whether the user identity, user agent, and/or hostname should be making changes in your environment.
- Pnputil.exe being executed from unfamiliar users should be investigated. If known behavior is causing false positives, it can be exempted from the rule.

## References

- https://learn.microsoft.com/en-us/windows-hardware/drivers/devtest/pnputil-command-syntax
- https://strontic.github.io/xcyclopedia/library/pnputil.exe-60EDC5E6BDBAEE441F2E3AEACD0340D2.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_susp_driver_installed_by_pnputil.yml)
