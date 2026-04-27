---
atomic_guid: "979356b9-b588-4e49-bba4-c35517c484f5"
title: "AWS - Scan for Anonymous Access to S3"
framework: "atomic"
generated: "true"
attack_technique_id: "T1530"
attack_technique_name: "Data from Cloud Storage Object"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1530/T1530.yaml"
build_date: "2026-04-27 19:12:27"
executor: "sh"
aliases:
  - "979356b9-b588-4e49-bba4-c35517c484f5"
  - "AWS - Scan for Anonymous Access to S3"
platforms:
  - "iaas:aws"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Upon successful execution, this test will test for anonymous access to AWS S3 buckets and dumps all the files to a local folder.

## ATT&CK Mapping

- [[kb/attack/techniques/T1530-data_from_cloud_storage|T1530: Data from Cloud Storage]]

## Input Arguments

### s3_bucket_name

- description: Name of the bucket
- type: string
- default: redatomic-test2

## Dependencies

Check if ~/.aws/credentials file has a default stanza is configured

### Prerequisite Check

```untitled
cat ~/.aws/credentials | grep "default"
aws s3api create-bucket --bucket #{s3_bucket_name}
aws s3api put-bucket-policy --bucket #{s3_bucket_name} --policy file://$PathToAtomicsFolder/T1530/src/policy.json
touch /tmp/T1530.txt
aws s3 cp /tmp/T1530.txt s3://#{s3_bucket_name}
```

### Get Prerequisite

```untitled
echo Please install the aws-cli and configure your AWS default profile using: aws configure
```

## Executor

- elevation_required: False
- name: sh

### Command

```bash
aws --no-sign-request s3 cp --recursive s3://#{s3_bucket_name} /tmp/#{s3_bucket_name}
```

### Cleanup

```bash
aws s3 rb s3://#{s3_bucket_name} --force 
rm -rf /tmp/#{s3_bucket_name}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1530/T1530.yaml)
