---
atomic_guid: "212cfbcf-4770-4980-bc21-303e37abd0e3"
title: "Auditing Configuration Changes on Linux Host"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.006"
attack_technique_name: "Impair Defenses: Indicator Blocking"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.006/T1562.006.yaml"
build_date: "2026-04-26 17:02:13"
executor: "bash"
aliases:
  - "212cfbcf-4770-4980-bc21-303e37abd0e3"
  - "Auditing Configuration Changes on Linux Host"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Auditing Configuration Changes on Linux Host

Emulates modification of auditd configuration files

## Metadata

- Atomic GUID: 212cfbcf-4770-4980-bc21-303e37abd0e3
- Technique: T1562.006: Impair Defenses: Indicator Blocking
- Platforms: linux
- Executor: bash
- Elevation Required: True
- Source Path: atomics/T1562.006/T1562.006.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.006]]

## Input Arguments

### audisp_config_file_name

- description: The name of the audispd configuration file to be changed
- type: string
- default: audispd.conf

### auditd_config_file_name

- description: The name of the auditd configuration file to be changed
- type: string
- default: auditd.conf

### libaudit_config_file_name

- description: The name of the libaudit configuration file to be changed
- type: string
- default: libaudit.conf

## Executor

- elevation_required: True
- name: bash

### Command

```bash
sed -i '$ a #art_test_1562_006_1' /etc/audisp/#{audisp_config_file_name}
if [ -f "/etc/#{auditd_config_file_name}" ];
then sed -i '$ a #art_test_1562_006_1' /etc/#{auditd_config_file_name}
else sed -i '$ a #art_test_1562_006_1' /etc/audit/#{auditd_config_file_name}
fi 
sed -i '$ a #art_test_1562_006_1' /etc/#{libaudit_config_file_name}
```

### Cleanup

```bash
sed -i '$ d' /etc/audisp/#{audisp_config_file_name}
if [ -f "/etc/#{auditd_config_file_name}" ];
then sed -i '$ d' /etc/#{auditd_config_file_name}
else sed -i '$ d' /etc/audit/#{auditd_config_file_name}
fi
sed -i '$ d' /etc/#{libaudit_config_file_name}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.006/T1562.006.yaml)
