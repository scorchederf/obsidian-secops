---
sigma_id: "96f697b0-b499-4e5d-9908-a67bec11cdb6"
title: "Removal of Potential COM Hijacking Registry Keys"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_delete/registry_delete_removal_com_hijacking_registry_key.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_delete/registry_delete_removal_com_hijacking_registry_key.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / registry_delete"
aliases:
  - "96f697b0-b499-4e5d-9908-a67bec11cdb6"
  - "Removal of Potential COM Hijacking Registry Keys"
attack_technique_ids:
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Removal of Potential COM Hijacking Registry Keys

Detects any deletion of entries in ".*\shell\open\command" registry keys.
These registry keys might have been used for COM hijacking activities by a threat actor or an attacker and the deletion could indicate steps to remove its tracks.

## Metadata

- Rule ID: 96f697b0-b499-4e5d-9908-a67bec11cdb6
- Status: test
- Level: medium
- Author: Roberto Rodriguez (Cyb3rWard0g), OTR (Open Threat Research)
- Date: 2020-05-02
- Modified: 2025-10-07
- Source Path: rules/windows/registry/registry_delete/registry_delete_removal_com_hijacking_registry_key.yml

## Logsource

- category: registry_delete
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Detection

```yaml
selection:
  TargetObject|endswith: \shell\open\command
filter_main_explorer:
  Image|endswith: C:\Windows\explorer.exe
filter_main_svchost:
  Image: C:\Windows\system32\svchost.exe
filter_main_msiexec:
  Image:
  - C:\Windows\System32\msiexec.exe
  - C:\Windows\SysWOW64\msiexec.exe
filter_main_generic_prorams:
  Image|startswith:
  - C:\Program Files\
  - C:\Program Files (x86)\
filter_main_openwith:
  Image: C:\Windows\System32\OpenWith.exe
filter_optional_dropbox:
  Image|endswith: \Dropbox.exe
  TargetObject|contains: \Dropbox.
filter_optional_wireshark:
  Image|endswith: \AppData\Local\Temp\Wireshark_uninstaller.exe
  TargetObject|contains: \wireshark-capture-file\
filter_optional_peazip:
  Image|contains: peazip
  TargetObject|contains: \PeaZip.
filter_optional_everything:
  Image|endswith: \Everything.exe
  TargetObject|contains: \Everything.
filter_optional_uninstallers:
  Image|startswith: C:\Windows\Installer\MSI
filter_optional_java:
  Image|startswith: C:\Program Files (x86)\Java\
  Image|endswith: \installer.exe
  TargetObject|contains: \Classes\WOW6432Node\CLSID\{4299124F-F2C3-41b4-9C73-9236B2AD0E8F}
filter_optional_edgeupdate:
  Image|contains: \Microsoft\EdgeUpdate\Install
filter_optional_avira:
  Image:
  - C:\Program Files (x86)\Avira\Antivirus\
  - C:\Program Files\Avira\Antivirus\
  TargetObject|endswith:
  - \CLSID\{305CA226-D286-468e-B848-2B2E8E697B74}\Shell\Open\Command
  - \AntiVir.Keyfile\shell\open\command
filter_optional_installer_temp:
- Image|contains|all:
  - AppData\Local\Temp
  - \setup.exe
- Image|contains|all:
  - \Temp\is-
  - \target.tmp
filter_optional_ninite:
  Image|endswith: \ninite.exe
filter_optional_discord:
  Image|endswith: \reg.exe
  TargetObject|endswith: \Discord\shell\open\command
filter_optional_spotify:
  Image|endswith: \Spotify.exe
  TargetObject|endswith: \Spotify\shell\open\command
filter_optional_eclipse:
  Image|endswith: C:\eclipse\eclipse.exe
  TargetObject|contains: _Classes\eclipse+
filter_optional_teamviewer:
  Image|contains|all:
  - \Temp
  - \TeamViewer
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Legitimate software (un)installations are known to cause false positives. Please add them as a filter when encountered

## References

- https://github.com/OTRF/detection-hackathon-apt29/issues/7
- https://github.com/OTRF/ThreatHunter-Playbook/blob/2d4257f630f4c9770f78d0c1df059f891ffc3fec/docs/evals/apt29/detections/3.C.1_22A46621-7A92-48C1-81BF-B3937EB4FDC3.md
- https://learn.microsoft.com/en-us/windows/win32/shell/launch
- https://learn.microsoft.com/en-us/windows/win32/api/shobjidl_core/nn-shobjidl_core-iexecutecommand
- https://learn.microsoft.com/en-us/windows/win32/shell/shell-and-managed-code

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_delete/registry_delete_removal_com_hijacking_registry_key.yml)
