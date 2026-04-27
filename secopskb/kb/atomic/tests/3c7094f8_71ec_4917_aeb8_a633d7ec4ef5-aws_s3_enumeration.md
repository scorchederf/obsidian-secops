---
atomic_guid: "3c7094f8-71ec-4917-aeb8-a633d7ec4ef5"
title: "AWS S3 Enumeration"
framework: "atomic"
generated: "true"
attack_technique_id: "T1619"
attack_technique_name: "Cloud Storage Object Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1619/T1619.yaml"
build_date: "2026-04-27 19:12:28"
executor: "sh"
aliases:
  - "3c7094f8-71ec-4917-aeb8-a633d7ec4ef5"
  - "AWS S3 Enumeration"
platforms:
  - "iaas:aws"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This test will enumerate all the S3 buckets in the user account and lists all the files in each bucket.

## ATT&CK Mapping

- [[kb/attack/techniques/T1619-cloud_storage_object_discovery|T1619: Cloud Storage Object Discovery]]

## Dependencies

Check if ~/.aws/credentials file has a default stanza is configured

### Prerequisite Check

```untitled
cat ~/.aws/credentials | grep "default"
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
for bucket in "$(aws s3 ls | cut -d " " -f3)"; do aws s3api list-objects-v2 --bucket $bucket --output text; done
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1619/T1619.yaml)
