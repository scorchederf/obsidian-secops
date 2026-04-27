---
mitre_id: "DC0077"
mitre_name: "Container Start"
mitre_type: "x-mitre-data-component"
mitre_stix_id: "x-mitre-data-component--5fe82895-28e5-4aac-845e-dc886b63be2e"
mitre_created: "2021-10-20T15:05:19.274Z"
mitre_modified: "2025-10-21T15:14:37.615Z"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

"Container Start" data component captures events related to the activation or invocation of a container within a containerized environment. This includes starting a previously stopped container, restarting an existing container, or initializing a container for runtime. Monitoring these activities is critical for identifying unauthorized or unexpected container activations, which may indicate potential adversarial activity or misconfigurations. Examples: 

- Docker Example: `docker start <container_name>`, `docker restart <container_name>`
- Kubernetes Example: Kubernetes automatically restarts containers as part of pod lifecycle management (e.g., due to health checks or configuration changes).
- Cloud-Native Example
    - AWS ECS: API Call: StartTask to activate a stopped ECS task.
    - Azure Container Instances: Command to restart a container group instance.
    - GCP Kubernetes Engine: Automatic restarts as part of node or pod management.

This data component can be collected through the following measures:

- Docker Audit Logging: Enable Docker logging to capture start and restart events. Use tools like auditd to monitor terminal activity involving container lifecycle commands.
- Kubernetes Audit Logs: Enable Kubernetes API server audit logging.
- Cloud Provider Logs
    - AWS CloudTrail: Capture StartTask or related API calls for ECS.
    - Azure Monitor: Track activity in container groups that indicate start or restart events.
    - GCP Cloud Logging: Record logs related to pod restarts or scaling events in Kubernetes Engine.
- SIEM Integration: Collect logs from Docker, Kubernetes, and cloud services to correlate container start events.

## Workspace

- [[workspaces/attack/data-components/DC0077-container_start-note|Open workspace note]]

![[workspaces/attack/data-components/DC0077-container_start-note]]

