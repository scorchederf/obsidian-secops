---
id: M1019
name: Threat Intelligence Program
created: 2019-06-06 19:55:50.927000+00:00
modified: 2024-12-24 14:05:21.946000+00:00
type: course-of-action
---

# Threat Intelligence Program

A Threat Intelligence Program enables organizations to proactively identify, analyze, and act on cyber threats by leveraging internal and external data sources. The program supports decision-making processes, prioritizes defenses, and improves incident response by delivering actionable intelligence tailored to the organization's risk profile and operational environment. This mitigation can be implemented through the following measures:

Establish a Threat Intelligence Team:

- Form a dedicated team or assign responsibility to existing security personnel to collect, analyze, and act on threat intelligence.

Define Intelligence Requirements:

- Identify the organization’s critical assets and focus intelligence gathering efforts on threats targeting these assets.

Leverage Internal and External Data Sources:

- Collect intelligence from internal sources such as logs, incidents, and alerts.
Subscribe to external threat intelligence feeds, participate in ISACs, and monitor open-source intelligence (OSINT).

Implement Tools for Automation:

- Use threat intelligence platforms (TIPs) to automate the collection, enrichment, and dissemination of threat data.
- Integrate threat intelligence with SIEMs to correlate IOCs with internal events.

Analyze and Act on Intelligence:

- Use frameworks like MITRE ATT&CK to map intelligence to adversary TTPs.
- Prioritize defensive measures, such as patching vulnerabilities or deploying IOCs, based on analyzed threats.

Share and Collaborate:

- Share intelligence with industry peers through ISACs or threat-sharing platforms to enhance collective defense.

Evaluate and Update the Program:

- Regularly assess the effectiveness of the threat intelligence program.
- Update intelligence priorities and capabilities as new threats emerge.

*Tools for Implementation*

Threat Intelligence Platforms (TIPs):

- OpenCTI: An open-source platform for structuring and sharing threat intelligence.
- MISP: A threat intelligence sharing platform for sharing structured threat data.

Threat Intelligence Feeds:

- Open Threat Exchange (OTX): Provides free access to a large repository of threat intelligence.
- CIRCL OSINT Feed: A free source for IOCs and threat information.

Automation and Enrichment Tools:

- TheHive: An open-source incident response platform with threat intelligence integration.
- Yeti: A platform for managing and structuring knowledge about threats.

Analysis Frameworks:

- MITRE ATT&CK Navigator: A tool for mapping threat intelligence to adversary behaviors.
- Cuckoo Sandbox: Analyzes malware to extract behavioral indicators.

Community and Collaboration Tools:

- ISAC Memberships: Join industry-specific ISACs for intelligence sharing.
- Slack/Discord Channels: Participate in threat intelligence communities for real-time collaboration.

## Properties

- id: M1019
- name: Threat Intelligence Program
- created: 2019-06-06 19:55:50.927000+00:00
- modified: 2024-12-24 14:05:21.946000+00:00
- type: course-of-action

## Mitigates Techniques

- [[T1068-exploitation_for_privilege_escalation|T1068: Exploitation for Privilege Escalation]]
- [[T1210-exploitation_of_remote_services|T1210: Exploitation of Remote Services]]
- [[T1211-exploitation_for_defense_evasion|T1211: Exploitation for Defense Evasion]]
- [[T1212-exploitation_for_credential_access|T1212: Exploitation for Credential Access]]
- [[T1656-impersonation|T1656: Impersonation]]

