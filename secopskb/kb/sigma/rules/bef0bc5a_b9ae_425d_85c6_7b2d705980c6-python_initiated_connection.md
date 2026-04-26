---
sigma_id: "bef0bc5a-b9ae-425d-85c6-7b2d705980c6"
title: "Python Initiated Connection"
framework: "sigma"
generated: "true"
source_path: "rules/windows/network_connection/net_connection_win_python.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_python.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / network_connection"
aliases:
  - "bef0bc5a-b9ae-425d-85c6-7b2d705980c6"
  - "Python Initiated Connection"
attack_technique_ids:
  - "T1046"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Python Initiated Connection

Detects a Python process initiating a network connection. While this often relates to package installation, it can also indicate a potential malicious script communicating with a C&C server.

## Metadata

- Rule ID: bef0bc5a-b9ae-425d-85c6-7b2d705980c6
- Status: test
- Level: medium
- Author: frack113
- Date: 2021-12-10
- Modified: 2025-03-05
- Source Path: rules/windows/network_connection/net_connection_win_python.yml

## Logsource

- category: network_connection
- definition: Requirements: Field enrichment is required for the filters to work. As field such as CommandLine and ParentImage are not available by default on this event type
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1046-network_service_discovery|T1046]]

## Detection

```yaml
selection:
  Initiated: 'true'
  Image|contains|all:
  - \python
  - .exe
filter_optional_conda:
  ParentImage: C:\ProgramData\Anaconda3\Scripts\conda.exe
  CommandLine|contains|all:
  - :\ProgramData\Anaconda3\Scripts\conda-script.py
  - update
filter_optional_conda_jupyter_notebook:
  ParentImage: C:\ProgramData\Anaconda3\python.exe
  CommandLine|contains: C:\ProgramData\Anaconda3\Scripts\jupyter-notebook-script.py
filter_main_local_communication:
  DestinationIp: 127.0.0.1
  SourceIp: 127.0.0.1
filter_main_pip:
  CommandLine|contains|all:
  - pip.exe
  - install
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Legitimate python scripts using the socket library or similar will trigger this. Apply additional filters and perform an initial baseline before deploying.

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1046/T1046.md#atomic-test-4---port-scan-using-python
- https://pypi.org/project/scapy/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_python.yml)
