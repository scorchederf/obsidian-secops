---
atomic_guid: "7906f0a6-b527-46ee-9026-6e81a9184e08"
title: "Disable auditd using auditctl"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.012"
attack_technique_name: "Impair Defenses: Disable or Modify Linux Audit System"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.012/T1562.012.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "7906f0a6-b527-46ee-9026-6e81a9184e08"
  - "Disable auditd using auditctl"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Disable auditd using auditctl

The command `auditctl -e 0` disables the audit system. By setting the parameter to `0`, auditing is deactivated, halting the monitoring and recording of security-related events. This action stops the generation of audit logs, ceasing the collection of data regarding system activities. Disabling auditing may be done for various reasons, such as troubleshooting, performance optimization, or temporarily suspending auditing requirements, but it reduces visibility into system events and can impact security monitoring and compliance efforts.

## Metadata

- Atomic GUID: 7906f0a6-b527-46ee-9026-6e81a9184e08
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
auditctl -e 0
```

### Cleanup

```bash
auditctl -e 1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.012/T1562.012.yaml)
