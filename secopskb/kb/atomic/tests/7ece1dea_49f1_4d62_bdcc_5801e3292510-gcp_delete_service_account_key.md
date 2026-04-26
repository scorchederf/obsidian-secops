---
atomic_guid: "7ece1dea-49f1-4d62-bdcc-5801e3292510"
title: "GCP - Delete Service Account Key"
framework: "atomic"
generated: "true"
attack_technique_id: "T1098"
attack_technique_name: "Account Manipulation"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1098/T1098.yaml"
build_date: "2026-04-26 14:38:39"
executor: "sh"
aliases:
  - "7ece1dea-49f1-4d62-bdcc-5801e3292510"
  - "GCP - Delete Service Account Key"
platforms:
  - "iaas:gcp"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# GCP - Delete Service Account Key

This Atomic will: 
  - Create a service account
  - Create a service account key, 
  - Store the result of retrieving a single key for that service account as a variable
  - Pass that variable for deletion
  - Delete the service account

The idea for this Atomic came from a Rule published by the Elastic team.

Identifies the deletion of an Identity and Access Management (IAM) service account key in Google Cloud Platform (GCP).
Each service account is associated with two sets of public/private RSA key pairs that are used to authenticate. 
If a key is deleted, the application will no longer be able to access Google Cloud resources using that key. A security best practice is to rotate your service account keys regularly.

Reference: https://github.com/elastic/detection-rules/blob/main/rules/integrations/gcp/impact_gcp_storage_bucket_deleted.toml

## Metadata

- Atomic GUID: 7ece1dea-49f1-4d62-bdcc-5801e3292510
- Technique: T1098: Account Manipulation
- Platforms: iaas:gcp
- Executor: sh
- Elevation Required: False
- Dependency Executor: sh
- Source Path: atomics/T1098/T1098.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1098-account_manipulation|T1098]]

## Input Arguments

### project_id

- description: ID of the GCP Project you to execute the command against.
- type: string
- default: atomic-test-1

### service_name

- description: The name of the service account.
- type: string
- default: atomic-service-account

## Dependencies

Requires gcloud

### Prerequisite Check

```text
if [ -x "$(command -v gcloud)" ]; then exit 0; else exit 1; fi;
```

### Get Prerequisite

```text
echo "Please Install Google Cloud SDK before running this atomic test : https://cloud.google.com/sdk/docs/install"
```

Check if user is logged in

### Prerequisite Check

```text
gcloud config get-value account
```

### Get Prerequisite

```text
gcloud auth login --no-launch-browser
```

Check if terraform is installed.

### Prerequisite Check

```text
terraform version
```

### Get Prerequisite

```text
echo Please install the terraform.
```

Create dependency resources using terraform

### Prerequisite Check

```text
stat "$PathToAtomicsFolder/T1098/src/T1098-17/terraform.tfstate"
```

### Get Prerequisite

```text
cd "$PathToAtomicsFolder/T1098/src/T1098-17/"
terraform init
terraform apply -auto-approve
```

## Executor

- elevation_required: False
- name: sh

### Command

```sh
gcloud config set project #{project_id}
KEY=`gcloud iam service-accounts keys list --iam-account=#{service_name}@#{project_id}.iam.gserviceaccount.com --format="value(KEY_ID)" --limit=1`
gcloud iam service-accounts keys delete $KEY --iam-account=#{service_name}@#{project_id}.iam.gserviceaccount.com --quiet
```

### Cleanup

```sh
cd "$PathToAtomicsFolder/T1098/src/T1098-17/"
terraform state rm google_service_account_key.key
terraform destroy -auto-approve
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1098/T1098.yaml)
