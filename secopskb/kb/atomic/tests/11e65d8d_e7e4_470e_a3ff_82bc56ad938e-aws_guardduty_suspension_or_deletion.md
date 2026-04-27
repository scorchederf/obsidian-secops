---
atomic_guid: "11e65d8d-e7e4-470e-a3ff-82bc56ad938e"
title: "AWS - GuardDuty Suspension or Deletion"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.001"
attack_technique_name: "Impair Defenses: Disable or Modify Tools"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml"
build_date: "2026-04-27 19:12:28"
executor: "bash"
aliases:
  - "11e65d8d-e7e4-470e-a3ff-82bc56ad938e"
  - "AWS - GuardDuty Suspension or Deletion"
platforms:
  - "iaas:aws"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Enables GuardDuty in AWS, upon successful creation this test will suspend and then delete the GuardDuty configuration.

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses#^t1562001-disable-or-modify-tools|T1562.001: Disable or Modify Tools]]

## Input Arguments

### region

- description: Name of the specified region
- type: string
- default: us-east-1

## Dependencies

Check if ~/.aws/credentials file has a default stanza is configured

### Prerequisite Check

```bash
cat ~/.aws/credentials | grep "default"
```

### Get Prerequisite

```bash
echo "Please install the aws-cli and configure your AWS default profile using: aws configure"
```

## Executor

- elevation_required: False
- name: bash

### Command

```bash
detectorId=$(aws guardduty create-detector --enable --region "#{region}" | grep -oP '(?<="DetectorId": ")[^"]*')
aws guardduty update-detector --no-enable --detector-id $detectorId
aws guardduty delete-detector --detector-id $detectorId
```

### Cleanup

```bash
echo "If test successfully ran, no cleanup required."
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml)
