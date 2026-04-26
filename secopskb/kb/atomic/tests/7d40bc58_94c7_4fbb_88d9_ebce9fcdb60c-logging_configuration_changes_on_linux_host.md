---
atomic_guid: "7d40bc58-94c7-4fbb-88d9-ebce9fcdb60c"
title: "Logging Configuration Changes on Linux Host"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.006"
attack_technique_name: "Impair Defenses: Indicator Blocking"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.006/T1562.006.yaml"
build_date: "2026-04-26 17:02:13"
executor: "bash"
aliases:
  - "7d40bc58-94c7-4fbb-88d9-ebce9fcdb60c"
  - "Logging Configuration Changes on Linux Host"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Logging Configuration Changes on Linux Host

Emulates modification of syslog configuration.

## Metadata

- Atomic GUID: 7d40bc58-94c7-4fbb-88d9-ebce9fcdb60c
- Technique: T1562.006: Impair Defenses: Indicator Blocking
- Platforms: linux
- Executor: bash
- Elevation Required: True
- Source Path: atomics/T1562.006/T1562.006.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.006]]

## Input Arguments

### rsyslog_config_file_name

- description: The name of the rsyslog configuration file to be changed
- type: string
- default: rsyslog.conf

### syslog_config_file_name

- description: The name of the syslog configuration file to be changed
- type: string
- default: syslog.conf

### syslog_ng_config_file_name

- description: The name of the syslog-ng configuration file to be changed
- type: string
- default: syslog-ng.conf

## Executor

- elevation_required: True
- name: bash

### Command

```bash
if [ -f "/etc/#{syslog_config_file_name}" ];
then sed -i '$ a #art_test_1562_006_2' /etc/#{syslog_config_file_name}
fi
if [ -f "/etc/#{rsyslog_config_file_name}" ];
then sed -i '$ a #art_test_1562_006_2' /etc/#{rsyslog_config_file_name}
fi
if [ -f "/etc/syslog-ng/#{syslog_ng_config_file_name}" ];
then sed -i '$ a #art_test_1562_006_2' /etc/syslog-ng/#{syslog_ng_config_file_name}
fi
```

### Cleanup

```bash
if [ -f "/etc/#{syslog_config_file_name}" ];
then sed -i '$ d' /etc/#{syslog_config_file_name}
fi
if [ -f "/etc/#{rsyslog_config_file_name}" ];
then sed -i '$ d' /etc/#{rsyslog_config_file_name}
fi
if [ -f "/etc/syslog-ng/#{syslog_ng_config_file_name}" ];
then sed -i '$ d' /etc/syslog-ng/#{syslog_ng_config_file_name}
fi
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.006/T1562.006.yaml)
