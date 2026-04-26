---
sigma_id: "6ad91e31-53df-4826-bd27-0166171c8040"
title: "Google Cloud Kubernetes Admission Controller"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/gcp/audit/gcp_kubernetes_admission_controller.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/gcp/audit/gcp_kubernetes_admission_controller.yml"
build_date: "2026-04-26 14:14:26"
status: "test"
level: "medium"
logsource: "gcp / gcp.audit"
aliases:
  - "6ad91e31-53df-4826-bd27-0166171c8040"
  - "Google Cloud Kubernetes Admission Controller"
attack_technique_ids:
  - "T1078"
  - "T1552"
  - "T1552.007"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Google Cloud Kubernetes Admission Controller

Identifies when an admission controller is executed in GCP Kubernetes.
A Kubernetes Admission controller intercepts, and possibly modifies, requests to the Kubernetes API server.
The behavior of this admission controller is determined by an admission webhook (MutatingAdmissionWebhook or ValidatingAdmissionWebhook) that the user deploys in the cluster.
An adversary can use such webhooks as the MutatingAdmissionWebhook for obtaining persistence in the cluster.
For example, attackers can intercept and modify the pod creation operations in the cluster and add their malicious container to every created pod. An adversary can use the webhook ValidatingAdmissionWebhook, which could be used to obtain access credentials.
An adversary could use the webhook to intercept the requests to the API server, record secrets, and other sensitive information.

## Metadata

- Rule ID: 6ad91e31-53df-4826-bd27-0166171c8040
- Status: test
- Level: medium
- Author: Austin Songer @austinsonger
- Date: 2021-11-25
- Modified: 2022-12-18
- Source Path: rules/cloud/gcp/audit/gcp_kubernetes_admission_controller.yml

## Logsource

- product: gcp
- service: gcp.audit

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078]]
- [[kb/attack/techniques/T1552-unsecured_credentials|T1552]]
- [[kb/attack/techniques/T1552-unsecured_credentials|T1552.007]]

## Detection

```yaml
selection:
  gcp.audit.method_name|startswith: admissionregistration.k8s.io.v
  gcp.audit.method_name|contains:
  - .mutatingwebhookconfigurations.
  - .validatingwebhookconfigurations.
  gcp.audit.method_name|endswith:
  - create
  - patch
  - replace
condition: selection
```

## False Positives

- Google Cloud Kubernetes Admission Controller may be done by a system administrator.
- If known behavior is causing false positives, it can be exempted from the rule.

## References

- https://cloud.google.com/kubernetes-engine/docs

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/gcp/audit/gcp_kubernetes_admission_controller.yml)
