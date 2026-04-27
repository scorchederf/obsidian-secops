---
atomic_guid: "6b8ca3ab-5980-4321-80c3-bcd77c8daed8"
title: "Logging Configuration Changes on FreeBSD Host"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.006"
attack_technique_name: "Impair Defenses: Indicator Blocking"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.006/T1562.006.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "6b8ca3ab-5980-4321-80c3-bcd77c8daed8"
  - "Logging Configuration Changes on FreeBSD Host"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Logging Configuration Changes on FreeBSD Host

Emulates modification of syslog configuration.

## Metadata

- Atomic GUID: 6b8ca3ab-5980-4321-80c3-bcd77c8daed8
- Technique: T1562.006: Impair Defenses: Indicator Blocking
- Platforms: linux
- Executor: sh
- Elevation Required: True
- Source Path: atomics/T1562.006/T1562.006.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.006]]

## Input Arguments

### syslog_config_file_name

- description: The name of the syslog configuration file to be changed
- type: string
- default: syslog.conf

## Executor

- elevation_required: True
- name: sh

### Command

```bash
if [ -f "/etc/#{syslog_config_file_name}" ];
then echo '#art_test_1562_006_2' >> /etc/#{syslog_config_file_name}
fi
```

### Cleanup

```bash
if [ -f "/etc/#{syslog_config_file_name}" ];
then sed -i "" '/#art_test_1562_006_2/d' /etc/#{syslog_config_file_name}
fi
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.006/T1562.006.yaml)
