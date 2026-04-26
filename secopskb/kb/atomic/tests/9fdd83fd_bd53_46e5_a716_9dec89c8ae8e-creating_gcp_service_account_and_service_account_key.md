---
atomic_guid: "9fdd83fd-bd53-46e5-a716-9dec89c8ae8e"
title: "Creating GCP Service Account and Service Account Key"
framework: "atomic"
generated: "true"
attack_technique_id: "T1078.004"
attack_technique_name: "Valid Accounts: Cloud Accounts"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1078.004/T1078.004.yaml"
build_date: "2026-04-26 17:02:12"
executor: "sh"
aliases:
  - "9fdd83fd-bd53-46e5-a716-9dec89c8ae8e"
  - "Creating GCP Service Account and Service Account Key"
platforms:
  - "google-workspace"
  - "iaas:gcp"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Creating GCP Service Account and Service Account Key

GCP Service Accounts can be used to gain intial access as well as maintain persistence inside Google Cloud.

## Metadata

- Atomic GUID: 9fdd83fd-bd53-46e5-a716-9dec89c8ae8e
- Technique: T1078.004: Valid Accounts: Cloud Accounts
- Platforms: google-workspace, iaas:gcp
- Executor: sh
- Elevation Required: False
- Dependency Executor: sh
- Source Path: atomics/T1078.004/T1078.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1078-valid_accounts|T1078.004]]

## Input Arguments

### output-key-file

- description: Email of the service account
- type: string
- default: gcp-art-service-account-1.json

### project-id

- description: ID of the project, you want to create service account as well as service account key for
- type: string
- default: art-project-1

### service-account-email

- description: Email of the service account
- type: string
- default: gcp-art-service-account-1@art-project-1.iam.gserviceaccount.com

### service-account-name

- description: Name of the service account
- type: string
- default: gcp-art-service-account-1

## Dependencies

Requires gcloud

### Prerequisite Check

```bash
if [ -x "$(command -v gcloud)" ]; then exit 0; else exit 1; fi;
```

### Get Prerequisite

```bash
echo "Please Install Google Cloud SDK before running this atomic test : https://cloud.google.com/sdk/docs/install"
```

Check if user is logged in

### Prerequisite Check

```bash
gcloud config get-value account
```

### Get Prerequisite

```bash
gcloud auth login --no-launch-browser
```

## Executor

- elevation_required: False
- name: sh

### Command

```bash
gcloud config set project #{project-id}
gcloud iam service-accounts create #{service-account-name}
gcloud iam service-accounts keys create #{output-key-file} --iam-account=#{service-account-email}
```

### Cleanup

```bash
gcloud iam service-accounts delete #{service-account-email} --quiet
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1078.004/T1078.004.yaml)
