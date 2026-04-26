---
sigma_id: "dcff7e85-d01f-4eb5-badd-84e2e6be8294"
title: "Windows Default Domain GPO Modification via GPME"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_mmc_default_domain_gpo_modification_via_gpme.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_mmc_default_domain_gpo_modification_via_gpme.yml"
build_date: "2026-04-26 14:14:40"
status: "experimental"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "dcff7e85-d01f-4eb5-badd-84e2e6be8294"
  - "Windows Default Domain GPO Modification via GPME"
attack_technique_ids:
  - "T1484.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Windows Default Domain GPO Modification via GPME

Detects the use of the Group Policy Management Editor (GPME) to modify Default Domain or Default Domain Controllers Group Policy Objects (GPOs).
Adversaries may leverage GPME to make stealthy changes in these default GPOs to deploy malicious GPOs configurations across the domain without raising suspicion.

## Metadata

- Rule ID: dcff7e85-d01f-4eb5-badd-84e2e6be8294
- Status: experimental
- Level: medium
- Author: TropChaud
- Date: 2025-11-22
- Source Path: rules/windows/process_creation/proc_creation_win_mmc_default_domain_gpo_modification_via_gpme.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1484-domain_or_tenant_policy_modification|T1484.001]]

## Detection

```yaml
selection_mmc:
- Image|endswith: \mmc.exe
- OriginalFileName: MMC.exe
selection_gpme:
  CommandLine|contains|all:
  - gpme.msc
  - 'gpobject:'
selection_default_gpos:
  CommandLine|contains:
  - 31B2F340-016D-11D2-945F-00C04FB984F9
  - 6AC1786C-016F-11D2-945F-00C04FB984F9
condition: all of selection_*
```

## False Positives

- Legitimate use of GPME to modify GPOs

## References

- https://www.trendmicro.com/en_us/research/25/i/unmasking-the-gentlemen-ransomware.html
- https://adsecurity.org/?p=3377
- https://sdmsoftware.com/general-stuff/launching-the-new-gp-management-editor-from-the-command-line/
- https://www.pentestpartners.com/security-blog/living-off-the-land-gpo-style/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_mmc_default_domain_gpo_modification_via_gpme.yml)
