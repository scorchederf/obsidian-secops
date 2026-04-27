---
atomic_guid: "c35ac4a8-19de-43af-b9f8-755da7e89c89"
title: "Create Systemd Service file,  Enable the service , Modify and Reload the service."
framework: "atomic"
generated: "true"
attack_technique_id: "T1543.002"
attack_technique_name: "Create or Modify System Process: SysV/Systemd Service"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1543.002/T1543.002.yaml"
build_date: "2026-04-26 17:02:13"
executor: "bash"
aliases:
  - "c35ac4a8-19de-43af-b9f8-755da7e89c89"
  - "Create Systemd Service file,  Enable the service , Modify and Reload the service."
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Create Systemd Service file,  Enable the service , Modify and Reload the service.

This test creates a systemd service unit file and enables it to autostart on boot. Once service is created and enabled, it also modifies this same service file showcasing both Creation and Modification of system process.

## Metadata

- Atomic GUID: c35ac4a8-19de-43af-b9f8-755da7e89c89
- Technique: T1543.002: Create or Modify System Process: SysV/Systemd Service
- Platforms: linux
- Executor: bash
- Elevation Required: True
- Source Path: atomics/T1543.002/T1543.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543.002]]

## Dependencies

System must be Ubuntu ,Kali OR CentOS.

### Prerequisite Check

```untitled
if [ $(cat /etc/os-release | grep -i ID=ubuntu) ] || [ $(cat /etc/os-release | grep -i ID=kali) ] || [ $(cat /etc/os-release | grep -i 'ID="centos"') ]; then exit /b 0; else exit /b 1; fi;
```

### Get Prerequisite

```untitled
echo Please run from Ubuntu ,Kali OR CentOS.
```

## Executor

- elevation_required: True
- name: bash

### Command

```bash
echo "#!/bin/bash" > /etc/init.d/T1543.002
echo "### BEGIN INIT INFO" >> /etc/init.d/T1543.002
echo "# Provides : Atomic Test T1543.002" >> /etc/init.d/T1543.002
echo "# Required-Start: \$all" >> /etc/init.d/T1543.002
echo "# Required-Stop : " >> /etc/init.d/T1543.002
echo "# Default-Start: 2 3 4 5" >> /etc/init.d/T1543.002
echo "# Default-Stop: " >> /etc/init.d/T1543.002
echo "# Short Description: Atomic Test for Systemd Service Creation" >> /etc/init.d/T1543.002
echo "### END INIT INFO" >> /etc/init.d/T1543.002
echo "python3 -c \"import os, base64;exec(base64.b64decode('aW1wb3J0IG9zCm9zLnBvcGVuKCdlY2hvIGF0b21pYyB0ZXN0IGZvciBDcmVhdGluZyBTeXN0ZW1kIFNlcnZpY2UgVDE1NDMuMDAyID4gL3RtcC9UMTU0My4wMDIuc3lzdGVtZC5zZXJ2aWNlLmNyZWF0aW9uJykK')) \" " >> /etc/init.d/T1543.002
chmod +x /etc/init.d/T1543.002
if [ $(cat /etc/os-release | grep -i ID=ubuntu) ] || [ $(cat /etc/os-release | grep -i ID=kali) ]; then update-rc.d T1543.002 defaults; elif [ $(cat /etc/os-release | grep -i 'ID="centos"') ]; then chkconfig T1543.002 on ; else echo "Please run this test on Ubnutu , kali OR centos" ; fi
systemctl enable T1543.002
systemctl start T1543.002
echo "python3 -c \"import os, base64;exec(base64.b64decode('aW1wb3J0IG9zCm9zLnBvcGVuKCdlY2hvIGF0b21pYyB0ZXN0IGZvciBtb2RpZnlpbmcgYSBTeXN0ZW1kIFNlcnZpY2UgVDE1NDMuMDAyID4gL3RtcC9UMTU0My4wMDIuc3lzdGVtZC5zZXJ2aWNlLm1vZGlmaWNhdGlvbicpCg=='))\"" | sudo tee -a /etc/init.d/T1543.002
systemctl daemon-reload
systemctl restart T1543.002
```

### Cleanup

```bash
systemctl stop T1543.002
systemctl disable T1543.002
rm -rf /etc/init.d/T1543.002
systemctl daemon-reload
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1543.002/T1543.002.yaml)
