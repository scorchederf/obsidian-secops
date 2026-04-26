---
atomic_guid: "99ee161b-dcb1-4276-8ecb-7cfdcb207820"
title: "AWS - EC2 Enumeration from Cloud Instance"
framework: "atomic"
generated: "true"
attack_technique_id: "T1580"
attack_technique_name: "Cloud Infrastructure Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1580/T1580.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "99ee161b-dcb1-4276-8ecb-7cfdcb207820"
  - "AWS - EC2 Enumeration from Cloud Instance"
platforms:
  - "linux"
  - "macos"
  - "iaas:aws"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# AWS - EC2 Enumeration from Cloud Instance

This atomic runs several API calls (sts:GetCallerIdentity, s3:ListBuckets, iam:GetAccountSummary, iam:ListRoles, iam:ListUsers, iam:GetAccountAuthorizationDetails, ec2:DescribeSnapshots, cloudtrail:DescribeTrails, guardduty:ListDetectors) from the context of an EC2 instance role. This simulates an attacker compromising an EC2 instance and running initial discovery commands on it. This atomic test leverages a tool called stratus-red-team built by DataDog (https://github.com/DataDog/stratus-red-team). Stratus Red Team is a self-contained binary. You can use it to easily detonate offensive attack techniques against a live cloud environment. Ref: https://stratus-red-team.cloud/attack-techniques/AWS/aws.discovery.ec2-enumerate-from-instance/

## Metadata

- Atomic GUID: 99ee161b-dcb1-4276-8ecb-7cfdcb207820
- Technique: T1580: Cloud Infrastructure Discovery
- Platforms: linux, macos, iaas:aws
- Executor: sh
- Elevation Required: False
- Dependency Executor: sh
- Source Path: atomics/T1580/T1580.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1580-cloud_infrastructure_discovery|T1580]]

## Input Arguments

### aws_region

- description: AWS region to detonate
- type: string
- default: us-west-2

### stratus_path

- description: Path of stratus binary
- type: path
- default: $PathToAtomicsFolder/T1580/src

## Dependencies

Stratus binary must be present at the (#{stratus_path}/stratus)

### Prerequisite Check

```bash
if test -f "#{stratus_path}/stratus"; then exit 0; else exit 1; fi
```

### Get Prerequisite

```bash
if [ "$(uname)" = "Darwin" ]
then DOWNLOAD_URL=$(curl -s https://api.github.com/repos/DataDog/stratus-red-team/releases/latest | grep browser_download_url | grep -i Darwin_x86_64 | cut -d '"' -f 4); wget -q -O #{stratus_path}/stratus-red-team-latest.tar.gz $DOWNLOAD_URL
  tar -xzvf #{stratus_path}/stratus-red-team-latest.tar.gz --directory #{stratus_path}/
elif [ "$(expr substr $(uname) 1 5)" = "Linux" ]
then DOWNLOAD_URL=$(curl -s https://api.github.com/repos/DataDog/stratus-red-team/releases/latest | grep browser_download_url | grep -i linux_x86_64 | cut -d '"' -f 4); wget -q -O #{stratus_path}/stratus-red-team-latest.tar.gz $DOWNLOAD_URL
  tar -xzvf #{stratus_path}/stratus-red-team-latest.tar.gz --directory #{stratus_path}/
fi
```

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
- name: sh

### Command

```bash
export AWS_REGION=#{aws_region}
cd #{stratus_path}
echo "Stratus: Start Warmup."
./stratus warmup aws.discovery.ec2-enumerate-from-instance
echo "Stratus: Start Detonate."
./stratus detonate aws.discovery.ec2-enumerate-from-instance
```

### Cleanup

```bash
cd #{stratus_path}
echo "Stratus: Start Cleanup."
./stratus cleanup aws.discovery.ec2-enumerate-from-instance
echo "Removing Stratus artifacts from local machine."
rm -rf stratus*
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1580/T1580.yaml)
