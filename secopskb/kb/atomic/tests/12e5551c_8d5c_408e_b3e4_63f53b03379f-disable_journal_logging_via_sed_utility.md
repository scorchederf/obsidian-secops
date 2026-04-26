---
atomic_guid: "12e5551c-8d5c-408e-b3e4-63f53b03379f"
title: "Disable journal logging via sed utility"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562"
attack_technique_name: "Impair Defenses"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562/T1562.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "12e5551c-8d5c-408e-b3e4-63f53b03379f"
  - "Disable journal logging via sed utility"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Disable journal logging via sed utility

The atomic test disables the journal logging by searching and replacing the "Storage" parameter to "none" within the journald.conf file, thus any new journal entries will only be temporarily available in memory and not written to disk

## Metadata

- Atomic GUID: 12e5551c-8d5c-408e-b3e4-63f53b03379f
- Technique: T1562: Impair Defenses
- Platforms: linux
- Executor: sh
- Elevation Required: True
- Source Path: atomics/T1562/T1562.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562]]

## Executor

- elevation_required: True
- name: sh

### Command

```bash
sudo sed -i 's/Storage=auto/Storage=none/' /etc/systemd/journald.conf
```

### Cleanup

```bash
sudo sed -i 's/Storage=none/Storage=auto/' /etc/systemd/journald.conf #re-enables storage of journal data
sudo systemctl restart systemd-journald #restart the journal service
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562/T1562.yaml)
