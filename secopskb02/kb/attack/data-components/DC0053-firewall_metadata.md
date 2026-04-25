---
mitre_id: "DC0053"
mitre_name: "Firewall Metadata"
mitre_type: "x-mitre-data-component"
mitre_stix_id: "x-mitre-data-component--746f095a-f84c-4ccc-90a5-c7caa5c100a2"
mitre_created: "2021-10-20T15:05:19.273Z"
mitre_modified: "2025-10-21T15:10:28.402Z"
mitre_version: "2.0"
mitre_domains:
  - "enterprise-attack"
framework: "attack"
generated: "true"
build_date: "2026-04-25 20:43:29"
build_source: "script"
object_type: "data-component"
tags:
  - "attack"
  - "data-component"
  - "detection"
  - "telemetry"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Contextual information about firewalls, including their configurations, policies, status, and other details such as names and associated rules. This metadata provides valuable insights into the operational state and configurations of firewalls, both in cloud control planes and host systems. Examples: 

- Firewall Name and Configuration: The name, type, and purpose of a firewall such as "Azure Firewall - Production Environment."
- Policy Details: Capturing firewall policy details, such as "Allow inbound TCP 443 to web servers."
- Firewall Status: Status indicators like "Active," "Disabled," or "Pending Updates."
- Audit Log Metadata: Log entries showing administrative changes, such as "Policy modified by admin@domain.com."
- Rules Associated with Firewalls: Rules specifying source/destination IP ranges, protocols, and ports.
- Tagging Information: Tags like "Environment: Production" or "Owner: NetworkOps."

This data component can be collected through the following measures:

Cloud Control Plane

- Azure: Use Azure Activity Logs and Network Watcher to collect metadata for Azure Firewall.
    - Example: `az network firewall show --name <firewall-name>`
- AWS: Use AWS CloudTrail and describe commands: `aws ec2 describe-security-groups`
- Google Cloud: Use gcloud commands to extract metadata: `gcloud compute firewall-rules list --format=json`

Host-Based Firewalls

- Windows: Use PowerShell to gather metadata: `Get-NetFirewallRule -PolicyStore PersistentStore`
- Linux: Query iptables or nftables rulesets: `iptables -S`
- macOS: Use pfctl to extract metadata: `sudo pfctl -sr`

SIEM Integration

- Collect logs from cloud platforms, host systems, and network appliances.

API Monitoring

- Monitor API calls for metadata requests. Example (AWS): `Capture DescribeSecurityGroups or DescribeNetworkAcls` calls via CloudTrail.

Endpoint Detection and Response (EDR)

- Use EDR solutions to monitor firewall management tools for configuration changes or queries.

## Workspace

- [[workspaces/attack/data-components/DC0053-firewall_metadata-note|Open workspace note]]

![[workspaces/attack/data-components/DC0053-firewall_metadata-note]]

