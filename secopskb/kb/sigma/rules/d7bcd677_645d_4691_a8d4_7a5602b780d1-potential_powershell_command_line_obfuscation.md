---
sigma_id: "d7bcd677-645d-4691-a8d4-7a5602b780d1"
title: "Potential PowerShell Command Line Obfuscation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_cmdline_special_characters.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_cmdline_special_characters.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "d7bcd677-645d-4691-a8d4-7a5602b780d1"
  - "Potential PowerShell Command Line Obfuscation"
attack_technique_ids:
  - "T1027"
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Potential PowerShell Command Line Obfuscation

Detects the PowerShell command lines with special characters

## Metadata

- Rule ID: d7bcd677-645d-4691-a8d4-7a5602b780d1
- Status: test
- Level: high
- Author: Teymur Kheirkhabarov (idea), Vasiliy Burov (rule), oscd.community, Tim Shelton (fp)
- Date: 2020-10-15
- Modified: 2024-04-15
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_cmdline_special_characters.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection_img:
- Image|endswith:
  - \powershell.exe
  - \pwsh.exe
- OriginalFileName:
  - PowerShell.EXE
  - pwsh.dll
selection_re:
- CommandLine|re: \+.*\+.*\+.*\+.*\+.*\+.*\+.*\+.*\+.*\+.*\+.*\+.*\+.*\+
- CommandLine|re: \{.*\{.*\{.*\{.*\{.*\{.*\{.*\{.*\{.*\{
- CommandLine|re: \^.*\^.*\^.*\^.*\^
- CommandLine|re: '`.*`.*`.*`.*`'
filter_optional_amazonSSM:
  ParentImage: C:\Program Files\Amazon\SSM\ssm-document-worker.exe
filter_optional_defender_atp:
  CommandLine|contains:
  - new EventSource("Microsoft.Windows.Sense.Client.Management"
  - public static extern bool InstallELAMCertificateInfo(SafeFileHandle handle);
condition: all of selection_* and not 1 of filter_optional_*
```

## False Positives

- Amazon SSM Document Worker
- Windows Defender ATP

## References

- https://speakerdeck.com/heirhabarov/hunting-for-powershell-abuse?slide=64

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_cmdline_special_characters.yml)
