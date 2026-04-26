---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-SYSDM"
d3fend_name: "System Dependency Mapping"
d3fend_ontology_id: "d3f:SystemDependencyMapping"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3ASystemDependencyMapping/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

---

System dependency mapping identifies and models the dependencies of system components on each other to carry out their function.

## Workspace

- [[workspaces/defend/techniques/D3-SYSDM-system_dependency_mapping-note|Open workspace note]]

![[workspaces/defend/techniques/D3-SYSDM-system_dependency_mapping-note]]

## Parent Technique

- [[D3-SYSM-system_mapping|D3-SYSM: System Mapping]]

## Knowledge Base Article

## How it works
The organization collects and models architectural information about the software, hardware, and products and maps the dependencies between systems, including each system's internal components and dependencies.

## Considerations
* Data exchanges identified in the network mapping efforts usually indicate such dependencies, but may not be part of the intended design.
* Architectural design artifacts and SMEs may need to be consulted to determine if dependencies are intended or otherwise essential.
* System depedency mapping can identify internal dependencies of standard and pre-built systems that should be incorporated into a complete system dependency model.
* System dependencies for critical systems--those supporting critical organizational activities--should be prioritized for supply chain risk analysis.
* System dependencies should identify the integral components of a given named system and their structure to form a system.
* System dependencies with a given system may be fixed by a particular product's configuration, and leveraging external knowledge bases about dependencies available (e.g., from package managers) is essential.

## Ontology Relationships

- [[D3-SYSM-system_mapping|D3-SYSM: System Mapping]]

