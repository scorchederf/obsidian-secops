---
atomic_guid: "25e2be0e-96f7-4417-bd16-a4a2500e3802"
title: "Copy and Delete Mailbox Data on Linux"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.008"
attack_technique_name: "Email Collection: Mailbox Manipulation"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.008/T1070.008.yaml"
build_date: "2026-04-26 14:38:39"
executor: "bash"
aliases:
  - "25e2be0e-96f7-4417-bd16-a4a2500e3802"
  - "Copy and Delete Mailbox Data on Linux"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Copy and Delete Mailbox Data on Linux

Copies and deletes mail data on Linux

## Metadata

- Atomic GUID: 25e2be0e-96f7-4417-bd16-a4a2500e3802
- Technique: T1070.008: Email Collection: Mailbox Manipulation
- Platforms: linux
- Executor: bash
- Elevation Required: True
- Source Path: atomics/T1070.008/T1070.008.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal|T1070.008]]

## Dependencies

Create dummy file in /var/spool/mail/ if no files exist

### Prerequisite Check

```text
if [ -z "$(ls -A /var/spool/mail/)" ]; then exit 1; else exit 0; fi
```

### Get Prerequisite

```text
if [ -z "$(ls -A /var/spool/mail/)" ]; then touch /var/spool/mail/temp; fi
```

## Executor

- elevation_required: True
- name: bash

### Command

```bash
mkdir -p /var/spool/mail/copy && for file in /var/spool/mail/*; do if [ "$(basename "$file")" != "copy" ]; then cp -R "$file" /var/spool/mail/copy/; fi; done && rm -rf /var/spool/mail/copy/*
```

### Cleanup

```bash
rm -rf /var/spool/mail/copy
if [ -f "$(ls -A /var/spool/mail/temp)" ]; then rm /var/spool/mail/temp; fi
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.008/T1070.008.yaml)
