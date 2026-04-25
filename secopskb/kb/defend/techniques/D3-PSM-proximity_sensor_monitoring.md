---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-PSM"
d3fend_name: "Proximity Sensor Monitoring"
d3fend_ontology_id: "d3f:ProximitySensorMonitoring"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AProximitySensorMonitoring/"
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

Monitoring events from proximity sensors that indicate a credential or tagged asset is within the sensor’s read range or a defined zone. Common enabling technologies include RFID, Bluetooth Low Energy (BLE), and Ultra-Wideband (UWB).

## Workspace

- [[notes/defend/techniques/D3-PSM-proximity_sensor_monitoring-note|Open workspace note]]

![[notes/defend/techniques/D3-PSM-proximity_sensor_monitoring-note]]

## Parent Technique

- [[D3-PHAM-physical_access_monitoring|D3-PHAM: Physical Access Monitoring]]

## Knowledge Base Article

## How it works

Proximity readers and sensors detect credentials or tagged assets within their read field, then report presence and, when applicable, authenticate to a controller for access decisions. Systems may use RSSI, dwell time, or time-of-flight to enforce zones and policies such as anti-passback. Secure, authenticated communication between readers and controllers helps prevent cloning and replay attacks.

## Considerations

 * Place readers and align antennas to achieve consistent read ranges; account for materials like metal and liquids that can detune signals.
* Use cryptographic credentials with mutual authentication and encrypted, supervised reader links to mitigate cloning and relay attacks.
* Protect privacy by minimizing collected data, limiting retention, and restricting access to proximity logs.
* Calibrate detection thresholds and zone boundaries; re-test after layout changes or equipment moves.
* Monitor reader and tag health, including battery status for BLE and UWB tags and supervision signals for wired and wireless devices.

## Ontology Relationships

- [[D3-PHAM-physical_access_monitoring|D3-PHAM: Physical Access Monitoring]]

