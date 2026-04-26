---
sigma_id: "85de1f22-d189-44e4-8239-dc276b45379b"
title: "Curl Web Request With Potential Custom User-Agent"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_curl_custom_user_agent.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_curl_custom_user_agent.yml"
build_date: "2026-04-26 14:14:23"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "85de1f22-d189-44e4-8239-dc276b45379b"
  - "Curl Web Request With Potential Custom User-Agent"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Curl Web Request With Potential Custom User-Agent

Detects execution of "curl.exe" with a potential custom "User-Agent". Attackers can leverage this to download or exfiltrate data via "curl" to a domain that only accept specific "User-Agent" strings

## Metadata

- Rule ID: 85de1f22-d189-44e4-8239-dc276b45379b
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-07-27
- Modified: 2025-12-11
- Source Path: rules/windows/process_creation/proc_creation_win_curl_custom_user_agent.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_img:
- Image|endswith: \curl.exe
- OriginalFileName: curl.exe
selection_header_flag_1:
  CommandLine|re: \s-H\s
selection_header_flag_2:
  CommandLine|contains: --header
selection_user_agent:
  CommandLine|contains: 'User-Agent:'
condition: selection_img and 1 of selection_header_* and selection_user_agent
```

## False Positives

- Unknown

## References

- https://labs.withsecure.com/publications/fin7-target-veeam-servers
- https://github.com/WithSecureLabs/iocs/blob/344203de742bb7e68bd56618f66d34be95a9f9fc/FIN7VEEAM/iocs.csv

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_curl_custom_user_agent.yml)
