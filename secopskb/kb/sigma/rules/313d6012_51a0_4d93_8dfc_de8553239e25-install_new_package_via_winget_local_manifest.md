---
sigma_id: "313d6012-51a0-4d93-8dfc-de8553239e25"
title: "Install New Package Via Winget Local Manifest"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_winget_local_install_via_manifest.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_winget_local_install_via_manifest.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "313d6012-51a0-4d93-8dfc-de8553239e25"
  - "Install New Package Via Winget Local Manifest"
attack_technique_ids:
  - "T1059"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Install New Package Via Winget Local Manifest

Detects usage of winget to install applications via manifest file. Adversaries can abuse winget to download payloads remotely and execute them.
The manifest option enables you to install an application by passing in a YAML file directly to the client.
Winget can be used to download and install exe, msi or msix files later.

## Metadata

- Rule ID: 313d6012-51a0-4d93-8dfc-de8553239e25
- Status: test
- Level: medium
- Author: Sreeman, Florian Roth (Nextron Systems), frack113
- Date: 2020-04-21
- Modified: 2023-04-17
- Source Path: rules/windows/process_creation/proc_creation_win_winget_local_install_via_manifest.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]

## Detection

```yaml
selection_img:
- Image|endswith: \winget.exe
- OriginalFileName: winget.exe
selection_install_flag:
  CommandLine|contains:
  - install
  - ' add '
selection_manifest_flag:
  CommandLine|contains:
  - '-m '
  - --manifest
condition: all of selection_*
```

## False Positives

- Some false positives are expected in some environment that may use this functionality to install and test their custom applications

## References

- https://learn.microsoft.com/en-us/windows/package-manager/winget/install#local-install
- https://lolbas-project.github.io/lolbas/Binaries/Winget/
- https://github.com/nasbench/Misc-Research/tree/b9596e8109dcdb16ec353f316678927e507a5b8d/LOLBINs/Winget

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_winget_local_install_via_manifest.yml)
