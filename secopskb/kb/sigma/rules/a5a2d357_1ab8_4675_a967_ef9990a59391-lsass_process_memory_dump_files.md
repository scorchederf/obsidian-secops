---
sigma_id: "a5a2d357-1ab8-4675-a967-ef9990a59391"
title: "LSASS Process Memory Dump Files"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_lsass_default_dump_file_names.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_lsass_default_dump_file_names.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "a5a2d357-1ab8-4675-a967-ef9990a59391"
  - "LSASS Process Memory Dump Files"
attack_technique_ids:
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# LSASS Process Memory Dump Files

Detects creation of files with names used by different memory dumping tools to create a memory dump of the LSASS process memory, which contains user credentials.

## Metadata

- Rule ID: a5a2d357-1ab8-4675-a967-ef9990a59391
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2021-11-15
- Modified: 2024-10-08
- Source Path: rules/windows/file/file_event/file_event_win_lsass_default_dump_file_names.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]

## Detection

```yaml
selection_1:
  TargetFilename|endswith:
  - \Andrew.dmp
  - \Coredump.dmp
  - \lsass.dmp
  - \lsass.rar
  - \lsass.zip
  - \NotLSASS.zip
  - \PPLBlade.dmp
  - \rustive.dmp
selection_2:
  TargetFilename|contains:
  - \lsass_2
  - \lsassdmp
  - \lsassdump
selection_3:
  TargetFilename|contains|all:
  - \lsass
  - .dmp
selection_4:
  TargetFilename|contains: SQLDmpr
  TargetFilename|endswith: .mdmp
selection_5:
  TargetFilename|contains:
  - \nanodump
  - \proc_
  TargetFilename|endswith: .dmp
condition: 1 of selection_*
```

## False Positives

- Unknown

## References

- https://www.google.com/search?q=procdump+lsass
- https://medium.com/@markmotig/some-ways-to-dump-lsass-exe-c4a75fdc49bf
- https://github.com/elastic/detection-rules/blob/c76a39796972ecde44cb1da6df47f1b6562c9770/rules/windows/credential_access_lsass_memdump_file_created.toml
- https://www.whiteoaksecurity.com/blog/attacks-defenses-dumping-lsass-no-mimikatz/
- https://github.com/helpsystems/nanodump
- https://github.com/CCob/MirrorDump
- https://github.com/safedv/RustiveDump/blob/1a9b026b477587becfb62df9677cede619d42030/src/main.rs#L35
- https://github.com/ricardojoserf/NativeDump/blob/01d8cd17f31f51f5955a38e85cd3c83a17596175/NativeDump/Program.cs#L258

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_lsass_default_dump_file_names.yml)
