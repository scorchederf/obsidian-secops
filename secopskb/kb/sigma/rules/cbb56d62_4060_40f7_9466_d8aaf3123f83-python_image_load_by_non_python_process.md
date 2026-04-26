---
sigma_id: "cbb56d62-4060-40f7-9466-d8aaf3123f83"
title: "Python Image Load By Non-Python Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_susp_python_image_load.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_susp_python_image_load.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "low"
logsource: "windows / image_load"
aliases:
  - "cbb56d62-4060-40f7-9466-d8aaf3123f83"
  - "Python Image Load By Non-Python Process"
attack_technique_ids:
  - "T1027.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Python Image Load By Non-Python Process

Detects the image load of "Python Core" by a non-Python process. This might be indicative of a execution of executable that has been bundled from Python code.
Various tools like Py2Exe, PyInstaller, and cx_Freeze are used to bundle Python code into standalone executables.
Threat actors often use these tools to bundle malicious Python scripts into executables, sometimes to obfuscate the code or to bypass security measures.

## Metadata

- Rule ID: cbb56d62-4060-40f7-9466-d8aaf3123f83
- Status: test
- Level: low
- Author: Patrick St. John, OTR (Open Threat Research)
- Date: 2020-05-03
- Modified: 2025-08-18
- Source Path: rules/windows/image_load/image_load_susp_python_image_load.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027.002]]

## Detection

```yaml
selection:
  Description: Python Core
filter_main_generic:
- Image|contains: Python
- Image|startswith:
  - C:\Program Files\
  - C:\Program Files (x86)\
  - C:\ProgramData\Anaconda3\
filter_optional_null_image:
  Image: null
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Legitimate Py2Exe Binaries
- Known false positive caused with Python Anaconda
- Various legitimate software is bundled from Python code into executables

## References

- https://www.py2exe.org/
- https://unit42.paloaltonetworks.com/unit-42-technical-analysis-seaduke/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_susp_python_image_load.yml)
