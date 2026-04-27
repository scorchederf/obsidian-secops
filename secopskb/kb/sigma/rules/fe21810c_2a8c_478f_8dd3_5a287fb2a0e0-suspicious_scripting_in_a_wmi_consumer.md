---
sigma_id: "fe21810c-2a8c-478f-8dd3-5a287fb2a0e0"
title: "Suspicious Scripting in a WMI Consumer"
framework: "sigma"
generated: "true"
source_path: "rules/windows/wmi_event/sysmon_wmi_susp_scripting.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/wmi_event/sysmon_wmi_susp_scripting.yml"
build_date: "2026-04-27 19:13:57"
status: "test"
level: "high"
logsource: "windows / wmi_event"
aliases:
  - "fe21810c-2a8c-478f-8dd3-5a287fb2a0e0"
  - "Suspicious Scripting in a WMI Consumer"
attack_technique_ids:
  - "T1059.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects suspicious commands that are related to scripting/powershell in WMI Event Consumers

## Logsource

- category: wmi_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059005-visual-basic|T1059.005: Visual Basic]]

## Detection

```yaml
selection_destination:
- Destination|contains|all:
  - new-object
  - net.webclient
  - .downloadstring
- Destination|contains|all:
  - new-object
  - net.webclient
  - .downloadfile
- Destination|contains:
  - ' iex('
  - ' -nop '
  - ' -noprofile '
  - ' -decode '
  - ' -enc '
  - WScript.Shell
  - System.Security.Cryptography.FromBase64Transform
condition: selection_destination
```

## False Positives

- Legitimate administrative scripts

## References

- https://in.security/an-intro-into-abusing-and-identifying-wmi-event-subscriptions-for-persistence/
- https://github.com/Neo23x0/signature-base/blob/615bf1f6bac3c1bdc417025c40c073e6c2771a76/yara/gen_susp_lnk_files.yar#L19
- https://github.com/RiccardoAncarani/LiquidSnake

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/wmi_event/sysmon_wmi_susp_scripting.yml)
