---
sigma_id: "5afee48e-67dd-4e03-a783-f74259dcf998"
title: "Potential LSASS Process Dump Via Procdump"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_sysinternals_procdump_lsass.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sysinternals_procdump_lsass.yml"
build_date: "2026-04-26 15:01:48"
status: "stable"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "5afee48e-67dd-4e03-a783-f74259dcf998"
  - "Potential LSASS Process Dump Via Procdump"
attack_technique_ids:
  - "T1036"
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potential LSASS Process Dump Via Procdump

Detects potential credential harvesting attempts through LSASS memory dumps using ProcDump.
This rule identifies suspicious command-line patterns that combine memory dump flags (-ma, -mm, -mp) with LSASS-related process markers.
LSASS (Local Security Authority Subsystem Service) contains sensitive authentication data including plaintext passwords, NTLM hashes, and Kerberos tickets in memory.
Attackers commonly dump LSASS memory to extract credentials for lateral movement and privilege escalation.

## Metadata

- Rule ID: 5afee48e-67dd-4e03-a783-f74259dcf998
- Status: stable
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2018-10-30
- Modified: 2025-10-19
- Source Path: rules/windows/process_creation/proc_creation_win_sysinternals_procdump_lsass.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036]]
- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]

## Detection

```yaml
selection_flags:
  CommandLine|contains|windash:
  - ' -ma '
  - ' -mm '
  - ' -mp '
selection_process:
  CommandLine|contains:
  - ' ls'
  - ' keyiso'
  - ' samss'
condition: all of selection_*
```

## False Positives

- Unlikely, because no one should dump an lsass process memory
- Another tool that uses command line flags similar to ProcDump

## References

- https://learn.microsoft.com/en-us/sysinternals/downloads/procdump
- https://research.splunk.com/endpoint/3742ebfe-64c2-11eb-ae93-0242ac130002
- https://x.com/wietze/status/1958302556033065292?s=12

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sysinternals_procdump_lsass.yml)
