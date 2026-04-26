---
sigma_id: "c74d7efc-8826-45d9-b8bb-f04fac9e4eff"
title: "Run Once Task Configuration in Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_event/registry_event_runonce_persistence.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_runonce_persistence.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "windows / registry_event"
aliases:
  - "c74d7efc-8826-45d9-b8bb-f04fac9e4eff"
  - "Run Once Task Configuration in Registry"
attack_technique_ids:
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Run Once Task Configuration in Registry

Rule to detect the configuration of Run Once registry key. Configured payload can be run by runonce.exe /AlternateShellStartup

## Metadata

- Rule ID: c74d7efc-8826-45d9-b8bb-f04fac9e4eff
- Status: test
- Level: medium
- Author: Avneet Singh @v3t0_, oscd.community
- Date: 2020-11-15
- Modified: 2024-03-25
- Source Path: rules/windows/registry/registry_event/registry_event_runonce_persistence.yml

## Logsource

- category: registry_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Detection

```yaml
selection:
  TargetObject|contains: \Microsoft\Active Setup\Installed Components
  TargetObject|endswith: \StubPath
filter_optional_chrome:
  Details|contains|all:
  - C:\Program Files\Google\Chrome\Application\
  - \Installer\chrmstp.exe" --configure-user-settings --verbose-logging --system-level
filter_optional_edge:
  Details|contains:
  - C:\Program Files (x86)\Microsoft\Edge\Application\
  - C:\Program Files\Microsoft\Edge\Application\
  Details|endswith: \Installer\setup.exe" --configure-user-settings --verbose-logging
    --system-level --msedge --channel=stable
condition: selection and not 1 of filter_optional_*
```

## False Positives

- Legitimate modification of the registry key by legitimate program

## References

- https://twitter.com/pabraeken/status/990717080805789697
- https://lolbas-project.github.io/lolbas/Binaries/Runonce/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_runonce_persistence.yml)
