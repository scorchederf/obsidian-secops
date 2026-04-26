---
sigma_id: "b439f47d-ef52-4b29-9a2f-57d8a96cb6b8"
title: "WMI ActiveScriptEventConsumers Activity Via Scrcons.EXE DLL Load"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_scrcons_wmi_scripteventconsumer.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_scrcons_wmi_scripteventconsumer.yml"
build_date: "2026-04-26 14:14:39"
status: "test"
level: "medium"
logsource: "windows / image_load"
aliases:
  - "b439f47d-ef52-4b29-9a2f-57d8a96cb6b8"
  - "WMI ActiveScriptEventConsumers Activity Via Scrcons.EXE DLL Load"
attack_technique_ids:
  - "T1546.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# WMI ActiveScriptEventConsumers Activity Via Scrcons.EXE DLL Load

Detects signs of the WMI script host process "scrcons.exe" loading scripting DLLs which could indicates WMI ActiveScriptEventConsumers EventConsumers activity.

## Metadata

- Rule ID: b439f47d-ef52-4b29-9a2f-57d8a96cb6b8
- Status: test
- Level: medium
- Author: Roberto Rodriguez (Cyb3rWard0g), OTR (Open Threat Research)
- Date: 2020-09-02
- Modified: 2023-02-22
- Source Path: rules/windows/image_load/image_load_scrcons_wmi_scripteventconsumer.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.003]]

## Detection

```yaml
selection:
  Image|endswith: \scrcons.exe
  ImageLoaded|endswith:
  - \vbscript.dll
  - \wbemdisp.dll
  - \wshom.ocx
  - \scrrun.dll
condition: selection
```

## False Positives

- Legitimate event consumers
- Dell computers on some versions register an event consumer that is known to cause false positives when brightness is changed by the corresponding keyboard button

## References

- https://twitter.com/HunterPlaybook/status/1301207718355759107
- https://www.mdsec.co.uk/2020/09/i-like-to-move-it-windows-lateral-movement-part-1-wmi-event-subscription/
- https://threathunterplaybook.com/hunts/windows/200902-RemoteWMIActiveScriptEventConsumers/notebook.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_scrcons_wmi_scripteventconsumer.yml)
