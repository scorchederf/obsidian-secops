---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-SVCDM"
d3fend_name: "Service Dependency Mapping"
d3fend_ontology_id: "d3f:ServiceDependencyMapping"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AServiceDependencyMapping/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-25 14:47:22"
build_source: "script"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[notes/index|Notes]]

---

Service dependency mapping determines the services on which each given service relies.

## Workspace

- [[notes/defend/techniques/D3-SVCDM-service_dependency_mapping-note|Open workspace note]]

![[notes/defend/techniques/D3-SVCDM-service_dependency_mapping-note]]

## Parent Technique

- [[D3-SYSM-system_mapping|D3-SYSM: System Mapping]]

## Knowledge Base Article

## How it works
The organization collects and models architectural information about the services and consumers of services and maps the dependencies between the services.

## Considerations
* Architectural design artifacts and SMEs may need to be consulted to determine if dependencies are intended or otherwise essential.
* Service dependencies for critical systems--those supporting critical organizational activities--should be prioritized for supply chain risk analysis.
* Service dependencies in cloud or microservice architectures may be discovered using distributed tracing capabilities

## Ontology Relationships

- [[D3-SYSM-system_mapping|D3-SYSM: System Mapping]]

