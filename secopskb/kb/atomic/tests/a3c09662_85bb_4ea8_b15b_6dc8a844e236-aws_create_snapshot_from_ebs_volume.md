---
atomic_guid: "a3c09662-85bb-4ea8-b15b-6dc8a844e236"
title: "AWS - Create Snapshot from EBS Volume"
framework: "atomic"
generated: "true"
attack_technique_id: "T1578.001"
attack_technique_name: "Modify Cloud Compute Infrastructure: Create Snapshot"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1578.001/T1578.001.yaml"
build_date: "2026-04-27 19:12:28"
executor: "sh"
aliases:
  - "a3c09662-85bb-4ea8-b15b-6dc8a844e236"
  - "AWS - Create Snapshot from EBS Volume"
platforms:
  - "iaas:aws"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Creates an EBS snapshot in AWS using the AWS CLI.
This simulates an adversary duplicating volume data via snapshots for persistence or exfiltration.

## ATT&CK Mapping

- [[kb/attack/techniques/T1578-modify_cloud_compute_infrastructure#^t1578001-create-snapshot|T1578.001: Create Snapshot]]

## Input Arguments

### aws_region

- description: AWS region where the volume is located.
- type: string
- default: us-east-1

### aws_volume_id

- description: The AWS EBS Volume ID to create a snapshot from.
- type: string
- default: vol-0123456789abcdef0

## Dependencies

AWS CLI must be installed.

### Prerequisite Check

```untitled
if command -v aws > /dev/null 2>&1; then exit 0; else exit 1; fi
```

### Get Prerequisite

```untitled
echo "Install AWS CLI: https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html"
```

AWS CLI must be authenticated.

### Prerequisite Check

```untitled
if aws sts get-caller-identity --region #{aws_region} > /dev/null 2>&1; then exit 0; else exit 1; fi
```

### Get Prerequisite

```untitled
echo "Configure AWS credentials with: aws configure"
```

EBS volume must exist.

### Prerequisite Check

```untitled
if aws ec2 describe-volumes --volume-ids #{aws_volume_id} --region #{aws_region} > /dev/null 2>&1; then exit 0; else exit 1; fi
```

### Get Prerequisite

```untitled
echo "Ensure the volume ID exists in the target AWS account and region."
```

## Executor

- elevation_required: False
- name: sh

### Command

```bash
aws ec2 create-snapshot --region #{aws_region} --volume-id #{aws_volume_id} --description "Atomic Red Team Test Snapshot" --query "SnapshotId" --output text
```

### Cleanup

```bash
SNAPSHOT_ID=$(aws ec2 describe-snapshots --region #{aws_region} --filters "Name=volume-id,Values=#{aws_volume_id}" --query "Snapshots[0].SnapshotId" --output text)
if [ "$SNAPSHOT_ID" != "None" ]; then
  aws ec2 delete-snapshot --region #{aws_region} --snapshot-id "$SNAPSHOT_ID"
fi
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1578.001/T1578.001.yaml)
