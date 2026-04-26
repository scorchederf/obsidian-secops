---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-CIA"
d3fend_name: "Container Image Analysis"
d3fend_ontology_id: "d3f:ContainerImageAnalysis"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AContainerImageAnalysis/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
attack_technique_ids:
  - "T1525"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

---

Analyzing a Container Image with respect to a set of policies.

## Workspace

- [[workspaces/defend/techniques/D3-CIA-container_image_analysis-note|Open workspace note]]

![[workspaces/defend/techniques/D3-CIA-container_image_analysis-note]]

## Parent Technique

- [[D3-AVE-asset_vulnerability_enumeration|D3-AVE: Asset Vulnerability Enumeration]]

## Related ATT&CK Techniques

- [[T1525-implant_internal_image|T1525: Implant Internal Image]]

## Knowledge Base Article

## How it works

Container images are standalone collections of the executable code and
content that are used to populate a container environment.
They are usually created by either building a container from scratch or by
building on top of an existing image pulled from a repository.

Throughout the container build workflow,
images should be scanned to identify:

- outdated libraries,
- known vulnerabilities,
- or misconfigurations, such as insecure ports or permissions.

Scanning should also provide the flexibility to disregard false positives
for vulnerability detection where knowledgeable
cybersecurity professionals have deemed alerts to be inaccurate.

One approach to implementing image scanning is to use an admission controller
to block deployments if the image does not comply with the organization's
security policies.

An admission controller is a Container Orchestration feature that can intercept and
process requests to the Container Orchestration API prior to persistence of the object,
but after the request is authenticated and authorized.
A webhook can be implemented to scan any image before it is deployed in the orchestrator.
This admission controller

## Considerations

* Image scanning is key to ensuring deployed containers are secure.
* Using trusted repositories to build containers is a critical part of the container build workflow.
* This technique does not necessarly prevent the build process to add insecure or unsecured
  files to the Image.


## Ontology Relationships

- [[D3-AVE-asset_vulnerability_enumeration|D3-AVE: Asset Vulnerability Enumeration]]

