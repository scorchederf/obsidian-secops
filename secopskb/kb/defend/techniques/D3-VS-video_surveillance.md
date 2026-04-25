---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-VS"
d3fend_name: "Video Surveillance"
d3fend_ontology_id: "d3f:VideoSurveillance"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AVideoSurveillance/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-25 14:47:22"
build_source: "script"
attack_technique_ids:
  - "T1125"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[notes/index|Notes]]

---

Monitoring of physical areas via camera video feeds to deter, detect, and investigate unauthorized access and related security events.

## Workspace

- [[notes/defend/techniques/D3-VS-video_surveillance-note|Open workspace note]]

![[notes/defend/techniques/D3-VS-video_surveillance-note]]

## Parent Technique

- [[D3-PHAM-physical_access_monitoring|D3-PHAM: Physical Access Monitoring]]

## Related ATT&CK Techniques

- [[T1125-video_capture|T1125: Video Capture]]

## Knowledge Base Article

## How it works

Video surveillance uses digital cameras that stream to a video management system (VMS) or network video recorder (NVR) for live monitoring, recording, and retrieval. Recording can be continuous or event-driven using analytics (motion in regions of interest, line crossing) or external triggers (access denials, sensor alarms). Time synchronization aligns video with other logs, while health monitoring detects camera outages and tamper. Secure export workflows preserve integrity for investigations.

## Considerations

* Plan camera placement and coverage to avoid occlusions and handle challenging lighting; select lenses and mounting to capture entry points and critical areas.
* Size storage and bandwidth for the intended retention period by choosing appropriate resolution, frame rate, and compression, and monitor capacity over time.
* Secure cameras and management systems with unique credentials, timely firmware updates, encrypted transport, and network segmentation to limit exposure.
* Address privacy and legal obligations with visible notice, role-based access to footage, and retention policies aligned with regulations and organizational policy.
* Monitor system health and build resilience with tamper and heartbeat alerts, recorder failover where needed, and accurate time synchronization for correlation.

## Ontology Relationships

- [[D3-PHAM-physical_access_monitoring|D3-PHAM: Physical Access Monitoring]]

