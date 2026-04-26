---
atomic_guid: "9c10dc6b-20bd-403a-8e67-50ef7d07ed4e"
title: "AWS - CloudTrail Changes"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.008"
attack_technique_name: "Impair Defenses: Disable Cloud Logs"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.008/T1562.008.yaml"
build_date: "2026-04-26 14:38:40"
executor: "sh"
aliases:
  - "9c10dc6b-20bd-403a-8e67-50ef7d07ed4e"
  - "AWS - CloudTrail Changes"
platforms:
  - "iaas:aws"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# AWS - CloudTrail Changes

Creates a new cloudTrail in AWS, Upon successful creation it will Update,Stop and Delete the cloudTrail

## Metadata

- Atomic GUID: 9c10dc6b-20bd-403a-8e67-50ef7d07ed4e
- Technique: T1562.008: Impair Defenses: Disable Cloud Logs
- Platforms: iaas:aws
- Executor: sh
- Elevation Required: False
- Source Path: atomics/T1562.008/T1562.008.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.008]]

## Input Arguments

### cloudtrail_name

- description: Name of the cloudTrail
- type: string
- default: redatomictesttrail

### region

- description: Name of the region
- type: string
- default: us-east-1

### s3_bucket_name

- description: Name of the bucket
- type: string
- default: redatomic-test

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
echo Please install the terraform and configure your aws default profile
```

Check if the dependency resources are already present.

### Prerequisite Check

```text
if [ -f "$PathToAtomicsFolder/T1562.008/src/T1562.008-1/terraform.tfstate" ]; then exit 0; else exit 1; fi;
```

### Get Prerequisite

```text
cd "$PathToAtomicsFolder/T1562.008/src/T1562.008-1/"
terraform init
terraform apply -auto-approve
```

## Executor

- elevation_required: False
- name: sh

### Command

```sh
aws cloudtrail update-trail --name #{cloudtrail_name} --s3-bucket-name #{s3_bucket_name}  --is-multi-region-trail --region #{region}
aws cloudtrail stop-logging --name #{cloudtrail_name} --region #{region}
aws cloudtrail delete-trail --name #{cloudtrail_name} --region #{region}
```

### Cleanup

```sh
cd "$PathToAtomicsFolder/T1562.008/src/T1562.008-1/"
terraform destroy -auto-approve
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.008/T1562.008.yaml)
