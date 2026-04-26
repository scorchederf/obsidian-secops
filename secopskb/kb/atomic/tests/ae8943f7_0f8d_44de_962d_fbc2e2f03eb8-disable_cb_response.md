---
atomic_guid: "ae8943f7-0f8d-44de-962d-fbc2e2f03eb8"
title: "Disable Cb Response"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.001"
attack_technique_name: "Impair Defenses: Disable or Modify Tools"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "ae8943f7-0f8d-44de-962d-fbc2e2f03eb8"
  - "Disable Cb Response"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Disable Cb Response

Disable the Cb Response service

## Metadata

- Atomic GUID: ae8943f7-0f8d-44de-962d-fbc2e2f03eb8
- Technique: T1562.001: Impair Defenses: Disable or Modify Tools
- Platforms: linux
- Executor: sh
- Source Path: atomics/T1562.001/T1562.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Executor

- name: sh

### Command

```bash
if [ $(rpm -q --queryformat '%{VERSION}' centos-release) -eq "6" ];
then
  service cbdaemon stop
  chkconfig off cbdaemon
else if [ $(rpm -q --queryformat '%{VERSION}' centos-release) -eq "7" ];
  systemctl stop cbdaemon
  systemctl disable cbdaemon
fi
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml)
