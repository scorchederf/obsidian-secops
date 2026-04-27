---
atomic_guid: "33a29ab1-cabb-407f-9448-269041bf2856"
title: "Delete all auditd rules using auditctl"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.012"
attack_technique_name: "Impair Defenses: Disable or Modify Linux Audit System"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.012/T1562.012.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "33a29ab1-cabb-407f-9448-269041bf2856"
  - "Delete all auditd rules using auditctl"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Delete all auditd rules using auditctl

Using 'auditctl -D' deletes all existing audit rules, resulting in the loss of previously configured monitoring settings and the audit trail. This action reduces visibility into system activities, potentially leading to compliance concerns and hampering security monitoring efforts. Additionally, it poses a risk of covering unauthorized activities by erasing evidence from audit logs.

## Metadata

- Atomic GUID: 33a29ab1-cabb-407f-9448-269041bf2856
- Technique: T1562.012: Impair Defenses: Disable or Modify Linux Audit System
- Platforms: linux
- Executor: sh
- Elevation Required: True
- Dependency Executor: sh
- Source Path: atomics/T1562.012/T1562.012.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.012]]

## Dependencies

Check if auditd is installed.

### Prerequisite Check

```bash
if [ $(command -v auditctl) ]; then exit 0; else exit 1; fi
```

### Get Prerequisite

```bash
(yum install auditd -y) || (apt-get install auditd -y) || (dnf install auditd -y)
```

## Executor

- elevation_required: True
- name: sh

### Command

```bash
auditctl -D
```

### Cleanup

```bash
service auditd restart
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.012/T1562.012.yaml)
