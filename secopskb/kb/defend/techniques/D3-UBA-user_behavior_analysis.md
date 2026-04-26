---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-UBA"
d3fend_name: "User Behavior Analysis"
d3fend_ontology_id: "d3f:UserBehaviorAnalysis"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AUserBehaviorAnalysis/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

User behavior analytics ("UBA") as defined by Gartner, is a cybersecurity process about detection of insider threats, targeted attacks, and financial fraud. UBA solutions look at patterns of human behavior, and then apply algorithms and statistical analysis to detect meaningful anomalies from those patterns-anomalies that indicate potential threats.' Instead of tracking devices or security events, UBA tracks a system's users. Big data platforms are increasing UBA functionality by allowing them to analyze petabytes worth of data to detect insider threats and advanced persistent threats.

## Workspace

- [[workspaces/defend/techniques/D3-UBA-user_behavior_analysis-note|Open workspace note]]

![[workspaces/defend/techniques/D3-UBA-user_behavior_analysis-note]]

## Child Techniques

- [[D3-ANET-authentication_event_thresholding|D3-ANET: Authentication Event Thresholding]]
- [[D3-AZET-authorization_event_thresholding|D3-AZET: Authorization Event Thresholding]]
- [[D3-CCSA-credential_compromise_scope_analysis|D3-CCSA: Credential Compromise Scope Analysis]]
- [[D3-DAM-domain_account_monitoring|D3-DAM: Domain Account Monitoring]]
- [[D3-JFAPA-job_function_access_pattern_analysis|D3-JFAPA: Job Function Access Pattern Analysis]]
- [[D3-LAM-local_account_monitoring|D3-LAM: Local Account Monitoring]]
- [[D3-RAPA-resource_access_pattern_analysis|D3-RAPA: Resource Access Pattern Analysis]]
- [[D3-SDA-session_duration_analysis|D3-SDA: Session Duration Analysis]]
- [[D3-UDTA-user_data_transfer_analysis|D3-UDTA: User Data Transfer Analysis]]
- [[D3-UGLPA-user_geolocation_logon_pattern_analysis|D3-UGLPA: User Geolocation Logon Pattern Analysis]]
- [[D3-WSAA-web_session_activity_analysis|D3-WSAA: Web Session Activity Analysis]]

## Knowledge Base Article

## Technique Overview

Some techniques monitor patterns of human behavior and then apply algorithms and to identify patterns such as repeated login attempts from a single IP address or large file downloads, or abnormal accesses.

Other techniques may have explicit or rigid definitions of "bad behavior" which are then matched against instances in a computer network environment.

