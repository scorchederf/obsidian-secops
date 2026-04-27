---
sigma_id: "a2d9e2f3-0f43-4c7a-bcd9-9acfc0d723aa"
title: "Suspicious Download and Execute Pattern via Curl/Wget"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_curl_wget_exec_tmp.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_curl_wget_exec_tmp.yml"
build_date: "2026-04-27 19:13:56"
status: "experimental"
level: "high"
logsource: "linux / process_creation"
aliases:
  - "a2d9e2f3-0f43-4c7a-bcd9-9acfc0d723aa"
  - "Suspicious Download and Execute Pattern via Curl/Wget"
attack_technique_ids:
  - "T1059.004"
  - "T1203"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects suspicious use of command-line tools such as curl or wget to download remote
content - particularly scripts - into temporary directories (e.g., /dev/shm, /tmp), followed by
immediate execution, indicating potential malicious activity. This pattern is commonly used
by malicious scripts, stagers, or downloaders in fileless or multi-stage Linux attacks.

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059004-unix-shell|T1059.004: Unix Shell]]
- [[kb/attack/techniques/T1203-exploitation_for_client_execution|T1203: Exploitation for Client Execution]]

## Detection

```yaml
selection_downloader:
  CommandLine|contains:
  - /curl
  - /wget
selection_tmp:
  CommandLine|contains:
  - /tmp/
  - /dev/shm/
selection_executor:
  CommandLine|contains: sh -c
condition: all of selection_*
```

## False Positives

- System update scripts using temporary files
- Installer scripts or automated provisioning tools

## References

- https://gtfobins.github.io/gtfobins/wget/
- https://gtfobins.github.io/gtfobins/curl/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_curl_wget_exec_tmp.yml)
