---
mitre_id: "DC0072"
mitre_name: "Container Creation"
mitre_type: "x-mitre-data-component"
mitre_stix_id: "x-mitre-data-component--a5ae90ca-0c4b-481c-959f-0eb18a7ff953"
mitre_created: "2021-10-20T15:05:19.274Z"
mitre_modified: "2025-11-12T22:03:39.105Z"
mitre_version: "2.0"
mitre_domains:
  - "enterprise-attack"
framework: "attack"
generated: "true"
build_date: "2026-04-23 22:40:56"
build_source: "script"
object_type: "data-component"
tags:
  - "attack"
  - "data-component"
  - "detection"
  - "telemetry"
---

# DC0072: Container Creation

"Container Creation" data component captures details about the initial construction of a container in a containerized environment. This includes events where a new container is instantiated, such as through Docker, Kubernetes, or other container orchestration platforms. Monitoring these events helps detect unauthorized or potentially malicious container creation. Examples:

- Docker Example: `docker create my-container`, `docker run --name=my-container nginx:latest`
- Kubernetes Example: `kubectl run my-pod --image=nginx`, `kubectl create deployment my-deployment --image=nginx`
- Cloud Container Services Example
    - AWS ECS: Task or service creation (`RunTask` or `CreateService`).
    - Azure Container Instances: Deployment of a container group.
    - Google Kubernetes Engine (GKE): Creation of new pods via GCP APIs.

## Workspace

- [[kb/notes/attack/data-components/dc0072-notes|Open workspace note]]

