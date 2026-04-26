---
sigma_id: "e6c54d94-498c-4562-a37c-b469d8e9a275"
title: "Suspicious PowerShell Download and Execute Pattern"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_susp_download_patterns.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_susp_download_patterns.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "e6c54d94-498c-4562-a37c-b469d8e9a275"
  - "Suspicious PowerShell Download and Execute Pattern"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious PowerShell Download and Execute Pattern

Detects suspicious PowerShell download patterns that are often used in malicious scripts, stagers or downloaders (make sure that your backend applies the strings case-insensitive)

## Metadata

- Rule ID: e6c54d94-498c-4562-a37c-b469d8e9a275
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-02-28
- Modified: 2022-03-01
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_susp_download_patterns.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection:
  CommandLine|contains:
  - IEX ((New-Object Net.WebClient).DownloadString
  - IEX (New-Object Net.WebClient).DownloadString
  - IEX((New-Object Net.WebClient).DownloadString
  - IEX(New-Object Net.WebClient).DownloadString
  - ' -command (New-Object System.Net.WebClient).DownloadFile('
  - ' -c (New-Object System.Net.WebClient).DownloadFile('
condition: selection
```

## False Positives

- Software installers that pull packages from remote systems and execute them

## References

- https://gist.github.com/jivoi/c354eaaf3019352ce32522f916c03d70
- https://www.trendmicro.com/en_us/research/22/j/lv-ransomware-exploits-proxyshell-in-attack.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_susp_download_patterns.yml)
