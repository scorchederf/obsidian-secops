---
sigma_id: "c0e0bdec-3e3d-47aa-9974-05539c999c89"
title: "Registry Modification for OCI DLL Redirection"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_potential_oci_dll_redirection.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_potential_oci_dll_redirection.yml"
build_date: "2026-04-26 14:14:34"
status: "experimental"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "c0e0bdec-3e3d-47aa-9974-05539c999c89"
  - "Registry Modification for OCI DLL Redirection"
attack_technique_ids:
  - "T1112"
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Registry Modification for OCI DLL Redirection

Detects registry modifications related to 'OracleOciLib' and 'OracleOciLibPath' under 'MSDTC' settings.
Threat actors may modify these registry keys to redirect the loading of 'oci.dll' to a malicious DLL, facilitating phantom DLL hijacking via the MSDTC service.

## Metadata

- Rule ID: c0e0bdec-3e3d-47aa-9974-05539c999c89
- Status: experimental
- Level: high
- Author: Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2026-01-24
- Source Path: rules/windows/registry/registry_set/registry_set_potential_oci_dll_redirection.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1112-modify_registry|T1112]]
- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection_ocilib:
  TargetObject|endswith: \SOFTWARE\Microsoft\MSDTC\MTxOCI\OracleOciLib
filter_main_ocilib_file:
  Details|contains: oci.dll
selection_ocilibpath:
  TargetObject|endswith: \SOFTWARE\Microsoft\MSDTC\MTxOCI\OracleOciLibPath
filter_main_ocilibpath:
  Details|contains: '%SystemRoot%\System32\'
condition: (selection_ocilib and not filter_main_ocilib_file) or (selection_ocilibpath
  and not filter_main_ocilibpath)
```

## False Positives

- Unlikely

## References

- https://www.crowdstrike.com/en-us/blog/4-ways-adversaries-hijack-dlls/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_potential_oci_dll_redirection.yml)
