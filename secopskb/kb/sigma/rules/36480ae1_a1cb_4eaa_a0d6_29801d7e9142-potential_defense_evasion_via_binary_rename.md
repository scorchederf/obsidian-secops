---
sigma_id: "36480ae1-a1cb-4eaa-a0d6-29801d7e9142"
title: "Potential Defense Evasion Via Binary Rename"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_renamed_binary.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_binary.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "36480ae1-a1cb-4eaa-a0d6-29801d7e9142"
  - "Potential Defense Evasion Via Binary Rename"
attack_technique_ids:
  - "T1036.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Defense Evasion Via Binary Rename

Detects the execution of a renamed binary often used by attackers or malware leveraging new Sysmon OriginalFileName datapoint.

## Metadata

- Rule ID: 36480ae1-a1cb-4eaa-a0d6-29801d7e9142
- Status: test
- Level: medium
- Author: Matthew Green @mgreen27, Ecco, James Pemberton @4A616D6573, oscd.community, Andreas Hunkeler (@Karneades)
- Date: 2019-06-15
- Modified: 2025-07-15
- Source Path: rules/windows/process_creation/proc_creation_win_renamed_binary.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036.003]]

## Detection

```yaml
selection:
  OriginalFileName:
  - Cmd.Exe
  - CONHOST.EXE
  - 7z.exe
  - 7za.exe
  - WinRAR.exe
  - wevtutil.exe
  - net.exe
  - net1.exe
  - netsh.exe
  - InstallUtil.exe
filter:
  Image|endswith:
  - \cmd.exe
  - \conhost.exe
  - \7z.exe
  - \7za.exe
  - \WinRAR.exe
  - \wevtutil.exe
  - \net.exe
  - \net1.exe
  - \netsh.exe
  - \InstallUtil.exe
condition: selection and not filter
```

## False Positives

- Custom applications use renamed binaries adding slight change to binary name. Typically this is easy to spot and add to whitelist

## References

- https://mgreen27.github.io/posts/2019/05/12/BinaryRename.html
- https://mgreen27.github.io/posts/2019/05/29/BinaryRename2.html
- https://github.com/redcanaryco/atomic-red-team/blob/0f229c0e42bfe7ca736a14023836d65baa941ed2/atomics/T1036.003/T1036.003.md#atomic-test-1---masquerading-as-windows-lsass-process
- https://www.splunk.com/en_us/blog/security/inno-setup-malware-redline-stealer-campaign.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_binary.yml)
