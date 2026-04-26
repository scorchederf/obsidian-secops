---
sigma_id: "4eec988f-7bf0-49f1-8675-1e6a510b3a2a"
title: "Potential PendingFileRenameOperations Tampering"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_susp_pendingfilerenameoperations.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_susp_pendingfilerenameoperations.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "4eec988f-7bf0-49f1-8675-1e6a510b3a2a"
  - "Potential PendingFileRenameOperations Tampering"
attack_technique_ids:
  - "T1036.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential PendingFileRenameOperations Tampering

Detect changes to the "PendingFileRenameOperations" registry key from uncommon or suspicious images locations to stage currently used files for rename or deletion after reboot.

## Metadata

- Rule ID: 4eec988f-7bf0-49f1-8675-1e6a510b3a2a
- Status: test
- Level: medium
- Author: frack113
- Date: 2023-01-27
- Modified: 2025-10-07
- Source Path: rules/windows/registry/registry_set/registry_set_susp_pendingfilerenameoperations.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036.003]]

## Detection

```yaml
selection_main:
  TargetObject|contains: \CurrentControlSet\Control\Session Manager\PendingFileRenameOperations
selection_susp_paths:
  Image|contains: \Users\Public\
selection_susp_images:
  Image|endswith:
  - \reg.exe
  - \regedit.exe
condition: selection_main and 1 of selection_susp_*
```

## False Positives

- Installers and updaters may set currently in use files for rename or deletion after a reboot.

## References

- https://any.run/report/3ecd4763ffc944fdc67a9027e459cd4f448b1a8d1b36147977afaf86bbf2a261/64b0ba45-e7ce-423b-9a1d-5b4ea59521e6
- https://devblogs.microsoft.com/scripting/determine-pending-reboot-statuspowershell-style-part-1/
- https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/cc960241(v=technet.10)?redirectedfrom=MSDN
- https://www.trendmicro.com/en_us/research/21/j/purplefox-adds-new-backdoor-that-uses-websockets.html
- https://www.trendmicro.com/en_us/research/19/i/purple-fox-fileless-malware-with-rookit-component-delivered-by-rig-exploit-kit-now-abuses-powershell.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_susp_pendingfilerenameoperations.yml)
