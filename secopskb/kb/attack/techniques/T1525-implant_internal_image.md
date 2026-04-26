---
mitre_id: "T1525"
mitre_name: "Implant Internal Image"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--4fd8a28b-4b3a-4cd6-a8cf-85ba5f824a7f"
mitre_created: "2019-09-04T12:04:03.552Z"
mitre_modified: "2025-10-24T17:48:45.786Z"
mitre_version: "2.2"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1525/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "IaaS"
  - "Containers"
mitre_tactic_ids:
  - "TA0003"
d3fend_ids:
  - "D3-CIA"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

---

Adversaries may implant cloud or container images with malicious code to establish persistence after gaining access to an environment. Amazon Web Services (AWS) Amazon Machine Images (AMIs), Google Cloud Platform (GCP) Images, and Azure Images as well as popular container runtimes such as Docker can be implanted or backdoored. Unlike [[T1608-stage_capabilities#^t1608001-upload-malware|T1608.001: Upload Malware]], this technique focuses on adversaries implanting an image in a registry within a victim’s environment. Depending on how the infrastructure is provisioned, this could provide persistent access if the infrastructure provisioning tool is instructed to always use the latest image.(Citation: Rhino Labs Cloud Image Backdoor Technique Sept 2019)

A tool has been developed to facilitate planting backdoors in cloud container images.(Citation: Rhino Labs Cloud Backdoor September 2019) If an adversary has access to a compromised AWS instance, and permissions to list the available container images, they may implant a backdoor such as a [[T1505-server_software_component#^t1505003-web-shell|T1505.003: Web Shell]].(Citation: Rhino Labs Cloud Image Backdoor Technique Sept 2019)

## Workspace

- [[workspaces/attack/techniques/T1525-implant_internal_image-note|Open workspace note]]

![[workspaces/attack/techniques/T1525-implant_internal_image-note]]

## Tactics

- [[TA0003-persistence|TA0003: Persistence]]

## D3FEND

- [[D3-CIA-container_image_analysis|D3-CIA: Container Image Analysis]]

## Mitigations

- [[M1026-privileged_account_management|M1026: Privileged Account Management]]
- [[M1045-code_signing|M1045: Code Signing]]
- [[M1047-audit|M1047: Audit]]

## Platforms

- IaaS
- Containers

