---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-FC"
d3fend_name: "File Carving"
d3fend_ontology_id: "d3f:FileCarving"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AFileCarving/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
attack_technique_ids:
  - "T1071"
  - "T1071.002"
  - "T1570"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

---

Identifying and extracting files from network application protocols through the use of network stream reassembly software.

## Workspace

- [[workspaces/defend/techniques/D3-FC-file_carving-note|Open workspace note]]

![[workspaces/defend/techniques/D3-FC-file_carving-note]]

## Parent Technique

- [[D3-NTA-network_traffic_analysis|D3-NTA: Network Traffic Analysis]]

## Related ATT&CK Techniques

- [[T1071-application_layer_protocol|T1071: Application Layer Protocol]]
- [[T1071-application_layer_protocol#^t1071002-file-transfer-protocols|T1071.002: File Transfer Protocols]]
- [[T1570-lateral_tool_transfer|T1570: Lateral Tool Transfer]]

## Knowledge Base Article

## How it works
Protocol stream reassembly software recreates a directional byte stream by analyzing captured network packets. Once the stream is reassembled pattern matching is applied to determine if it contains a file of interest. Files of interest range from executable, archive, or document file formats. Once the file is captured, it is then processed with standard File Analysis Techniques. Example network protocols include HTTP, SMTP, FTP, HTTP/2, and TLS/HTTP/Dropbox.

## Considerations
- This is an error prone process due to the intricacies of network protocols and network packet capture.  For example reassembly may be done in real-time or streaming fashion, or packets may be written to disk, then bulk processed.  The packets may arrive out of order, with fragmentation, duplicates, or re-transmissions.  The reassembly software must compensate for the imperfect packet stream in order to recreate the well formed file which was transmitted.
- File type identification can be a difficult process which can be exploited by adversaries.

## Ontology Relationships

- [[D3-NTA-network_traffic_analysis|D3-NTA: Network Traffic Analysis]]

