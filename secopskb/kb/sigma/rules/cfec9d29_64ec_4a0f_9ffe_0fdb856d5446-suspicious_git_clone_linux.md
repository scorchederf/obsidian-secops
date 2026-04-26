---
sigma_id: "cfec9d29-64ec-4a0f-9ffe-0fdb856d5446"
title: "Suspicious Git Clone - Linux"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_susp_git_clone.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_susp_git_clone.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "linux / process_creation"
aliases:
  - "cfec9d29-64ec-4a0f-9ffe-0fdb856d5446"
  - "Suspicious Git Clone - Linux"
attack_technique_ids:
  - "T1593.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Git Clone - Linux

Detects execution of "git" in order to clone a remote repository that contain suspicious keywords which might be suspicious

## Metadata

- Rule ID: cfec9d29-64ec-4a0f-9ffe-0fdb856d5446
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-01-03
- Modified: 2023-01-05
- Source Path: rules/linux/process_creation/proc_creation_lnx_susp_git_clone.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1593-search_open_websites_domains|T1593.003]]

## Detection

```yaml
selection_img:
  Image|endswith: /git
  CommandLine|contains: ' clone '
selection_keyword:
  CommandLine|contains:
  - exploit
  - Vulns
  - vulnerability
  - RCE
  - RemoteCodeExecution
  - Invoke-
  - CVE-
  - poc-
  - ProofOfConcept
  - proxyshell
  - log4shell
  - eternalblue
  - eternal-blue
  - MS17-
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://gist.githubusercontent.com/MichaelKoczwara/12faba9c061c12b5814b711166de8c2f/raw/e2068486692897b620c25fde1ea258c8218fe3d3/history.txt

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_susp_git_clone.yml)
