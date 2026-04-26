---
mitre_id: "S0683"
mitre_name: "Peirates"
mitre_type: "tool"
mitre_stix_id: "tool--79dd477a-8226-4b3d-ad15-28623675f221"
mitre_created: "2022-02-08T16:11:38.528Z"
mitre_modified: "2025-04-16T20:38:52.924Z"
mitre_version: "1.0"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/software/S0683/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "tool"
tags:
  - "attack"
  - "tool"
  - "offense"
mitre_aliases:
  - "Peirates"
aliases:
  - "S0683"
  - "Peirates"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

---

[Peirates](https://attack.mitre.org/software/S0683) is a post-exploitation Kubernetes exploitation framework with a focus on gathering service account tokens for lateral movement and privilege escalation. The tool is written in GoLang and publicly available on GitHub.(Citation: Peirates GitHub)

## Workspace

- [[workspaces/tools/S0683-peirates-note|Open workspace note]]

![[workspaces/tools/S0683-peirates-note]]

## Uses Techniques

- [[T1046-network_service_discovery|T1046: Network Service Discovery]]
- [[T1078-valid_accounts|T1078: Valid Accounts]]
    - [[T1078-valid_accounts#^t1078004-cloud-accounts|T1078.004: Cloud Accounts]]
- [[T1528-steal_application_access_token|T1528: Steal Application Access Token]]
- [[T1530-data_from_cloud_storage|T1530: Data from Cloud Storage]]
- [[T1550-use_alternate_authentication_material|T1550: Use Alternate Authentication Material]]
    - [[T1550-use_alternate_authentication_material#^t1550001-application-access-token|T1550.001: Application Access Token]]
- [[T1552-unsecured_credentials|T1552: Unsecured Credentials]]
    - [[T1552-unsecured_credentials#^t1552005-cloud-instance-metadata-api|T1552.005: Cloud Instance Metadata API]]
    - [[T1552-unsecured_credentials#^t1552007-container-api|T1552.007: Container API]]
- [[T1609-container_administration_command|T1609: Container Administration Command]]
- [[T1610-deploy_container|T1610: Deploy Container]]
- [[T1611-escape_to_host|T1611: Escape to Host]]
- [[T1613-container_and_resource_discovery|T1613: Container and Resource Discovery]]
- [[T1619-cloud_storage_object_discovery|T1619: Cloud Storage Object Discovery]]

