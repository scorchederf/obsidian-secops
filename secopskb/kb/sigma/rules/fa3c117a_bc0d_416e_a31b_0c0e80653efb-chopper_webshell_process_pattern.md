---
sigma_id: "fa3c117a-bc0d-416e-a31b-0c0e80653efb"
title: "Chopper Webshell Process Pattern"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_webshell_chopper.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_webshell_chopper.yml"
build_date: "2026-04-26 15:01:43"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "fa3c117a-bc0d-416e-a31b-0c0e80653efb"
  - "Chopper Webshell Process Pattern"
attack_technique_ids:
  - "T1505.003"
  - "T1018"
  - "T1033"
  - "T1087"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Chopper Webshell Process Pattern

Detects patterns found in process executions cause by China Chopper like tiny (ASPX) webshells

## Metadata

- Rule ID: fa3c117a-bc0d-416e-a31b-0c0e80653efb
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems), MSTI (query)
- Date: 2022-10-01
- Source Path: rules/windows/process_creation/proc_creation_win_webshell_chopper.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1505-server_software_component|T1505.003]]
- [[kb/attack/techniques/T1018-remote_system_discovery|T1018]]
- [[kb/attack/techniques/T1033-system_owner_user_discovery|T1033]]
- [[kb/attack/techniques/T1087-account_discovery|T1087]]

## Detection

```yaml
selection_origin:
- Image|endswith: \w3wp.exe
- ParentImage|endswith: \w3wp.exe
selection_cmdline:
  CommandLine|contains:
  - '&ipconfig&echo'
  - '&quser&echo'
  - '&whoami&echo'
  - '&c:&echo'
  - '&cd&echo'
  - '&dir&echo'
  - '&echo [E]'
  - '&echo [S]'
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://www.microsoft.com/security/blog/2022/09/30/analyzing-attacks-using-the-exchange-vulnerabilities-cve-2022-41040-and-cve-2022-41082/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_webshell_chopper.yml)
