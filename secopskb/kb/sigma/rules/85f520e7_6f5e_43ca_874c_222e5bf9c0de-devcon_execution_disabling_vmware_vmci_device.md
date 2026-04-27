---
sigma_id: "85f520e7-6f5e-43ca-874c-222e5bf9c0de"
title: "Devcon Execution Disabling VMware VMCI Device"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_devcon_disable_vmci_driver.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_devcon_disable_vmci_driver.yml"
build_date: "2026-04-26 17:03:18"
status: "experimental"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "85f520e7-6f5e-43ca-874c-222e5bf9c0de"
  - "Devcon Execution Disabling VMware VMCI Device"
attack_technique_ids:
  - "T1543.003"
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Devcon Execution Disabling VMware VMCI Device

Detects execution of devcon.exe with commands that disable the VMware Virtual Machine Communication Interface (VMCI) device.
This can be legitimate during VMware Tools troubleshooting or driver conflicts, but may also indicate malware attempting to hijack communication with the hardware via the VMCI device.
This has been used to facilitate VMware ESXi vulnerability exploits to escape VMs and execute code on the ESXi host.

## Metadata

- Rule ID: 85f520e7-6f5e-43ca-874c-222e5bf9c0de
- Status: experimental
- Level: high
- Author: Matt Anderson, Dray Agha, Anna Pham (Huntress)
- Date: 2026-01-02
- Source Path: rules/windows/process_creation/proc_creation_win_devcon_disable_vmci_driver.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543.003]]
- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection_img:
- Image|endswith: \devcon.exe
- OriginalFileName: DevCon.exe
selection_action:
  CommandLine|contains: ' disable '
selection_vmci_pci:
  CommandLine|contains:
  - 15AD&DEV_0740
  - VMWVMCIHOSTDEV
condition: all of selection_*
```

## False Positives

- Legitimate VMware administration, Tools installation/uninstallation, or troubleshooting driver conflicts.
- Automated scripts in virtualized environments for device cleanup.

## References

- https://learn.microsoft.com/en-us/windows-hardware/drivers/devtest/devcon
- https://communities.vmware.com/t5/VMware-Workstation-Pro/VMCI-driver-issues/td-p/2866060
- https://github.com/search?q=devcon+disable+VMWVMCIHOSTDEV
- https://huntress.com/blog/esxi-vm-escape-exploit

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_devcon_disable_vmci_driver.yml)
