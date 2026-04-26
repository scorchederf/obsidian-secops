---
sigma_id: "11701de9-d5a5-44aa-8238-84252f131895"
title: "Docker Container Discovery Via Dockerenv Listing"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_susp_dockerenv_recon.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_susp_dockerenv_recon.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "low"
logsource: "linux / process_creation"
aliases:
  - "11701de9-d5a5-44aa-8238-84252f131895"
  - "Docker Container Discovery Via Dockerenv Listing"
attack_technique_ids:
  - "T1082"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Docker Container Discovery Via Dockerenv Listing

Detects listing or file reading of ".dockerenv" which can be a sing of potential container discovery

## Metadata

- Rule ID: 11701de9-d5a5-44aa-8238-84252f131895
- Status: test
- Level: low
- Author: Seth Hanford
- Date: 2023-08-23
- Source Path: rules/linux/process_creation/proc_creation_lnx_susp_dockerenv_recon.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1082-system_information_discovery|T1082]]

## Detection

```yaml
selection:
  Image|endswith:
  - /cat
  - /dir
  - /find
  - /ls
  - /stat
  - /test
  - grep
  CommandLine|endswith: .dockerenv
condition: selection
```

## False Positives

- Legitimate system administrator usage of these commands
- Some container tools or deployments may use these techniques natively to determine how they proceed with execution, and will need to be filtered

## References

- https://blog.skyplabs.net/posts/container-detection/
- https://stackoverflow.com/questions/20010199/how-to-determine-if-a-process-runs-inside-lxc-docker

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_susp_dockerenv_recon.yml)
