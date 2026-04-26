---
sigma_id: "7090adee-82e2-4269-bd59-80691e7c6338"
title: "Console CodePage Lookup Via CHCP"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_chcp_codepage_lookup.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_chcp_codepage_lookup.yml"
build_date: "2026-04-26 14:14:22"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "7090adee-82e2-4269-bd59-80691e7c6338"
  - "Console CodePage Lookup Via CHCP"
attack_technique_ids:
  - "T1614.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Console CodePage Lookup Via CHCP

Detects use of chcp to look up the system locale value as part of host discovery

## Metadata

- Rule ID: 7090adee-82e2-4269-bd59-80691e7c6338
- Status: test
- Level: medium
- Author: _pete_0, TheDFIRReport
- Date: 2022-02-21
- Modified: 2024-03-05
- Source Path: rules/windows/process_creation/proc_creation_win_chcp_codepage_lookup.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1614-system_location_discovery|T1614.001]]

## Detection

```yaml
selection:
  ParentImage|endswith: \cmd.exe
  ParentCommandLine|contains|windash:
  - ' -c '
  - ' -r '
  - ' -k '
  Image|endswith: \chcp.com
  CommandLine|endswith:
  - chcp
  - 'chcp '
  - 'chcp  '
condition: selection
```

## False Positives

- During Anaconda update the 'conda.exe' process will eventually execution the 'chcp' command.
- Discord was seen using chcp to look up code pages

## References

- https://thedfirreport.com/2022/04/04/stolen-images-campaign-ends-in-conti-ransomware/
- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/chcp

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_chcp_codepage_lookup.yml)
