---
sigma_id: "ddd171b5-2cc6-4975-9e78-f0eccd08cc76"
title: "Potential Persistence Via Outlook Home Page"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_persistence_outlook_homepage.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_outlook_homepage.yml"
build_date: "2026-04-26 15:01:49"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "ddd171b5-2cc6-4975-9e78-f0eccd08cc76"
  - "Potential Persistence Via Outlook Home Page"
attack_technique_ids:
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potential Persistence Via Outlook Home Page

Detects potential persistence activity via outlook home page.
An attacker can set a home page to achieve code execution and persistence by editing the WebView registry keys.

## Metadata

- Rule ID: ddd171b5-2cc6-4975-9e78-f0eccd08cc76
- Status: test
- Level: high
- Author: Tobias Michalski (Nextron Systems), David Bertho (@dbertho) & Eirik Sveen (@0xSV1), Storebrand
- Date: 2021-06-09
- Modified: 2024-08-07
- Source Path: rules/windows/registry/registry_set/registry_set_persistence_outlook_homepage.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Detection

```yaml
selection:
  TargetObject|contains|all:
  - \Software\Microsoft\Office\
  - \Outlook\WebView\
  TargetObject|endswith: \URL
condition: selection
```

## False Positives

- Unknown

## References

- https://speakerdeck.com/heirhabarov/hunting-for-persistence-via-microsoft-exchange-server-or-outlook?slide=70
- https://support.microsoft.com/en-us/topic/outlook-home-page-feature-is-missing-in-folder-properties-d207edb7-aa02-46c5-b608-5d9dbed9bd04?ui=en-us&rs=en-us&ad=us
- https://trustedsec.com/blog/specula-turning-outlook-into-a-c2-with-one-registry-change

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_persistence_outlook_homepage.yml)
