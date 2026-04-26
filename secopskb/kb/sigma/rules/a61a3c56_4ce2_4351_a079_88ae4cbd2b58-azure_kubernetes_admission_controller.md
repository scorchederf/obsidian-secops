---
sigma_id: "a61a3c56-4ce2-4351-a079-88ae4cbd2b58"
title: "Azure Kubernetes Admission Controller"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/azure/activity_logs/azure_kubernetes_admission_controller.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_kubernetes_admission_controller.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "azure / activitylogs"
aliases:
  - "a61a3c56-4ce2-4351-a079-88ae4cbd2b58"
  - "Azure Kubernetes Admission Controller"
attack_technique_ids:
  - "T1078"
  - "T1552"
  - "T1552.007"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Azure Kubernetes Admission Controller

Identifies when an admission controller is executed in Azure Kubernetes.
A Kubernetes Admission controller intercepts, and possibly modifies, requests to the Kubernetes API server.
The behavior of this admission controller is determined by an admission webhook (MutatingAdmissionWebhook or ValidatingAdmissionWebhook) that the user deploys in the cluster.
An adversary can use such webhooks as the MutatingAdmissionWebhook for obtaining persistence in the cluster.
For example, attackers can intercept and modify the pod creation operations in the cluster and add their malicious container to every created pod.
An adversary can use the webhook ValidatingAdmissionWebhook, which could be used to obtain access credentials.
An adversary could use the webhook to intercept the requests to the API server, record secrets, and other sensitive information.

## Metadata

- Rule ID: a61a3c56-4ce2-4351-a079-88ae4cbd2b58
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-11-25
- Modified: 2022-12-18
- Source Path: rules/cloud/azure/activity_logs/azure_kubernetes_admission_controller.yml

## Logsource

- product: azure
- service: activitylogs

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078]]
- [[kb/attack/techniques/T1552-unsecured_credentials|T1552]]
- [[kb/attack/techniques/T1552-unsecured_credentials|T1552.007]]

## Detection

```yaml
selection:
  operationName|startswith:
  - MICROSOFT.KUBERNETES/CONNECTEDCLUSTERS/ADMISSIONREGISTRATION.K8S.IO
  - MICROSOFT.CONTAINERSERVICE/MANAGEDCLUSTERS/ADMISSIONREGISTRATION.K8S.IO
  operationName|endswith:
  - /MUTATINGWEBHOOKCONFIGURATIONS/WRITE
  - /VALIDATINGWEBHOOKCONFIGURATIONS/WRITE
condition: selection
```

## False Positives

- Azure Kubernetes Admissions Controller may be done by a system administrator.
- If known behavior is causing false positives, it can be exempted from the rule.

## References

- https://learn.microsoft.com/en-us/azure/role-based-access-control/resource-provider-operations#microsoftkubernetes

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/azure/activity_logs/azure_kubernetes_admission_controller.yml)
