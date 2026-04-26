---
sigma_id: "76737c19-66ee-4c07-b65a-a03301d1573d"
title: "GCP Break-glass Container Workload Deployed"
framework: "sigma"
generated: "true"
source_path: "rules/cloud/gcp/audit/gcp_breakglass_container_workload_deployed.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/gcp/audit/gcp_breakglass_container_workload_deployed.yml"
build_date: "2026-04-26 14:14:25"
status: "test"
level: "medium"
logsource: "gcp / gcp.audit"
aliases:
  - "76737c19-66ee-4c07-b65a-a03301d1573d"
  - "GCP Break-glass Container Workload Deployed"
attack_technique_ids:
  - "T1548"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# GCP Break-glass Container Workload Deployed

Detects the deployment of workloads that are deployed by using the break-glass flag to override Binary Authorization controls.

## Metadata

- Rule ID: 76737c19-66ee-4c07-b65a-a03301d1573d
- Status: test
- Level: medium
- Author: Bryan Lim
- Date: 2024-01-12
- Source Path: rules/cloud/gcp/audit/gcp_breakglass_container_workload_deployed.yml

## Logsource

- product: gcp
- service: gcp.audit

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548]]

## Detection

```yaml
selection:
  data.protoPayload.resource.type: k8s_cluster
  data.protoPayload.logName:
  - cloudaudit.googleapis.com/activity
  - cloudaudit.googleapis.com%2Factivity
  data.protoPayload.methodName: io.k8s.core.v1.pods.create
keywords:
- image-policy.k8s.io/break-glass
condition: selection and keywords
```

## False Positives

- Unknown

## References

- https://cloud.google.com/binary-authorization

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/cloud/gcp/audit/gcp_breakglass_container_workload_deployed.yml)
