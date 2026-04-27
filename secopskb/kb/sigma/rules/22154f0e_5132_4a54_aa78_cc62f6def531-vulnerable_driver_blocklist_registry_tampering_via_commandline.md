---
sigma_id: "22154f0e-5132-4a54-aa78-cc62f6def531"
title: "Vulnerable Driver Blocklist Registry Tampering Via CommandLine"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_vulnerable_driver_blocklist_registry_tampering.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_vulnerable_driver_blocklist_registry_tampering.yml"
build_date: "2026-04-27 19:13:58"
status: "experimental"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "22154f0e-5132-4a54-aa78-cc62f6def531"
  - "Vulnerable Driver Blocklist Registry Tampering Via CommandLine"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects tampering of the Vulnerable Driver Blocklist registry via command line tools such as PowerShell or REG.EXE.
The Vulnerable Driver Blocklist is a security feature that helps prevent the loading of known vulnerable drivers.
Disabling this feature may indicate an attempt to bypass security controls, often targeted by threat actors
to facilitate the installation of malicious or vulnerable drivers, particularly in scenarios involving Endpoint Detection and Response

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses#^t1562001-disable-or-modify-tools|T1562.001: Disable or Modify Tools]]

## Detection

```yaml
selection_img:
- Image|endswith:
  - \powershell.exe
  - \pwsh.exe
  - \reg.exe
- OriginalFileName:
  - PowerShell.EXE
  - pwsh.dll
  - reg.exe
selection_cli_1:
  CommandLine|contains:
  - 'add '
  - 'New-ItemProperty '
  - 'Set-ItemProperty '
  - 'si '
selection_cli_2:
  CommandLine|contains|all:
  - \Control\CI\Config
  - VulnerableDriverBlocklistEnable
condition: all of selection_*
```

## False Positives

- It is very unlikely for legitimate activities to disable the Vulnerable Driver Blocklist via command line tools; thus it is recommended to investigate promptly.

## References

- https://www.sophos.com/en-us/blog/sharpening-the-knife-gold-blades-strategic-evolution
- https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/design/microsoft-recommended-driver-block-rules

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_vulnerable_driver_blocklist_registry_tampering.yml)
