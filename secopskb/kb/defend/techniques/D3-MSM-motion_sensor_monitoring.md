---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-MSM"
d3fend_name: "Motion Sensor Monitoring"
d3fend_ontology_id: "d3f:MotionSensorMonitoring"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AMotionSensorMonitoring/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Monitoring events from motion detectors (e.g., passive IR, microwave, dual-technology) to detect presence or movement within protected areas.

## Workspace

- [[workspaces/defend/techniques/D3-MSM-motion_sensor_monitoring-note|Open workspace note]]

![[workspaces/defend/techniques/D3-MSM-motion_sensor_monitoring-note]]

## Parent Technique

- [[D3-PHAM-physical_access_monitoring|D3-PHAM: Physical Access Monitoring]]

## Knowledge Base Article

## How it works

Motion sensors generate events when movement is detected within their coverage pattern. Alarm panels or PACS correlate motion with arming schedules, door openings, and other sensors; video systems can use motion to trigger recording or bookmarks. Cross-zoning and sensitivity/pulse-count settings are commonly adjusted to balance detection and false-alarm rates.

## Considerations

* Place sensors at appropriate height and angle with clear line of sight, avoiding obstructions or reflective surfaces that can cause missed or false detections.
* Reduce false alarms by tuning sensitivity and pulse-count, using cross-zoning when needed, and accounting for HVAC airflow or rapid thermal changes.
* Monitor tamper and supervision signals; for wireless devices, verify periodic check-ins and battery levels; perform regular walk tests to validate coverage.
* Integrate motion events with cameras and with door position switches and other sensors in the protected area to provide context and faster verification; use motion to trigger recording or bookmarks.

## Ontology Relationships

- [[D3-PHAM-physical_access_monitoring|D3-PHAM: Physical Access Monitoring]]

