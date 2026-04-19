---
id: T1525
name: Implant Internal Image
created: 2019-09-04 12:04:03.552000+00:00
modified: 2025-10-24 17:48:45.786000+00:00
type: attack-pattern
x_mitre_version: 2.2
x_mitre_domains: enterprise-attack
---

## Tactic

- [[persistence|Persistence]]

Adversaries may implant cloud or container images with malicious code to establish persistence after gaining access to an environment. Amazon Web Services (AWS) Amazon Machine Images (AMIs), Google Cloud Platform (GCP) Images, and Azure Images as well as popular container runtimes such as Docker can be implanted or backdoored. Unlike [Upload Malware](https://attack.mitre.org/techniques/T1608/001), this technique focuses on adversaries implanting an image in a registry within a victim’s environment. Depending on how the infrastructure is provisioned, this could provide persistent access if the infrastructure provisioning tool is instructed to always use the latest image.(Citation: Rhino Labs Cloud Image Backdoor Technique Sept 2019)

A tool has been developed to facilitate planting backdoors in cloud container images.(Citation: Rhino Labs Cloud Backdoor September 2019) If an adversary has access to a compromised AWS instance, and permissions to list the available container images, they may implant a backdoor such as a [Web Shell](https://attack.mitre.org/techniques/T1505/003).(Citation: Rhino Labs Cloud Image Backdoor Technique Sept 2019)

## Mitigations

- [[M1026-privileged_account_management|M1026: Privileged Account Management]]
- [[M1045-code_signing|M1045: Code Signing]]
- [[M1047-audit|M1047: Audit]]

## Platforms

- IaaS
- Containers

