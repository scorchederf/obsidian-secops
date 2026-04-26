---
atomic_guid: "4608bc1b-e682-466b-a7d7-dbd76760db31"
title: "AWS - Config Logs Disabled"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.008"
attack_technique_name: "Impair Defenses: Disable Cloud Logs"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.008/T1562.008.yaml"
build_date: "2026-04-26 14:38:40"
executor: "sh"
aliases:
  - "4608bc1b-e682-466b-a7d7-dbd76760db31"
  - "AWS - Config Logs Disabled"
platforms:
  - "iaas:aws"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# AWS - Config Logs Disabled

Disables AWS Config by stopping the configuration recorder, deleting the delivery channel, and deleting the configuration recorder. An attacker with sufficient permissions can use this to stop configuration change recording and avoid detection of subsequent activity.

## Metadata

- Atomic GUID: 4608bc1b-e682-466b-a7d7-dbd76760db31
- Technique: T1562.008: Impair Defenses: Disable Cloud Logs
- Platforms: iaas:aws
- Executor: sh
- Elevation Required: False
- Source Path: atomics/T1562.008/T1562.008.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.008]]

## Input Arguments

### configuration_recorder_name

- description: Name of the configuration recorder
- type: string
- default: redatomictestconfigurationrecorder

### delivery_channel_name

- description: Name of the delivery channel
- type: string
- default: redatomictestdeliverychannel

### region

- description: Name of the region
- type: string
- default: us-west-2

## Dependencies

Check if ~/.aws/credentials file has a default stanza is configured

### Prerequisite Check

```text
cat ~/.aws/credentials | grep "default"
```

### Get Prerequisite

```text
echo Please install the aws-cli and configure your AWS default profile using: aws configure
```

Check if terraform is installed.

### Prerequisite Check

```text
terraform version
```

### Get Prerequisite

```text
echo Please install terraform and configure your AWS default profile
```

## Executor

- elevation_required: False
- name: sh

### Command

```sh
aws configservice stop-configuration-recorder --configuration-recorder-name #{configuration_recorder_name} --region #{region}
echo "*** Configuration recorder stopped ***"
aws configservice delete-delivery-channel --delivery-channel-name #{delivery_channel_name} --region #{region}
echo "*** Delivery channel deleted ***"
aws configservice delete-configuration-recorder --configuration-recorder-name #{configuration_recorder_name} --region #{region}
echo "*** Configuration recorder deleted ***"
```

### Cleanup

```sh
aws configservice list-configuration-recorders --region us-west-2
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.008/T1562.008.yaml)
