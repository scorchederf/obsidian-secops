---
atomic_guid: "cedaf7e7-28ee-42ab-ba13-456abd35d1bd"
title: "Auditing Configuration Changes on FreeBSD Host"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.006"
attack_technique_name: "Impair Defenses: Indicator Blocking"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.006/T1562.006.yaml"
build_date: "2026-04-27 19:12:28"
executor: "sh"
aliases:
  - "cedaf7e7-28ee-42ab-ba13-456abd35d1bd"
  - "Auditing Configuration Changes on FreeBSD Host"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Emulates modification of auditd configuration files

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses#^t1562006-indicator-blocking|T1562.006: Indicator Blocking]]

## Input Arguments

### auditd_config_file_name

- description: The name of the auditd configuration file to be changed
- type: string
- default: audit_event

## Executor

- elevation_required: True
- name: sh

### Command

```bash
echo '#art_test_1562_006_1' >> /etc/security/#{auditd_config_file_name}
```

### Cleanup

```bash
sed -i "" '/#art_test_1562_006_1/d' /etc/security/#{auditd_config_file_name}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.006/T1562.006.yaml)
