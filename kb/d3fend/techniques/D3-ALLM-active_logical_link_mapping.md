---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-ALLM"
d3fend_name: "Active Logical Link Mapping"
d3fend_ontology_id: "d3f:ActiveLogicalLinkMapping"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AActiveLogicalLinkMapping/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-23 22:40:56"
build_source: "script"
---

# D3-ALLM: Active Logical Link Mapping

Active logical link mapping sends and receives network traffic as a means to map the whole data link layer, where the links represent logical data flows rather than physical connection

## Parent Technique

- [[D3-LLM-logical_link_mapping|D3-LLM: Logical Link Mapping]]

## Knowledge Base Article

## How it works

Active logical link mapping establishes awareness of logical links in the network by sending data over the network to gather information about logical connections in the network.

Typically this will be achieved through network telemetry coordinated for network management and monitoring and will use a link layer discovery protocol such as LLDP and the information gathered and aggregated a higher levels using an application protocol such as SNMP.  The information may be polled by network management softare or configured once and then pushed from network sensors (or agents.)

Another means of establishing network connectivity is by means of sendingn traffic through the use of a tool such as traceroute, to determine the logical paths through the network architecture.

## Considerations

* Best practice is to encrypte network monitoring data and require authentication for queries or admin/management functions.
* Push notifications reduce bandwidth necessary to capture and maintain information if reliable transport is used.
* Special consideration should be made before using of active scanning in OT networks and OT-safe options chosen where available.

## Ontology Relationships

- [[D3-LLM-logical_link_mapping|D3-LLM: Logical Link Mapping]]

## Workspace

- [[kb/notes/d3fend/techniques/d3-allm-notes|Open workspace note]]

