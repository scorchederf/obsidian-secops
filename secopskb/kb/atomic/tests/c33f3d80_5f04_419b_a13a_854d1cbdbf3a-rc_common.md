---
atomic_guid: "c33f3d80-5f04-419b-a13a-854d1cbdbf3a"
title: "rc.common"
framework: "atomic"
generated: "true"
attack_technique_id: "T1037.004"
attack_technique_name: "Boot or Logon Initialization Scripts: Rc.common"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1037.004/T1037.004.yaml"
build_date: "2026-04-26 17:02:12"
executor: "bash"
aliases:
  - "c33f3d80-5f04-419b-a13a-854d1cbdbf3a"
  - "rc.common"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# rc.common

Modify rc.common

## Metadata

- Atomic GUID: c33f3d80-5f04-419b-a13a-854d1cbdbf3a
- Technique: T1037.004: Boot or Logon Initialization Scripts: Rc.common
- Platforms: linux
- Executor: bash
- Elevation Required: True
- Source Path: atomics/T1037.004/T1037.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1037-boot_or_logon_initialization_scripts|T1037.004]]

## Executor

- elevation_required: True
- name: bash

### Command

```bash
filename='/etc/rc.common';if [ ! -f $filename ];then sudo touch $filename;else sudo cp $filename /etc/rc.common.original;fi
printf '%s\n' '#!/bin/bash' | sudo tee /etc/rc.common
echo "python3 -c \"import os, base64;exec(base64.b64decode('aW1wb3J0IG9zCm9zLnBvcGVuKCdlY2hvIGF0b21pYyB0ZXN0IGZvciBtb2RpZnlpbmcgcmMuY29tbW9uID4gL3RtcC9UMTAzNy4wMDQucmMuY29tbW9uJykK'))\"" | sudo tee -a /etc/rc.common
printf '%s\n' 'exit 0' | sudo tee -a /etc/rc.common
sudo chmod +x /etc/rc.common
```

### Cleanup

```bash
origfilename='/etc/rc.common.original';if [ ! -f $origfilename ];then sudo rm /etc/rc.common;else sudo cp $origfilename /etc/rc.common && sudo rm $origfilename;fi
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1037.004/T1037.004.yaml)
