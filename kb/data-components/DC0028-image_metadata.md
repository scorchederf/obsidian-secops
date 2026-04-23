---
mitre_id: "DC0028"
mitre_name: "Image Metadata"
mitre_type: "x-mitre-data-component"
mitre_stix_id: "x-mitre-data-component--b597a220-6510-4397-b0d8-342cd2c58827"
mitre_created: "2021-10-20T15:05:19.272Z"
mitre_modified: "2025-11-12T22:03:39.105Z"
mitre_version: "2.0"
mitre_domains:
  - "enterprise-attack"
build_date: "2026-04-21 20:44:18"
build_source: "script"
---

# DC0028: Image Metadata

contextual information associated with a virtual machine image, such as its name, resource group, status (active or inactive), type (custom or prebuilt), size, creation date, and permissions. This metadata is critical for understanding the state and configuration of virtual machine images in cloud environments. Examples: 

- Azure Compute Service Image Metadata Example:
    - Name: MyCustomImage
    - Resource Group: MyResourceGroup
    - State: Available
    - Type: Managed Image
- AWS EC2 AMI Metadata Example:
    - Image ID: ami-1234567890abcdef0
    - Name: ProdImage
    - State: Available
    - Platform: Windows
- Google Cloud Compute Engine Image Metadata Example:
    - Image Name: webserver-image
    - Project: my-project-id
    - Family: webserver
    - Source Disk: my-disk-id
- VMware vSphere Template Metadata Example:
    - Name: LinuxTemplate
    - Disk Size: 40GB
    - Network Adapter: VM Network

