---
mitre_id: "DC0069"
mitre_name: "Cloud Service Modification"
mitre_type: "x-mitre-data-component"
mitre_stix_id: "x-mitre-data-component--e52d89f9-1710-4708-88a5-cbef77c4cd5e"
mitre_created: "2021-10-20T15:05:19.274Z"
mitre_modified: "2025-11-12T22:03:39.105Z"
mitre_version: "2.0"
mitre_domains:
  - "enterprise-attack"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "data-component"
tags:
  - "attack"
  - "data-component"
  - "detection"
  - "telemetry"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Cloud service modification refers to changes made to the configuration, settings, or data of a cloud service. These modifications can include administrative changes such as enabling or disabling features, altering permissions, or deleting critical components. Monitoring these changes is critical to detect potential misconfigurations or malicious activity. Examples: 

- AWS Cloud Service Modifications: A user disables AWS CloudTrail logging (StopLogging) or deletes a CloudWatch configuration rule (DeleteConfigRule).
- Azure Cloud Service Modifications: Changes to Azure Role-Based Access Control (RBAC) roles, such as adding a new Contributor role to a sensitive resource.
- Google Cloud Service Modifications: Deletion of a Google Cloud Storage bucket or disabling a Google Cloud Function.
- Office 365 Cloud Service Modifications: Altering mailbox permissions or disabling auditing in Microsoft 365.

## Workspace

- [[workspaces/attack/data-components/DC0069-cloud_service_modification-note|Open workspace note]]

![[workspaces/attack/data-components/DC0069-cloud_service_modification-note]]

