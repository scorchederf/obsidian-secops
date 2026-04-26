---
sigma_id: "a1e11042-a74a-46e6-b07c-c4ce8ecc239b"
title: "Potential Persistence Via Event Viewer Events.asp"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_persistence_event_viewer_events_asp.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_event_viewer_events_asp.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "a1e11042-a74a-46e6-b07c-c4ce8ecc239b"
  - "Potential Persistence Via Event Viewer Events.asp"
attack_technique_ids:
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Persistence Via Event Viewer Events.asp

Detects potential registry persistence technique using the Event Viewer "Events.asp" technique

## Metadata

- Rule ID: a1e11042-a74a-46e6-b07c-c4ce8ecc239b
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-02-17
- Modified: 2023-03-05
- Source Path: rules/windows/registry/registry_set/registry_set_persistence_event_viewer_events_asp.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Detection

```yaml
selection:
  TargetObject|contains:
  - \Microsoft\Windows NT\CurrentVersion\Event Viewer\MicrosoftRedirectionProgram
  - \Microsoft\Windows NT\CurrentVersion\Event Viewer\MicrosoftRedirectionURL
filter_default_redirect_program:
  Image|endswith: C:\WINDOWS\system32\svchost.exe
  TargetObject|endswith: \Microsoft\Windows NT\CurrentVersion\Event Viewer\MicrosoftRedirectionProgram
  Details: '%%SystemRoot%%\PCHealth\HelpCtr\Binaries\HelpCtr.exe'
filter_default_redirect_program_cli:
  Image|endswith: C:\WINDOWS\system32\svchost.exe
  TargetObject|endswith: \Microsoft\Windows NT\CurrentVersion\Event Viewer\MicrosoftRedirectionProgramCommandLineParameters
  Details: -url hcp://services/centers/support?topic=%%s
filter_url:
  Details: http://go.microsoft.com/fwlink/events.asp
filter_cleaner:
  Details: (Empty)
condition: selection and not 1 of filter_*
```

## False Positives

- Unknown

## References

- https://twitter.com/nas_bench/status/1626648985824788480
- https://admx.help/?Category=Windows_7_2008R2&Policy=Microsoft.Policies.InternetCommunicationManagement::EventViewer_DisableLinks
- https://www.hexacorn.com/blog/2019/02/15/beyond-good-ol-run-key-part-103/
- https://github.com/redcanaryco/atomic-red-team/blob/f296668303c29d3f4c07e42bdd2b28d8dd6625f9/atomics/T1112/T1112.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_event_viewer_events_asp.yml)
