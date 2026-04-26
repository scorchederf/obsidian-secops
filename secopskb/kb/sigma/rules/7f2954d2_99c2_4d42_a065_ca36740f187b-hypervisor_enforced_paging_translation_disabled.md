---
sigma_id: "7f2954d2-99c2-4d42-a065-ca36740f187b"
title: "Hypervisor Enforced Paging Translation Disabled"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_deviceguard_hypervisorenforcedpagingtranslation_disabled.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_deviceguard_hypervisorenforcedpagingtranslation_disabled.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "7f2954d2-99c2-4d42-a065-ca36740f187b"
  - "Hypervisor Enforced Paging Translation Disabled"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Hypervisor Enforced Paging Translation Disabled

Detects changes to the "DisableHypervisorEnforcedPagingTranslation" registry value. Where the it is set to "1" in order to disable the Hypervisor Enforced Paging Translation feature.

## Metadata

- Rule ID: 7f2954d2-99c2-4d42-a065-ca36740f187b
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2024-07-05
- Source Path: rules/windows/registry/registry_set/registry_set_deviceguard_hypervisorenforcedpagingtranslation_disabled.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection:
  TargetObject|endswith: \DisableHypervisorEnforcedPagingTranslation
  Details: DWORD (0x00000001)
condition: selection
```

## False Positives

- Unknown

## References

- https://twitter.com/standa_t/status/1808868985678803222
- https://github.com/AaLl86/WindowsInternals/blob/070dc4f317726dfb6ffd2b7a7c121a33a8659b5e/Slides/Hypervisor-enforced%20Paging%20Translation%20-%20The%20end%20of%20non%20data-driven%20Kernel%20Exploits%20(Recon2024).pdf

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_deviceguard_hypervisorenforcedpagingtranslation_disabled.yml)
