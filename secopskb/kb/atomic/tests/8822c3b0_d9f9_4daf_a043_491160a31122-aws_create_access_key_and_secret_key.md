---
atomic_guid: "8822c3b0-d9f9-4daf-a043-491160a31122"
title: "AWS - Create Access Key and Secret Key"
framework: "atomic"
generated: "true"
attack_technique_id: "T1098.001"
attack_technique_name: "Account Manipulation: Additional Cloud Credentials"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1098.001/T1098.001.yaml"
build_date: "2026-04-27 19:12:27"
executor: "sh"
aliases:
  - "8822c3b0-d9f9-4daf-a043-491160a31122"
  - "AWS - Create Access Key and Secret Key"
platforms:
  - "iaas:aws"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Adversaries create their own new access and secret keys to programatically interact with AWS environment, which is already compromised

## ATT&CK Mapping

- [[kb/attack/techniques/T1098-account_manipulation#^t1098001-additional-cloud-credentials|T1098.001: Additional Cloud Credentials]]

## Input Arguments

### username

- description: Create new AWS access and secret keys for the user
- type: string
- default: atomicredteam

## Dependencies

Check if the user exists.

### Prerequisite Check

```untitled
aws iam list-users | grep #{username}
```

### Get Prerequisite

```untitled
echo Please run atomic test T1136.003, before running this atomic
```

## Executor

- name: sh

### Command

```bash
aws iam create-access-key --user-name #{username} > "$PathToAtomicsFolder/T1098.001/bin/aws_secret.creds"
cd "$PathToAtomicsFolder/T1098.001/bin/"
./aws_secret.sh
```

### Cleanup

```bash
access_key=`cat "$PathToAtomicsFolder/T1098.001/bin/aws_secret.creds" | jq -r '.AccessKey.AccessKeyId'`
aws iam delete-access-key --access-key-id $access_key --user-name #{username}
rm "$PathToAtomicsFolder/T1098.001/bin/aws_secret.creds"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1098.001/T1098.001.yaml)
