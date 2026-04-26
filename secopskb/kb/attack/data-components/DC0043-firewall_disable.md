---
mitre_id: "DC0043"
mitre_name: "Firewall Disable"
mitre_type: "x-mitre-data-component"
mitre_stix_id: "x-mitre-data-component--c97d0171-f6e0-4415-85ff-4082fdb8c72a"
mitre_created: "2021-10-20T15:05:19.273Z"
mitre_modified: "2025-10-21T15:14:40.022Z"
mitre_version: "2.0"
mitre_domains:
  - "enterprise-attack"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "data-component"
tags:
  - "attack"
  - "data-component"
  - "detection"
  - "telemetry"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

The deactivation, misconfiguration, or complete stoppage of firewall services, either on a host or in a cloud control plane. Such activity may involve turning off firewalls, modifying rules to disable protection, or deleting firewall-related configurations and activity logs. Examples: 

- Disabling Host-Based Firewalls: Stopping the Windows Defender Firewall service or using `iptables -F` to flush all rules on a Linux system.
- Cloud Firewall Modification or Deactivation: Modifying or deleting security group rules in AWS or disabling a network firewall in Azure.
- Activity Log Deletion: Writing or deleting entries in Azure Firewall Activity Logs to hide unauthorized firewall changes.
- Temporary Disable for Malicious Operations: Temporarily disabling a firewall to allow malicious files or traffic, then re-enabling it to avoid detection.
- Using Command-Line Tools to Stop Firewalls: Running commands like `Set-NetFirewallProfile -Enabled False on Windows or systemctl stop ufw` on Linux.

This data component can be collected through the following measures:

Cloud Control Plane

- Azure Activity Logs:
    - Enable logging of administrative actions, such as stopping or modifying Azure Firewall configurations.
    - Use Azure Monitor to track specific firewall-related actions, including disabling or rule deletion.
- AWS CloudTrail Logs:
    - Monitor `RevokeSecurityGroupIngress` or `RevokeSecurityGroupEgress` events to detect rule changes in AWS Security Groups.
- Google Cloud Platform Logs:
    - Collect logs from the Firewall Rules resource in Google Cloud Operations Suite to detect rule deletions or modifications.

Host-Level Firewalls

- Windows Firewall Event Logs:
    - Enable logging of firewall state changes:
        - Security Event ID 2004: Firewall service stopped.
        - Security Event ID 2005: Firewall service started.
    - Use Sysmon for process creation events tied to firewall commands or scripts (Sysmon Event ID 1).
- Linux Firewall Logs: Use auditd to track commands like iptables, firewalld, or ufw: `auditctl -a always,exit -F arch=b64 -S execve -k firewall_disable`
- macOS Firewall: Monitor changes to the macOS Application Firewall using the log show command.

Network-Level Monitoring

- IDS/IPS Alerts: Deploy IDS/IPS systems to monitor abnormal traffic flows that could indicate firewall disablement.
- NetFlow Data: Analyze NetFlow or packet capture data for traffic patterns inconsistent with firewall enforcement.

SIEM and CSPM Tools

- SIEM Integration: Use tools like Splunk or QRadar to centralize and analyze firewall disablement events from both hosts and cloud platforms.
- Cloud Security Posture Management (CSPM): Use CSPM solutions to monitor misconfigurations and track deactivation of critical cloud services like firewalls.

## Workspace

- [[workspaces/attack/data-components/DC0043-firewall_disable-note|Open workspace note]]

![[workspaces/attack/data-components/DC0043-firewall_disable-note]]

