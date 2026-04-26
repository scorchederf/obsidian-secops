---
sigma_id: "eeb30123-9fbd-4ee8-aaa0-2e545bbed6dc"
title: "Security Support Provider (SSP) Added to LSA Configuration"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_event/registry_event_ssp_added_lsa_config.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_ssp_added_lsa_config.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "high"
logsource: "windows / registry_event"
aliases:
  - "eeb30123-9fbd-4ee8-aaa0-2e545bbed6dc"
  - "Security Support Provider (SSP) Added to LSA Configuration"
attack_technique_ids:
  - "T1547.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Security Support Provider (SSP) Added to LSA Configuration

Detects the addition of a SSP to the registry. Upon a reboot or API call, SSP DLLs gain access to encrypted and plaintext passwords stored in Windows.

## Metadata

- Rule ID: eeb30123-9fbd-4ee8-aaa0-2e545bbed6dc
- Status: test
- Level: high
- Author: iwillkeepwatch
- Date: 2019-01-18
- Modified: 2026-03-30
- Source Path: rules/windows/registry/registry_event/registry_event_ssp_added_lsa_config.yml

## Logsource

- category: registry_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.005]]

## Detection

```yaml
selection:
  TargetObject|endswith:
  - \Control\Lsa\Security Packages
  - \Control\Lsa\OSConfig\Security Packages
filter_main_msiexec:
  Image:
  - C:\Windows\system32\msiexec.exe
  - C:\Windows\syswow64\MsiExec.exe
filter_main_image_null:
  Image: null
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://powersploit.readthedocs.io/en/latest/Persistence/Install-SSP/
- https://github.com/EmpireProject/Empire/blob/08cbd274bef78243d7a8ed6443b8364acd1fc48b/data/module_source/persistence/Install-SSP.ps1#L157

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_ssp_added_lsa_config.yml)
