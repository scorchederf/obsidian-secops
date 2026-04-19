---
id: T1102
name: Web Service
created: 2017-05-31 21:31:13.915000+00:00
modified: 2025-10-24 17:49:02.831000+00:00
type: attack-pattern
x_mitre_version: 1.3
x_mitre_domains: enterprise-attack
---

## Tactic

- [[command_and_control|Command and Control]]

Adversaries may use an existing, legitimate external Web service as a means for relaying data to/from a compromised system. Popular websites, cloud services, and social media acting as a mechanism for C2 may give a significant amount of cover due to the likelihood that hosts within a network are already communicating with them prior to a compromise. Using common services, such as those offered by Google, Microsoft, or Twitter, makes it easier for adversaries to hide in expected noise.(Citation: Broadcom BirdyClient Microsoft Graph API 2024) Web service providers commonly use SSL/TLS encryption, giving adversaries an added level of protection.

Use of Web services may also protect back-end C2 infrastructure from discovery through malware binary analysis while also enabling operational resiliency (since this infrastructure may be dynamically changed).

## Properties

- id: T1102
- name: Web Service
- created: 2017-05-31 21:31:13.915000+00:00
- modified: 2025-10-24 17:49:02.831000+00:00
- type: attack-pattern
- x_mitre_version: 1.3
- x_mitre_domains: enterprise-attack

## Subtechniques

### T1102.001: Dead Drop Resolver

^t1102001-dead-drop-resolver

**Parent Technique**
- [[T1102-web_service|T1102: Web Service]]

**Tactic**
- [[command_and_control|Command and Control]]

Adversaries may use an existing, legitimate external Web service to host information that points to additional command and control (C2) infrastructure. Adversaries may post content, known as a dead drop resolver, on Web services with embedded (and often obfuscated/encoded) domains or IP addresses. Once infected, victims will reach out to and be redirected by these resolvers.

Popular websites and social media acting as a mechanism for C2 may give a significant amount of cover due to the likelihood that hosts within a network are already communicating with them prior to a compromise. Using common services, such as those offered by Google or Twitter, makes it easier for adversaries to hide in expected noise. Web service providers commonly use SSL/TLS encryption, giving adversaries an added level of protection.

Use of a dead drop resolver may also protect back-end C2 infrastructure from discovery through malware binary analysis while also enabling operational resiliency (since this infrastructure may be dynamically changed).

#### Properties

- id: T1102.001
- name: Dead Drop Resolver
- created: 2020-03-14 22:24:21.841000+00:00
- modified: 2025-10-24 17:49:37.828000+00:00
- type: attack-pattern
- x_mitre_version: 1.1
- x_mitre_domains: enterprise-attack

### T1102.002: Bidirectional Communication

^t1102002-bidirectional-communication

**Parent Technique**
- [[T1102-web_service|T1102: Web Service]]

**Tactic**
- [[command_and_control|Command and Control]]

Adversaries may use an existing, legitimate external Web service as a means for sending commands to and receiving output from a compromised system over the Web service channel. Compromised systems may leverage popular websites and social media to host command and control (C2) instructions. Those infected systems can then send the output from those commands back over that Web service channel. The return traffic may occur in a variety of ways, depending on the Web service being utilized. For example, the return traffic may take the form of the compromised system posting a comment on a forum, issuing a pull request to development project, updating a document hosted on a Web service, or by sending a Tweet. 

Popular websites and social media acting as a mechanism for C2 may give a significant amount of cover due to the likelihood that hosts within a network are already communicating with them prior to a compromise. Using common services, such as those offered by Google or Twitter, makes it easier for adversaries to hide in expected noise. Web service providers commonly use SSL/TLS encryption, giving adversaries an added level of protection. 

#### Properties

- id: T1102.002
- name: Bidirectional Communication
- created: 2020-03-14 22:34:03.024000+00:00
- modified: 2025-10-24 17:49:18.602000+00:00
- type: attack-pattern
- x_mitre_version: 1.1
- x_mitre_domains: enterprise-attack

### T1102.003: One-Way Communication

^t1102003-one-way-communication

**Parent Technique**
- [[T1102-web_service|T1102: Web Service]]

**Tactic**
- [[command_and_control|Command and Control]]

Adversaries may use an existing, legitimate external Web service as a means for sending commands to a compromised system without receiving return output over the Web service channel. Compromised systems may leverage popular websites and social media to host command and control (C2) instructions. Those infected systems may opt to send the output from those commands back over a different C2 channel, including to another distinct Web service. Alternatively, compromised systems may return no output at all in cases where adversaries want to send instructions to systems and do not want a response.

Popular websites and social media acting as a mechanism for C2 may give a significant amount of cover due to the likelihood that hosts within a network are already communicating with them prior to a compromise. Using common services, such as those offered by Google or Twitter, makes it easier for adversaries to hide in expected noise. Web service providers commonly use SSL/TLS encryption, giving adversaries an added level of protection.

#### Properties

- id: T1102.003
- name: One-Way Communication
- created: 2020-03-14 22:45:52.963000+00:00
- modified: 2025-10-24 17:49:08.849000+00:00
- type: attack-pattern
- x_mitre_version: 1.1
- x_mitre_domains: enterprise-attack

## Mitigations

- [[M1021-restrict_web-based_content|M1021: Restrict Web-Based Content]]
- [[M1031-network_intrusion_prevention|M1031: Network Intrusion Prevention]]

## Platforms

- ESXi
- Linux
- Windows
- macOS

## Tools

- [[S0508-ngrok|S0508: ngrok]]
- [[S1063-brute_ratel_c4|S1063: Brute Ratel C4]]

