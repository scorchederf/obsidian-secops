---
atomic_guid: "89e69b4b-3458-4ec6-b819-b3008debc1bc"
title: "Azure - Create Snapshot from Managed Disk"
framework: "atomic"
generated: "true"
attack_technique_id: "T1578.001"
attack_technique_name: "Modify Cloud Compute Infrastructure: Create Snapshot"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1578.001/T1578.001.yaml"
build_date: "2026-04-26 14:38:40"
executor: "sh"
aliases:
  - "89e69b4b-3458-4ec6-b819-b3008debc1bc"
  - "Azure - Create Snapshot from Managed Disk"
platforms:
  - "iaas:azure"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Azure - Create Snapshot from Managed Disk

Creates a snapshot of a managed disk in Azure using the Azure CLI.
Simulates adversary snapshotting behavior for persistence or data duplication.

## Metadata

- Atomic GUID: 89e69b4b-3458-4ec6-b819-b3008debc1bc
- Technique: T1578.001: Modify Cloud Compute Infrastructure: Create Snapshot
- Platforms: iaas:azure
- Executor: sh
- Elevation Required: False
- Source Path: atomics/T1578.001/T1578.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1578-modify_cloud_compute_infrastructure|T1578.001]]

## Input Arguments

### azure_disk_name

- description: The Azure disk name.
- type: string
- default: myDiskName

### azure_resource_group

- description: The Azure resource group where the disk is located.
- type: string
- default: myResourceGroup

### azure_snapshot_name

- description: The Azure snapshot name.
- type: string
- default: mySnapshotName

## Dependencies

Azure CLI must be installed.

### Prerequisite Check

```text
if command -v az > /dev/null 2>&1; then exit 0; else exit 1; fi
```

### Get Prerequisite

```text
echo "Install Azure CLI: https://learn.microsoft.com/en-us/cli/azure/install-azure-cli"
```

Azure CLI must be authenticated.

### Prerequisite Check

```text
if az account show > /dev/null 2>&1; then exit 0; else exit 1; fi
```

### Get Prerequisite

```text
echo "Login with: az login"
```

Azure disk must exist.

### Prerequisite Check

```text
if az disk show --resource-group #{azure_resource_group} --name #{azure_disk_name} > /dev/null 2>&1; then exit 0; else exit 1; fi
```

### Get Prerequisite

```text
echo "Ensure the disk exists in the given resource group."
```

## Executor

- elevation_required: False
- name: sh

### Command

```sh
az snapshot create --resource-group #{azure_resource_group} --name #{azure_snapshot_name} --source #{azure_disk_name} --location eastus
```

### Cleanup

```sh
az snapshot delete --resource-group #{azure_resource_group} --name #{azure_snapshot_name}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1578.001/T1578.001.yaml)
