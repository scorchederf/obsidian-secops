---
atomic_guid: "99b38f24-5acc-4aa3-85e5-b7f97a5d37ac"
title: "AWS - EC2 Security Group Enumeration"
framework: "atomic"
generated: "true"
attack_technique_id: "T1580"
attack_technique_name: "Cloud Infrastructure Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1580/T1580.yaml"
build_date: "2026-04-27 19:12:28"
executor: "command_prompt"
aliases:
  - "99b38f24-5acc-4aa3-85e5-b7f97a5d37ac"
  - "AWS - EC2 Security Group Enumeration"
platforms:
  - "iaas:aws"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Simulate an attacker's action to enumerate EC2 Security Groups in a compromised AWS environment.

## ATT&CK Mapping

- [[kb/attack/techniques/T1580-cloud_infrastructure_discovery|T1580: Cloud Infrastructure Discovery]]

## Input Arguments

### aws_profile

- description: AWS CLI profile name
- type: string
- default: default

### output_format

- description: Desired output format (text, table, json)
- type: string
- default: json

## Dependencies

AWS CLI installed and configured with the necessary access rights.

### Prerequisite Check

```untitled
type aws || aws --version
```

### Get Prerequisite

```untitled
if [ "$(uname)" = "Darwin" ] || [ "$(expr substr $(uname) 1 5)" = "Linux" ]; then
  curl "https://aws.amazon.com/cli/" -o "Install-AWSCLI.sh" && sh Install-AWSCLI.sh
elif [ "$(expr substr $(uname) 1 5)" = "MINGW" ]; then
  Invoke-WebRequest -Uri "https://aws.amazon.com/cli/" -OutFile "Install-AWSCLI.ps1"; .\Install-AWSCLI.ps1
fi
```

Check if AWS CLI is installed and configured.

### Prerequisite Check

```untitled
aws sts get-caller-identity --profile #{aws_profile}
```

### Get Prerequisite

```untitled
if ! aws sts get-caller-identity --profile #{aws_profile}; then
  echo "AWS CLI not properly configured. Please configure AWS CLI."
fi
```

## Executor

- name: command_prompt

### Command

```cmd
aws ec2 describe-security-groups --profile #{aws_profile} --output #{output_format}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1580/T1580.yaml)
