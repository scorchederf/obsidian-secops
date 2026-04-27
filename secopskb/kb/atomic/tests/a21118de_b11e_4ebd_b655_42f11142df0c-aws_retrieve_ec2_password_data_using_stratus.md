---
atomic_guid: "a21118de-b11e-4ebd-b655-42f11142df0c"
title: "AWS - Retrieve EC2 Password Data using stratus"
framework: "atomic"
generated: "true"
attack_technique_id: "T1552"
attack_technique_name: "Unsecured Credentials"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552/T1552.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "a21118de-b11e-4ebd-b655-42f11142df0c"
  - "AWS - Retrieve EC2 Password Data using stratus"
platforms:
  - "linux"
  - "macos"
  - "iaas:aws"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# AWS - Retrieve EC2 Password Data using stratus

This atomic runs an API call GetPasswordData from a role that does not have permission to do so. This simulates an attacker attempting to retrieve RDP passwords on a high number of Windows EC2 instances. This atomic test leverages a tool called stratus-red-team built by DataDog (https://github.com/DataDog/stratus-red-team). Stratus Red Team is a self-contained binary. You can use it to easily detonate offensive attack techniques against a live cloud environment. Ref: https://stratus-red-team.cloud/attack-techniques/AWS/aws.credential-access.ec2-get-password-data/

## Metadata

- Atomic GUID: a21118de-b11e-4ebd-b655-42f11142df0c
- Technique: T1552: Unsecured Credentials
- Platforms: linux, macos, iaas:aws
- Executor: sh
- Elevation Required: False
- Dependency Executor: sh
- Source Path: atomics/T1552/T1552.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1552-unsecured_credentials|T1552]]

## Input Arguments

### aws_region

- description: AWS region to detonate
- type: string
- default: us-west-2

### stratus_path

- description: Path of stratus binary
- type: path
- default: $PathToAtomicsFolder/T1552/src

## Dependencies

Stratus binary must be present at the (#{stratus_path}/stratus)

### Prerequisite Check

```bash
if [ -f #{stratus_path}/stratus ]; then exit 0; else exit 1; fi;
```

### Get Prerequisite

```bash
if [ "$(uname)" == "Darwin" ]
then DOWNLOAD_URL=$(curl -s https://api.github.com/repos/DataDog/stratus-red-team/releases/latest | grep browser_download_url | grep Darwin_x86_64 | cut -d '"' -f 4); wget -q -O #{stratus_path}/stratus-red-team-latest.tar.gz $DOWNLOAD_URL
  tar -xzvf #{stratus_path}/stratus-red-team-latest.tar.gz --directory #{stratus_path}/
elif [ "$(expr substr $(uname) 1 5)" == "Linux" ]
then DOWNLOAD_URL=$(curl -s https://api.github.com/repos/DataDog/stratus-red-team/releases/latest | grep browser_download_url | grep Linux_x86_64 | cut -d '"' -f 4) 
  wget -q -O #{stratus_path}/stratus-red-team-latest.tar.gz $DOWNLOAD_URL
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
echo Please install the aws-cli and configure your AWS defult profile using: aws configure
```

## Executor

- elevation_required: False
- name: sh

### Command

```bash
export AWS_REGION=#{aws_region} 
cd #{stratus_path}
echo "starting warmup"
./stratus warmup aws.credential-access.ec2-get-password-data
echo "starting detonate"
./stratus detonate aws.credential-access.ec2-get-password-data --force
```

### Cleanup

```bash
export AWS_REGION=#{aws_region}
echo "Cleanup detonation"
cd #{stratus_path}
./stratus cleanup --all
rm -rf stratus*
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1552/T1552.yaml)
