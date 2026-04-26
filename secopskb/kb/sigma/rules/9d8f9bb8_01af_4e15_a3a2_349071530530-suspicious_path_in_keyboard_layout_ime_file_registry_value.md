---
sigma_id: "9d8f9bb8-01af-4e15-a3a2-349071530530"
title: "Suspicious Path In Keyboard Layout IME File Registry Value"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_ime_suspicious_paths.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_ime_suspicious_paths.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "9d8f9bb8-01af-4e15-a3a2-349071530530"
  - "Suspicious Path In Keyboard Layout IME File Registry Value"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious Path In Keyboard Layout IME File Registry Value

Detects usage of Windows Input Method Editor (IME) keyboard layout feature, which allows an attacker to load a DLL into the process after sending the WM_INPUTLANGCHANGEREQUEST message.
Before doing this, the client needs to register the DLL in a special registry key that is assumed to implement this keyboard layout. This registry key should store a value named "Ime File" with a DLL path.
IMEs are essential for languages that have more characters than can be represented on a standard keyboard, such as Chinese, Japanese, and Korean.

## Metadata

- Rule ID: 9d8f9bb8-01af-4e15-a3a2-349071530530
- Status: test
- Level: high
- Author: X__Junior (Nextron Systems)
- Date: 2023-11-21
- Source Path: rules/windows/registry/registry_set/registry_set_ime_suspicious_paths.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection_registry:
  TargetObject|contains|all:
  - \Control\Keyboard Layouts\
  - Ime File
selection_folders_1:
  Details|contains:
  - :\Perflogs\
  - :\Users\Public\
  - :\Windows\Temp\
  - \AppData\Local\Temp\
  - \AppData\Roaming\
  - \Temporary Internet
selection_folders_2:
- Details|contains|all:
  - :\Users\
  - \Favorites\
- Details|contains|all:
  - :\Users\
  - \Favourites\
- Details|contains|all:
  - :\Users\
  - \Contacts\
condition: selection_registry and 1 of selection_folders_*
```

## False Positives

- Unknown

## References

- https://www.linkedin.com/pulse/guntior-story-advanced-bootkit-doesnt-rely-windows-disk-baranov-wue8e/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_ime_suspicious_paths.yml)
