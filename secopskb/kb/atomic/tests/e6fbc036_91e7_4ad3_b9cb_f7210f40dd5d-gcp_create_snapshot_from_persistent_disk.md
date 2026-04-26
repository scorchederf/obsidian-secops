---
atomic_guid: "e6fbc036-91e7-4ad3-b9cb-f7210f40dd5d"
title: "GCP - Create Snapshot from Persistent Disk"
framework: "atomic"
generated: "true"
attack_technique_id: "T1578.001"
attack_technique_name: "Modify Cloud Compute Infrastructure: Create Snapshot"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1578.001/T1578.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "sh"
aliases:
  - "e6fbc036-91e7-4ad3-b9cb-f7210f40dd5d"
  - "GCP - Create Snapshot from Persistent Disk"
platforms:
  - "iaas:gcp"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# GCP - Create Snapshot from Persistent Disk

Creates a snapshot of a persistent disk in GCP using the gcloud CLI.
Emulates adversary behavior to gain access to volume data or replicate environment state.

## Metadata

- Atomic GUID: e6fbc036-91e7-4ad3-b9cb-f7210f40dd5d
- Technique: T1578.001: Modify Cloud Compute Infrastructure: Create Snapshot
- Platforms: iaas:gcp
- Executor: sh
- Elevation Required: False
- Source Path: atomics/T1578.001/T1578.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1578-modify_cloud_compute_infrastructure|T1578.001]]

## Input Arguments

### gcp_disk_name

- description: The Google Cloud disk name.
- type: string
- default: myDiskName

### gcp_snapshot_name

- description: The Google Cloud snapshot name.
- type: string
- default: mySnapshotName

### gcp_zone

- description: The Google Cloud zone where the disk is located.
- type: string
- default: us-central1-a

## Dependencies

gcloud CLI must be installed.

### Prerequisite Check

```untitled
if command -v gcloud > /dev/null 2>&1; then exit 0; else exit 1; fi
```

### Get Prerequisite

```untitled
echo "Install gcloud CLI: https://cloud.google.com/sdk/docs/install"
```

gcloud CLI must be authenticated.

### Prerequisite Check

```untitled
if gcloud auth list --filter=status:ACTIVE --format="value(account)" | grep . > /dev/null; then exit 0; else exit 1; fi
```

### Get Prerequisite

```untitled
echo "Authenticate with: gcloud auth login"
```

GCP disk must exist.

### Prerequisite Check

```untitled
if gcloud compute disks describe #{gcp_disk_name} --zone=#{gcp_zone} > /dev/null 2>&1; then exit 0; else exit 1; fi
```

### Get Prerequisite

```untitled
echo "Ensure the disk exists in the specified zone."
```

## Executor

- elevation_required: False
- name: sh

### Command

```bash
gcloud compute snapshots create #{gcp_snapshot_name} --source-disk=#{gcp_disk_name} --zone=#{gcp_zone}
```

### Cleanup

```bash
gcloud compute snapshots delete #{gcp_snapshot_name} --quiet
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1578.001/T1578.001.yaml)
