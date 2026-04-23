---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-AEM"
d3fend_name: "Application Exception Monitoring"
d3fend_ontology_id: "d3f:ApplicationExceptionMonitoring"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AApplicationExceptionMonitoring/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-23 22:40:56"
build_source: "script"
attack_technique_ids:
  - "T1003"
  - "T1003.005"
  - "T1003.006"
  - "T1070"
  - "T1070.001"
  - "T1070.003"
  - "T1110"
  - "T1110.001"
  - "T1110.003"
  - "T1110.004"
  - "T1134"
  - "T1134.002"
  - "T1134.003"
  - "T1140"
  - "T1187"
  - "T1546"
  - "T1546.003"
  - "T1546.005"
  - "T1548"
  - "T1548.003"
---

# D3-AEM: Application Exception Monitoring

Monitoring the failures of system counters and timers.

## Parent Technique

- [[D3-APM-application_performance_monitoring|D3-APM: Application Performance Monitoring]]

## Related ATT&CK Techniques

- [[T1003-os_credential_dumping|T1003: OS Credential Dumping]]
- [[T1003-os_credential_dumping#^t1003005-cached-domain-credentials|T1003.005: Cached Domain Credentials]]
- [[T1003-os_credential_dumping#^t1003006-dcsync|T1003.006: DCSync]]
- [[T1070-indicator_removal|T1070: Indicator Removal]]
- [[T1070-indicator_removal#^t1070001-clear-windows-event-logs|T1070.001: Clear Windows Event Logs]]
- [[T1070-indicator_removal#^t1070003-clear-command-history|T1070.003: Clear Command History]]
- [[T1110-brute_force|T1110: Brute Force]]
- [[T1110-brute_force#^t1110001-password-guessing|T1110.001: Password Guessing]]
- [[T1110-brute_force#^t1110003-password-spraying|T1110.003: Password Spraying]]
- [[T1110-brute_force#^t1110004-credential-stuffing|T1110.004: Credential Stuffing]]
- [[T1134-access_token_manipulation|T1134: Access Token Manipulation]]
- [[T1134-access_token_manipulation#^t1134002-create-process-with-token|T1134.002: Create Process with Token]]
- [[T1134-access_token_manipulation#^t1134003-make-and-impersonate-token|T1134.003: Make and Impersonate Token]]
- [[T1140-deobfuscate_decode_files_or_information|T1140: Deobfuscate/Decode Files or Information]]
- [[T1187-forced_authentication|T1187: Forced Authentication]]
- [[T1546-event_triggered_execution|T1546: Event Triggered Execution]]
- [[T1546-event_triggered_execution#^t1546003-windows-management-instrumentation-event-subscription|T1546.003: Windows Management Instrumentation Event Subscription]]
- [[T1546-event_triggered_execution#^t1546005-trap|T1546.005: Trap]]
- [[T1548-abuse_elevation_control_mechanism|T1548: Abuse Elevation Control Mechanism]]
- [[T1548-abuse_elevation_control_mechanism#^t1548003-sudo-and-sudo-caching|T1548.003: Sudo and Sudo Caching]]

## Knowledge Base Article

## How it works
Monitoring timer and counter failures or exceedances can reveal issues with the program or platform, and is important for both safety and security. It may also help identify tampering or malicious activity affecting the device or the processes it controls.

## Ontology Relationships

- [[D3-APM-application_performance_monitoring|D3-APM: Application Performance Monitoring]]

## Workspace

- [[kb/notes/d3fend/techniques/d3-aem-notes|Open workspace note]]

