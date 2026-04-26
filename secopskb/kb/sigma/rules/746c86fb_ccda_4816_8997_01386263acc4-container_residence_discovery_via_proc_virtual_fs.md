---
sigma_id: "746c86fb-ccda-4816-8997-01386263acc4"
title: "Container Residence Discovery Via Proc Virtual FS"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_susp_container_residence_discovery.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_susp_container_residence_discovery.yml"
build_date: "2026-04-26 14:14:22"
status: "test"
level: "low"
logsource: "linux / process_creation"
aliases:
  - "746c86fb-ccda-4816-8997-01386263acc4"
  - "Container Residence Discovery Via Proc Virtual FS"
attack_technique_ids:
  - "T1082"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Container Residence Discovery Via Proc Virtual FS

Detects potential container discovery via listing of certain kernel features in the "/proc" virtual filesystem

## Metadata

- Rule ID: 746c86fb-ccda-4816-8997-01386263acc4
- Status: test
- Level: low
- Author: Seth Hanford
- Date: 2023-08-23
- Source Path: rules/linux/process_creation/proc_creation_lnx_susp_container_residence_discovery.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1082-system_information_discovery|T1082]]

## Detection

```yaml
selection_tools:
  Image|endswith:
  - awk
  - /cat
  - grep
  - /head
  - /less
  - /more
  - /nl
  - /tail
selection_procfs_kthreadd:
  CommandLine|contains: /proc/2/
selection_procfs_target:
  CommandLine|contains: /proc/
  CommandLine|endswith:
  - /cgroup
  - /sched
condition: selection_tools and 1 of selection_procfs_*
```

## False Positives

- Legitimate system administrator usage of these commands
- Some container tools or deployments may use these techniques natively to determine how they proceed with execution, and will need to be filtered

## References

- https://blog.skyplabs.net/posts/container-detection/
- https://stackoverflow.com/questions/20010199/how-to-determine-if-a-process-runs-inside-lxc-docker

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_susp_container_residence_discovery.yml)
