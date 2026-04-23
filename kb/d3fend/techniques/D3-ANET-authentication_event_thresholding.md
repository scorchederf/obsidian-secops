---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-ANET"
d3fend_name: "Authentication Event Thresholding"
d3fend_ontology_id: "d3f:AuthenticationEventThresholding"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AAuthenticationEventThresholding/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-23 22:40:56"
build_source: "script"
---

# D3-ANET: Authentication Event Thresholding

Collecting authentication events, creating a baseline user profile, and determining whether authentication events are consistent with the baseline profile.

## Parent Technique

- [[D3-UBA-user_behavior_analysis|D3-UBA: User Behavior Analysis]]

## Knowledge Base Article

## How it works
Authentication event data is collected (logon information such as device id, time of day, day of week, geo-location, etc.) to create an activity baseline. Then, a threshold is determined either through a manually specified configuration, or a statistical analysis of deviations in historical data. New authentication events are evaluated to determine if a threshold is exceeded. Thresholds can be static or dynamic.

### Actions
As a result of the analysis, actions taken could include:

* [Account Locking](/technique/d3f:AccountLocking)
* Raising an alert

### Example data sources
 * Directory server logs
 * VPN Server logs
 * IDAM Capability logs
 * NAC logs
 * Authentication client logs
 * Kerberos network traffic
 * LDAP network traffic

## Considerations

This technique covers statistical outliers. Though depending on the complexity or dimensionality of the data considered, outliers may not be obvious to a human analyst reviewing events in simplistic analytic views. If the malicious activity is not statistically different from benign activity, an alert threshold will not be met.

## Ontology Relationships

- [[D3-UBA-user_behavior_analysis|D3-UBA: User Behavior Analysis]]

## Workspace

- [[kb/notes/d3fend/techniques/d3-anet-notes|Open workspace note]]

