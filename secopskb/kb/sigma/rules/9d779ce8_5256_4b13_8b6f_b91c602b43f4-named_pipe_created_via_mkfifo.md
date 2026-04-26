---
sigma_id: "9d779ce8-5256-4b13-8b6f-b91c602b43f4"
title: "Named Pipe Created Via Mkfifo"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_mkfifo_named_pipe_creation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_mkfifo_named_pipe_creation.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "low"
logsource: "linux / process_creation"
aliases:
  - "9d779ce8-5256-4b13-8b6f-b91c602b43f4"
  - "Named Pipe Created Via Mkfifo"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Named Pipe Created Via Mkfifo

Detects the creation of a new named pipe using the "mkfifo" utility

## Metadata

- Rule ID: 9d779ce8-5256-4b13-8b6f-b91c602b43f4
- Status: test
- Level: low
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-06-16
- Source Path: rules/linux/process_creation/proc_creation_lnx_mkfifo_named_pipe_creation.yml

## Logsource

- category: process_creation
- product: linux

## Detection

```yaml
selection:
  Image|endswith: /mkfifo
condition: selection
```

## False Positives

- Unknown

## References

- https://dev.to/0xbf/use-mkfifo-to-create-named-pipe-linux-tips-5bbk
- https://www.mandiant.com/resources/blog/barracuda-esg-exploited-globally

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_mkfifo_named_pipe_creation.yml)
