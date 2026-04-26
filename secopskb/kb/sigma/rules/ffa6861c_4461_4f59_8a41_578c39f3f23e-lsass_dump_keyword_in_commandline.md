---
sigma_id: "ffa6861c-4461-4f59-8a41-578c39f3f23e"
title: "LSASS Dump Keyword In CommandLine"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_lsass_dmp_cli_keywords.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_lsass_dmp_cli_keywords.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "ffa6861c-4461-4f59-8a41-578c39f3f23e"
  - "LSASS Dump Keyword In CommandLine"
attack_technique_ids:
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# LSASS Dump Keyword In CommandLine

Detects the presence of the keywords "lsass" and ".dmp" in the commandline, which could indicate a potential attempt to dump or create a dump of the lsass process.

## Metadata

- Rule ID: ffa6861c-4461-4f59-8a41-578c39f3f23e
- Status: test
- Level: high
- Author: E.M. Anhaus, Tony Lambert, oscd.community, Nasreddine Bencherchali (Nextron Systems)
- Date: 2019-10-24
- Modified: 2023-08-29
- Source Path: rules/windows/process_creation/proc_creation_win_susp_lsass_dmp_cli_keywords.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]

## Detection

```yaml
selection:
- CommandLine|contains:
  - lsass.dmp
  - lsass.zip
  - lsass.rar
  - Andrew.dmp
  - Coredump.dmp
  - NotLSASS.zip
  - lsass_2
  - lsassdump
  - lsassdmp
- CommandLine|contains|all:
  - lsass
  - .dmp
- CommandLine|contains|all:
  - SQLDmpr
  - .mdmp
- CommandLine|contains|all:
  - nanodump
  - .dmp
condition: selection
```

## False Positives

- Unlikely

## References

- https://github.com/Hackndo/lsassy
- https://medium.com/@markmotig/some-ways-to-dump-lsass-exe-c4a75fdc49bf
- https://github.com/elastic/detection-rules/blob/c76a39796972ecde44cb1da6df47f1b6562c9770/rules/windows/credential_access_lsass_memdump_file_created.toml
- https://www.whiteoaksecurity.com/blog/attacks-defenses-dumping-lsass-no-mimikatz/
- https://github.com/helpsystems/nanodump
- https://github.com/CCob/MirrorDump

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_lsass_dmp_cli_keywords.yml)
