---
sigma_id: "3f0f5957-04f8-4792-ad89-192b0303bde6"
title: "Python WebServer Execution - Linux"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_python_http_server_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_python_http_server_execution.yml"
build_date: "2026-04-26 14:14:34"
status: "experimental"
level: "medium"
logsource: "linux / process_creation"
aliases:
  - "3f0f5957-04f8-4792-ad89-192b0303bde6"
  - "Python WebServer Execution - Linux"
attack_technique_ids:
  - "T1048.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Python WebServer Execution - Linux

Detects the execution of Python web servers via command line interface (CLI).
After gaining access to target systems, adversaries may use Python's built-in HTTP server modules to quickly establish a web server without requiring additional software.
This technique is commonly used in post-exploitation scenarios as it provides a simple method for transferring files between the compromised host and attacker-controlled systems.

## Metadata

- Rule ID: 3f0f5957-04f8-4792-ad89-192b0303bde6
- Status: experimental
- Level: medium
- Author: Mohamed LAKRI
- Date: 2025-10-17
- Source Path: rules/linux/process_creation/proc_creation_lnx_python_http_server_execution.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1048-exfiltration_over_alternative_protocol|T1048.003]]

## Detection

```yaml
selection_img:
- Image|endswith:
  - /python
  - /python2
  - /python3
- Image|contains:
  - /python2.
  - /python3.
selection_module:
  CommandLine|contains:
  - http.server
  - SimpleHTTPServer
condition: all of selection_*
```

## False Positives

- Testing or development activity

## References

- https://www.atomicredteam.io/atomic-red-team/atomics/T1048.003#atomic-test-8---python3-httpserver
- https://docs.python.org/3/library/http.server.html
- https://docs.python.org/2/library/simplehttpserver.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_python_http_server_execution.yml)
