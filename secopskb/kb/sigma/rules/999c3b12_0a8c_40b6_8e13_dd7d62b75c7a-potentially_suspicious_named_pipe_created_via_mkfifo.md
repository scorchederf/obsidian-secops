---
sigma_id: "999c3b12-0a8c-40b6-8e13-dd7d62b75c7a"
title: "Potentially Suspicious Named Pipe Created Via Mkfifo"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_mkfifo_named_pipe_creation_susp_location.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_mkfifo_named_pipe_creation_susp_location.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "linux / process_creation"
aliases:
  - "999c3b12-0a8c-40b6-8e13-dd7d62b75c7a"
  - "Potentially Suspicious Named Pipe Created Via Mkfifo"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potentially Suspicious Named Pipe Created Via Mkfifo

Detects the creation of a new named pipe using the "mkfifo" utility in a potentially suspicious location

## Metadata

- Rule ID: 999c3b12-0a8c-40b6-8e13-dd7d62b75c7a
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-06-16
- Source Path: rules/linux/process_creation/proc_creation_lnx_mkfifo_named_pipe_creation_susp_location.yml

## Logsource

- category: process_creation
- product: linux

## Detection

```yaml
selection:
  Image|endswith: /mkfifo
  CommandLine|contains: ' /tmp/'
condition: selection
```

## False Positives

- Unknown

## References

- https://dev.to/0xbf/use-mkfifo-to-create-named-pipe-linux-tips-5bbk
- https://www.mandiant.com/resources/blog/barracuda-esg-exploited-globally

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_mkfifo_named_pipe_creation_susp_location.yml)
