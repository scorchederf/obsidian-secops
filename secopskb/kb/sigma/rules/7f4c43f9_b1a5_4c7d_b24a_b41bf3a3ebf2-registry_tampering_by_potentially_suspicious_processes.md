---
sigma_id: "7f4c43f9-b1a5-4c7d-b24a-b41bf3a3ebf2"
title: "Registry Tampering by Potentially Suspicious Processes"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_event/registry_event_susp_process_registry_modification.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_susp_process_registry_modification.yml"
build_date: "2026-04-26 14:14:34"
status: "experimental"
level: "medium"
logsource: "windows / registry_event"
aliases:
  - "7f4c43f9-b1a5-4c7d-b24a-b41bf3a3ebf2"
  - "Registry Tampering by Potentially Suspicious Processes"
attack_technique_ids:
  - "T1112"
  - "T1059.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Registry Tampering by Potentially Suspicious Processes

Detects suspicious registry modifications made by suspicious processes such as script engine processes such as WScript, or CScript etc.
These processes are rarely used for legitimate registry modifications, and their activity may indicate an attempt to modify the registry
without using standard tools like regedit.exe or reg.exe, potentially for evasion and persistence.

## Metadata

- Rule ID: 7f4c43f9-b1a5-4c7d-b24a-b41bf3a3ebf2
- Status: experimental
- Level: medium
- Author: Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2025-08-13
- Modified: 2026-04-14
- Source Path: rules/windows/registry/registry_event/registry_event_susp_process_registry_modification.yml

## Logsource

- category: registry_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1112-modify_registry|T1112]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.005]]

## Detection

```yaml
selection:
  Image|endswith:
  - \mshta.exe
  - \wscript.exe
  - \cscript.exe
filter_main_legit_wscript:
  Image|endswith: \wscript.exe
  TargetObject|contains:
  - SOFTWARE\Microsoft\Windows NT\CurrentVersion\Notifications\Data\
  - \Services\bam\State\UserSettings\S-1-
  - Software\Microsoft\Windows Script\Settings\Telemetry\wscript.exe\
  - Software\Microsoft\Windows\CurrentVersion\Internet Settings\
condition: selection and not 1 of filter_main_*
```

## False Positives

- Some legitimate admin or install scripts may use these processes for registry modifications.

## References

- https://www.nextron-systems.com/2025/07/29/detecting-the-most-popular-mitre-persistence-method-registry-run-keys-startup-folder/
- https://www.linkedin.com/posts/mauricefielenbach_livingofftheland-redteam-persistence-activity-7344801774182051843-TE00/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_susp_process_registry_modification.yml)
