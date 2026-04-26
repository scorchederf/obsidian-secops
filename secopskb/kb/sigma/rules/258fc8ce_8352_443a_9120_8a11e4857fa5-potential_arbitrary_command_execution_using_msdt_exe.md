---
sigma_id: "258fc8ce-8352-443a-9120-8a11e4857fa5"
title: "Potential Arbitrary Command Execution Using Msdt.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_msdt_arbitrary_command_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_msdt_arbitrary_command_execution.yml"
build_date: "2026-04-26 15:01:48"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "258fc8ce-8352-443a-9120-8a11e4857fa5"
  - "Potential Arbitrary Command Execution Using Msdt.EXE"
attack_technique_ids:
  - "T1202"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potential Arbitrary Command Execution Using Msdt.EXE

Detects processes leveraging the "ms-msdt" handler or the "msdt.exe" binary to execute arbitrary commands as seen in the follina (CVE-2022-30190) vulnerability

## Metadata

- Rule ID: 258fc8ce-8352-443a-9120-8a11e4857fa5
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-05-29
- Modified: 2024-03-13
- Source Path: rules/windows/process_creation/proc_creation_win_msdt_arbitrary_command_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1202-indirect_command_execution|T1202]]

## Detection

```yaml
selection_img:
- Image|endswith: \msdt.exe
- OriginalFileName: msdt.exe
selection_cmd_inline:
  CommandLine|contains: IT_BrowseForFile=
selection_cmd_answerfile_flag:
  CommandLine|contains: ' PCWDiagnostic'
selection_cmd_answerfile_param:
  CommandLine|contains|windash: ' -af '
condition: selection_img and (selection_cmd_inline or all of selection_cmd_answerfile_*)
```

## False Positives

- Unknown

## References

- https://twitter.com/nao_sec/status/1530196847679401984
- https://app.any.run/tasks/713f05d2-fe78-4b9d-a744-f7c133e3fafb/
- https://twitter.com/_JohnHammond/status/1531672601067675648

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_msdt_arbitrary_command_execution.yml)
