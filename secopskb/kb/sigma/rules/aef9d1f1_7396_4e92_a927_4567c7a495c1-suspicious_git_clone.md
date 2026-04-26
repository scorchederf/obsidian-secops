---
sigma_id: "aef9d1f1-7396-4e92-a927-4567c7a495c1"
title: "Suspicious Git Clone"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_git_susp_clone.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_git_susp_clone.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "aef9d1f1-7396-4e92-a927-4567c7a495c1"
  - "Suspicious Git Clone"
attack_technique_ids:
  - "T1593.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Git Clone

Detects execution of "git" in order to clone a remote repository that contain suspicious keywords which might be suspicious

## Metadata

- Rule ID: aef9d1f1-7396-4e92-a927-4567c7a495c1
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-01-03
- Modified: 2023-01-10
- Source Path: rules/windows/process_creation/proc_creation_win_git_susp_clone.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1593-search_open_websites_domains|T1593.003]]

## Detection

```yaml
selection_img:
- Image|endswith:
  - \git.exe
  - \git-remote-https.exe
- OriginalFileName: git.exe
selection_cli:
  CommandLine|contains:
  - ' clone '
  - 'git-remote-https '
selection_keyword:
  CommandLine|contains:
  - exploit
  - Vulns
  - vulnerability
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

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_git_susp_clone.yml)
