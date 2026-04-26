---
atomic_guid: "22d89a2f-d475-4895-b2d4-68626d49c029"
title: "AWS - CloudTrail Logs Impairment Through S3 Lifecycle Rule using Stratus"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.008"
attack_technique_name: "Impair Defenses: Disable Cloud Logs"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.008/T1562.008.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "22d89a2f-d475-4895-b2d4-68626d49c029"
  - "AWS - CloudTrail Logs Impairment Through S3 Lifecycle Rule using Stratus"
platforms:
  - "linux"
  - "macos"
  - "iaas:aws"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# AWS - CloudTrail Logs Impairment Through S3 Lifecycle Rule using Stratus

This Atomic test will use the Stratus Red Team will first setup a CloudTrail logging into an S3 bucket and will then make an API call to update the lifecycle rule on that S3 bucket with an expiration date of 1 day. This will essentially delete all the logs after one day. Adversaries often do this actiivity to evade detection. Stratus Red Team is a self-contained binary. You can use it to easily detonate offensive attack techniques against a live cloud environment. ref: https://stratus-red-team.cloud/attack-techniques/AWS/aws.defense-evasion.cloudtrail-lifecycle-rule/

## Metadata

- Atomic GUID: 22d89a2f-d475-4895-b2d4-68626d49c029
- Technique: T1562.008: Impair Defenses: Disable Cloud Logs
- Platforms: linux, macos, iaas:aws
- Executor: sh
- Elevation Required: False
- Dependency Executor: sh
- Source Path: atomics/T1562.008/T1562.008.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.008]]

## Input Arguments

### aws_region

- description: AWS region to detonate
- type: string
- default: us-west-2

### stratus_path

- description: Path of stratus binary
- type: path
- default: $PathToAtomicsFolder/T1562.008/src

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
then DOWNLOAD_URL=$(curl -s https://api.github.com/repos/DataDog/stratus-red-team/releases/latest | grep browser_download_url | grep linux_x86_64 | cut -d '"' -f 4) 
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
./stratus warmup aws.defense-evasion.cloudtrail-lifecycle-rule
echo "starting detonate"
./stratus detonate aws.defense-evasion.cloudtrail-lifecycle-rule --force
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

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.008/T1562.008.yaml)
