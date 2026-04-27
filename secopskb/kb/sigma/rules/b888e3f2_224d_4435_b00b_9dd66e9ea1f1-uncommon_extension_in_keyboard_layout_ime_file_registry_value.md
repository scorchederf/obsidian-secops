---
sigma_id: "b888e3f2-224d-4435-b00b-9dd66e9ea1f1"
title: "Uncommon Extension In Keyboard Layout IME File Registry Value"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_ime_non_default_extension.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_ime_non_default_extension.yml"
build_date: "2026-04-27 19:13:58"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "b888e3f2-224d-4435-b00b-9dd66e9ea1f1"
  - "Uncommon Extension In Keyboard Layout IME File Registry Value"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects usage of Windows Input Method Editor (IME) keyboard layout feature, which allows an attacker to load a DLL into the process after sending the WM_INPUTLANGCHANGEREQUEST message.
Before doing this, the client needs to register the DLL in a special registry key that is assumed to implement this keyboard layout. This registry key should store a value named "Ime File" with a DLL path.
IMEs are essential for languages that have more characters than can be represented on a standard keyboard, such as Chinese, Japanese, and Korean.

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses#^t1562001-disable-or-modify-tools|T1562.001: Disable or Modify Tools]]

## Detection

```yaml
selection:
  TargetObject|contains|all:
  - \Control\Keyboard Layouts\
  - Ime File
filter_main_known_extension:
  Details|endswith: .ime
condition: selection and not 1 of filter_main_*
```

## False Positives

- IMEs are essential for languages that have more characters than can be represented on a standard keyboard, such as Chinese, Japanese, and Korean.

## References

- https://www.linkedin.com/pulse/guntior-story-advanced-bootkit-doesnt-rely-windows-disk-baranov-wue8e/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_ime_non_default_extension.yml)
