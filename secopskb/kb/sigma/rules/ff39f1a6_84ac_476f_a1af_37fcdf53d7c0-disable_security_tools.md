---
sigma_id: "ff39f1a6-84ac-476f-a1af-37fcdf53d7c0"
title: "Disable Security Tools"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_disable_security_tools.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_disable_security_tools.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "macos / process_creation"
aliases:
  - "ff39f1a6-84ac-476f-a1af-37fcdf53d7c0"
  - "Disable Security Tools"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Disable Security Tools

Detects disabling security tools

## Metadata

- Rule ID: ff39f1a6-84ac-476f-a1af-37fcdf53d7c0
- Status: test
- Level: medium
- Author: Daniil Yugoslavskiy, oscd.community
- Date: 2020-10-19
- Modified: 2021-11-27
- Source Path: rules/macos/process_creation/proc_creation_macos_disable_security_tools.yml

## Logsource

- category: process_creation
- product: macos

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
launchctl_unload:
  Image: /bin/launchctl
  CommandLine|contains: unload
security_plists:
  CommandLine|contains:
  - com.objective-see.lulu.plist
  - com.objective-see.blockblock.plist
  - com.google.santad.plist
  - com.carbonblack.defense.daemon.plist
  - com.carbonblack.daemon.plist
  - at.obdev.littlesnitchd.plist
  - com.tenablesecurity.nessusagent.plist
  - com.opendns.osx.RoamingClientConfigUpdater.plist
  - com.crowdstrike.falcond.plist
  - com.crowdstrike.userdaemon.plist
  - osquery
  - filebeat
  - auditbeat
  - packetbeat
  - td-agent
disable_gatekeeper:
  Image: /usr/sbin/spctl
  CommandLine|contains: disable
condition: (launchctl_unload and security_plists) or disable_gatekeeper
```

## False Positives

- Legitimate activities

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1562.001/T1562.001.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_disable_security_tools.yml)
