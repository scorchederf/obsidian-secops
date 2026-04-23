---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-IPCTA"
d3fend_name: "IPC Traffic Analysis"
d3fend_ontology_id: "d3f:IPCTrafficAnalysis"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AIPCTrafficAnalysis/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-23 22:40:56"
build_source: "script"
attack_technique_ids:
  - "T1197"
---

# D3-IPCTA: IPC Traffic Analysis

Analyzing standard inter process communication (IPC) protocols to detect deviations from normal protocol activity.

## Parent Technique

- [[D3-NTA-network_traffic_analysis|D3-NTA: Network Traffic Analysis]]

## Related ATT&CK Techniques

- [[T1197-bits_jobs|T1197: BITS Jobs]]

## Knowledge Base Article

## How it works
Inter process communication enables applications or threads to share data. This can involve one or more computers. Monitoring IPC in your environment can reveal abnormal or malicious activity.
IPC can occur within a single computer or between multiple computers remotely through network protocols. Thus there are multiple ways to collect and monitor these exchanges between processes. A network protocol analyzer may monitor and parse SMB network traffic to record system activity. A host based monitoring agent may monitor IPC activity contained within a single host to look for deviations from standard usages.

### Examples
 * SMB
 * Zeromq
 * Java RMI API

## Considerations
* IPC can generate substantial amounts of data, and it may not be feasible to collect all of it.
* IPC may occur over loopback interfaces or direct memory access granted by the operating system.

## Ontology Relationships

- [[D3-NTA-network_traffic_analysis|D3-NTA: Network Traffic Analysis]]

## Workspace

- [[kb/notes/d3fend/techniques/d3-ipcta-notes|Open workspace note]]

