---
sigma_id: "46490193-1b22-4c29-bdd6-5bf63907216f"
title: "VBScript Payload Stored in Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_vbs_payload_stored.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_vbs_payload_stored.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "46490193-1b22-4c29-bdd6-5bf63907216f"
  - "VBScript Payload Stored in Registry"
attack_technique_ids:
  - "T1547.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# VBScript Payload Stored in Registry

Detects VBScript content stored into registry keys as seen being used by UNC2452 group

## Metadata

- Rule ID: 46490193-1b22-4c29-bdd6-5bf63907216f
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2021-03-05
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_vbs_payload_stored.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.001]]

## Detection

```yaml
selection:
  TargetObject|contains: Software\Microsoft\Windows\CurrentVersion
  Details|contains:
  - 'vbscript:'
  - 'jscript:'
  - mshtml,
  - RunHTMLApplication
  - Execute(
  - CreateObject
  - window.close
filter:
  TargetObject|contains: Software\Microsoft\Windows\CurrentVersion\Run
filter_dotnet:
  Image|endswith: \msiexec.exe
  TargetObject|contains: \SOFTWARE\Microsoft\Windows\CurrentVersion\Installer\UserData\
  Details|contains:
  - \Microsoft.NET\Primary Interop Assemblies\Microsoft.mshtml.dll
  - <\Microsoft.mshtml,fileVersion=
  - _mshtml_dll_
  - <\Microsoft.mshtml,culture=
condition: selection and not 1 of filter*
```

## False Positives

- Unknown

## References

- https://www.microsoft.com/security/blog/2021/03/04/goldmax-goldfinder-sibot-analyzing-nobelium-malware/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_vbs_payload_stored.yml)
