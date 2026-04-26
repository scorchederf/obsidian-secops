---
atomic_guid: "d56152ec-01d9-42a2-877c-aac1f6ebe8e6"
title: "GCP - Delete Activity Event Log"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.008"
attack_technique_name: "Impair Defenses: Disable Cloud Logs"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.008/T1562.008.yaml"
build_date: "2026-04-26 14:38:40"
executor: "sh"
aliases:
  - "d56152ec-01d9-42a2-877c-aac1f6ebe8e6"
  - "GCP - Delete Activity Event Log"
platforms:
  - "iaas:gcp"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# GCP - Delete Activity Event Log

GCP provides 4 types of Cloud Audit Logs: Admin Activity, Data Access, System Events, and Policy Denied.
An adversary may attempt to delete logs in order to hide their activity. However, Admin Activity, System Events, and Policy Deny events logs cannot be deleted. 

This Atomic attempts to delete the Activity Event log. An event is generated under the method name of `google.logging.v2.LoggingServiceV2.DeleteLog` with a Serverity of `ERROR`.

## Metadata

- Atomic GUID: d56152ec-01d9-42a2-877c-aac1f6ebe8e6
- Technique: T1562.008: Impair Defenses: Disable Cloud Logs
- Platforms: iaas:gcp
- Executor: sh
- Elevation Required: False
- Dependency Executor: sh
- Source Path: atomics/T1562.008/T1562.008.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.008]]

## Input Arguments

### project-id

- description: ID of the GCP Project you to execute the command against.
- type: string
- default: atomic-project-1

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

## Executor

- elevation_required: False
- name: sh

### Command

```sh
gcloud config set project #{project-id}
gcloud logging logs delete projects/#{project-id}/logs/cloudaudit.googleapis.com%2Factivity --quiet
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.008/T1562.008.yaml)
