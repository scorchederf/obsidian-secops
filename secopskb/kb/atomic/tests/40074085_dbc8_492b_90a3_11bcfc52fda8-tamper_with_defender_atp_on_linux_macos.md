---
atomic_guid: "40074085-dbc8-492b-90a3-11bcfc52fda8"
title: "Tamper with Defender ATP on Linux/MacOS"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.001"
attack_technique_name: "Impair Defenses: Disable or Modify Tools"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml"
build_date: "2026-04-27 19:12:28"
executor: "sh"
aliases:
  - "40074085-dbc8-492b-90a3-11bcfc52fda8"
  - "Tamper with Defender ATP on Linux/MacOS"
platforms:
  - "linux"
  - "macos"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

With root privileges, an adversary can disable real time protection. Note, this test assumes Defender is not in passive mode and real-time protection is enabled. The use of a managed.json on Linux or Defender .plist on MacOS will prevent these changes. Tamper protection will also prevent this (available on MacOS, but not Linux at the time of writing). Installation of MDATP is a prerequisite. Installation steps vary across MacOS and Linux distros. See Microsoft public documentation for instructions: https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/mac-install-manually?view=o365-worldwide https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/linux-install-manually?view=o365-worldwide

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses#^t1562001-disable-or-modify-tools|T1562.001: Disable or Modify Tools]]

## Executor

- elevation_required: True
- name: sh

### Command

```bash
sudo mdatp config real-time-protection --value disabled
```

### Cleanup

```bash
sudo mdatp config real-time-protection --value enabled
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml)
