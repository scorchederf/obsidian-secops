---
atomic_guid: "31dad7ad-2286-4c02-ae92-274418c85fec"
title: "Linux VM Check via Hardware"
framework: "atomic"
generated: "true"
attack_technique_id: "T1082"
attack_technique_name: "System Information Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1082/T1082.yaml"
build_date: "2026-04-26 17:02:12"
executor: "bash"
aliases:
  - "31dad7ad-2286-4c02-ae92-274418c85fec"
  - "Linux VM Check via Hardware"
platforms:
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Linux VM Check via Hardware

Identify virtual machine hardware. This technique is used by the Pupy RAT and other malware.

## Metadata

- Atomic GUID: 31dad7ad-2286-4c02-ae92-274418c85fec
- Technique: T1082: System Information Discovery
- Platforms: linux
- Executor: bash
- Elevation Required: True
- Source Path: atomics/T1082/T1082.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1082-system_information_discovery|T1082]]

## Executor

- elevation_required: True
- name: bash

### Command

```bash
if [ -f /sys/class/dmi/id/bios_version ]; then cat /sys/class/dmi/id/bios_version | grep -i amazon; fi
if [ -f /sys/class/dmi/id/product_name ]; then cat /sys/class/dmi/id/product_name | grep -i "Droplet\|HVM\|VirtualBox\|VMware"; fi
if [ -f /sys/class/dmi/id/chassis_vendor ]; then cat /sys/class/dmi/id/chassis_vendor | grep -i "Xen\|Bochs\|QEMU"; fi
if [ -x "$(command -v dmidecode)" ]; then sudo dmidecode | grep -i "microsoft\|vmware\|virtualbox\|quemu\|domu"; fi
if [ -f /proc/scsi/scsi ]; then cat /proc/scsi/scsi | grep -i "vmware\|vbox"; fi
if [ -f /proc/ide/hd0/model ]; then cat /proc/ide/hd0/model | grep -i "vmware\|vbox\|qemu\|virtual"; fi
if [ -x "$(command -v lspci)" ]; then sudo lspci | grep -i "vmware\|virtualbox"; fi
if [ -x "$(command -v lscpu)" ]; then sudo lscpu | grep -i "Xen\|KVM\|Microsoft"; fi
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1082/T1082.yaml)
