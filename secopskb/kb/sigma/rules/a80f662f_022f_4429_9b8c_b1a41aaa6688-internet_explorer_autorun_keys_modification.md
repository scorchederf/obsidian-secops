---
sigma_id: "a80f662f-022f-4429-9b8c-b1a41aaa6688"
title: "Internet Explorer Autorun Keys Modification"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_asep_reg_keys_modification_internet_explorer.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_asep_reg_keys_modification_internet_explorer.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "a80f662f-022f-4429-9b8c-b1a41aaa6688"
  - "Internet Explorer Autorun Keys Modification"
attack_technique_ids:
  - "T1547.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Internet Explorer Autorun Keys Modification

Detects modification of autostart extensibility point (ASEP) in registry.

## Metadata

- Rule ID: a80f662f-022f-4429-9b8c-b1a41aaa6688
- Status: test
- Level: medium
- Author: Victor Sergeev, Daniil Yugoslavskiy, Gleb Sukhodolskiy, Timur Zinniatullin, oscd.community, Tim Shelton, frack113 (split)
- Date: 2019-10-25
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_asep_reg_keys_modification_internet_explorer.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.001]]

## Detection

```yaml
ie:
  TargetObject|contains:
  - \Software\Wow6432Node\Microsoft\Internet Explorer
  - \Software\Microsoft\Internet Explorer
ie_details:
  TargetObject|contains:
  - \Toolbar
  - \Extensions
  - \Explorer Bars
filter_empty:
  Details: (Empty)
filter_extensions:
  TargetObject|contains:
  - \Extensions\{2670000A-7350-4f3c-8081-5663EE0C6C49}
  - \Extensions\{31D09BA0-12F5-4CCE-BE8A-2923E76605DA}
  - \Extensions\{789FE86F-6FC4-46A1-9849-EDE0DB0C95CA}
  - \Extensions\{A95fe080-8f5d-11d2-a20b-00aa003c157a}
filter_toolbar:
  TargetObject|endswith:
  - \Toolbar\ShellBrowser\ITBar7Layout
  - \Toolbar\ShowDiscussionButton
  - \Toolbar\Locked
condition: ie and ie_details and not 1 of filter_*
```

## False Positives

- Legitimate software automatically (mostly, during installation) sets up autorun keys for legitimate reason
- Legitimate administrator sets up autorun keys for legitimate reason

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1547.001/T1547.001.md
- https://learn.microsoft.com/en-us/sysinternals/downloads/autoruns
- https://gist.github.com/GlebSukhodolskiy/0fc5fa5f482903064b448890db1eaf9d

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_asep_reg_keys_modification_internet_explorer.yml)
