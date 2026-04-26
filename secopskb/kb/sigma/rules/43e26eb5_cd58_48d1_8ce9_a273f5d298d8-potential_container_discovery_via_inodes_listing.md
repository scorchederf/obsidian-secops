---
sigma_id: "43e26eb5-cd58-48d1-8ce9-a273f5d298d8"
title: "Potential Container Discovery Via Inodes Listing"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_susp_inod_listing.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_susp_inod_listing.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "low"
logsource: "linux / process_creation"
aliases:
  - "43e26eb5-cd58-48d1-8ce9-a273f5d298d8"
  - "Potential Container Discovery Via Inodes Listing"
attack_technique_ids:
  - "T1082"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Container Discovery Via Inodes Listing

Detects listing of the inodes of the "/" directory to determine if the we are running inside of a container.

## Metadata

- Rule ID: 43e26eb5-cd58-48d1-8ce9-a273f5d298d8
- Status: test
- Level: low
- Author: Seth Hanford
- Date: 2023-08-23
- Modified: 2025-11-24
- Source Path: rules/linux/process_creation/proc_creation_lnx_susp_inod_listing.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1082-system_information_discovery|T1082]]

## Detection

```yaml
selection_ls_img:
  Image|endswith: /ls
selection_ls_cli:
- CommandLine|endswith: ' /'
- CommandLine|contains: ' / '
selection_regex_inode:
  CommandLine|re: (?:\s-[^-\s]{0,20}i|\s--inode\s)
selection_regex_dir:
  CommandLine|re: (?:\s-[^-\s]{0,20}d|\s--directory\s)
condition: all of selection_*
```

## False Positives

- Legitimate system administrator usage of these commands
- Some container tools or deployments may use these techniques natively to determine how they proceed with execution, and will need to be filtered

## References

- https://blog.skyplabs.net/posts/container-detection/
- https://stackoverflow.com/questions/20010199/how-to-determine-if-a-process-runs-inside-lxc-docker

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_susp_inod_listing.yml)
