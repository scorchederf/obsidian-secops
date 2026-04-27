---
atomic_guid: "6d99f93c-da56-49e3-b195-163090ace4f6"
title: "Copy and Modify Mailbox Data on Linux"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.008"
attack_technique_name: "Email Collection: Mailbox Manipulation"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.008/T1070.008.yaml"
build_date: "2026-04-27 19:12:26"
executor: "bash"
aliases:
  - "6d99f93c-da56-49e3-b195-163090ace4f6"
  - "Copy and Modify Mailbox Data on Linux"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Copies and modifies mail data on Linux

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal#^t1070008-clear-mailbox-data|T1070.008: Clear Mailbox Data]]

## Dependencies

Create dummy file in /var/spool/mail/ if no files exist

### Prerequisite Check

```untitled
if [ -z "$(ls -A /var/spool/mail/)" ]; then exit 1; else exit 0; fi
```

### Get Prerequisite

```untitled
if [ -z "$(ls -A /var/spool/mail/)" ]; then touch /var/spool/mail/temp; fi
```

## Executor

- elevation_required: True
- name: bash

### Command

```bash
mkdir -p /var/spool/mail/copy; for file in /var/spool/mail/*; do if [ "$(basename "$file")" != "copy" ]; then cp -R "$file" /var/spool/mail/copy/; if [ -f "/var/spool/mail/copy/$(basename "$file")" ]; then echo "Modification for Atomic Red Test" >> "/var/spool/mail/copy/$(basename "$file")"; fi; fi; done
```

### Cleanup

```bash
rm -rf /var/spool/mail/copy
if [ -f "$(ls -A /var/spool/mail/temp)" ]; then rm /var/spool/mail/temp; fi
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.008/T1070.008.yaml)
