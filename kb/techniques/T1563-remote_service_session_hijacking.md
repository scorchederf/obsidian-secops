---
id: T1563
name: Remote Service Session Hijacking
created: 2020-02-25 18:26:16.994000+00:00
modified: 2025-10-24 17:48:50.118000+00:00
type: attack-pattern
x_mitre_version: 1.1
x_mitre_domains: enterprise-attack
---

## Tactic

- [[lateral_movement|Lateral Movement]]

Adversaries may take control of preexisting sessions with remote services to move laterally in an environment. Users may use valid credentials to log into a service specifically designed to accept remote connections, such as telnet, SSH, and RDP. When a user logs into a service, a session will be established that will allow them to maintain a continuous interaction with that service.

Adversaries may commandeer these sessions to carry out actions on remote systems. [Remote Service Session Hijacking](https://attack.mitre.org/techniques/T1563) differs from use of [Remote Services](https://attack.mitre.org/techniques/T1021) because it hijacks an existing session rather than creating a new session using [Valid Accounts](https://attack.mitre.org/techniques/T1078).(Citation: RDP Hijacking Medium)(Citation: Breach Post-mortem SSH Hijack)

## Properties

- id: T1563
- name: Remote Service Session Hijacking
- created: 2020-02-25 18:26:16.994000+00:00
- modified: 2025-10-24 17:48:50.118000+00:00
- type: attack-pattern
- x_mitre_version: 1.1
- x_mitre_domains: enterprise-attack

## Subtechniques

### T1563.001: SSH Hijacking

^t1563001-ssh-hijacking

**Parent Technique**
- [[T1563-remote_service_session_hijacking|T1563: Remote Service Session Hijacking]]

**Tactic**
- [[lateral_movement|Lateral Movement]]

Adversaries may hijack a legitimate user's SSH session to move laterally within an environment. Secure Shell (SSH) is a standard means of remote access on Linux and macOS systems. It allows a user to connect to another system via an encrypted tunnel, commonly authenticating through a password, certificate or the use of an asymmetric encryption key pair.

In order to move laterally from a compromised host, adversaries may take advantage of trust relationships established with other systems via public key authentication in active SSH sessions by hijacking an existing connection to another system. This may occur through compromising the SSH agent itself or by having access to the agent's socket. If an adversary is able to obtain root access, then hijacking SSH sessions is likely trivial.(Citation: Slideshare Abusing SSH)(Citation: SSHjack Blackhat)(Citation: Clockwork SSH Agent Hijacking)(Citation: Breach Post-mortem SSH Hijack)

[SSH Hijacking](https://attack.mitre.org/techniques/T1563/001) differs from use of [SSH](https://attack.mitre.org/techniques/T1021/004) because it hijacks an existing SSH session rather than creating a new session using [Valid Accounts](https://attack.mitre.org/techniques/T1078).

#### Properties

- id: T1563.001
- name: SSH Hijacking
- created: 2020-02-25 18:34:38.290000+00:00
- modified: 2025-10-24 17:48:45.240000+00:00
- type: attack-pattern
- x_mitre_version: 1.1
- x_mitre_domains: enterprise-attack

### T1563.002: RDP Hijacking

^t1563002-rdp-hijacking

**Parent Technique**
- [[T1563-remote_service_session_hijacking|T1563: Remote Service Session Hijacking]]

**Tactic**
- [[lateral_movement|Lateral Movement]]

Adversaries may hijack a legitimate user’s remote desktop session to move laterally within an environment. Remote desktop is a common feature in operating systems. It allows a user to log into an interactive session with a system desktop graphical user interface on a remote system. Microsoft refers to its implementation of the Remote Desktop Protocol (RDP) as Remote Desktop Services (RDS).(Citation: TechNet Remote Desktop Services)

Adversaries may perform RDP session hijacking which involves stealing a legitimate user's remote session. Typically, a user is notified when someone else is trying to steal their session. With System permissions and using Terminal Services Console, `c:\windows\system32\tscon.exe [session number to be stolen]`, an adversary can hijack a session without the need for credentials or prompts to the user.(Citation: RDP Hijacking Korznikov) This can be done remotely or locally and with active or disconnected sessions.(Citation: RDP Hijacking Medium) It can also lead to [Remote System Discovery](https://attack.mitre.org/techniques/T1018) and Privilege Escalation by stealing a Domain Admin or higher privileged account session. All of this can be done by using native Windows commands, but it has also been added as a feature in red teaming tools.(Citation: Kali Redsnarf)

#### Properties

- id: T1563.002
- name: RDP Hijacking
- created: 2020-02-25 18:35:42.765000+00:00
- modified: 2025-10-24 17:49:30.049000+00:00
- type: attack-pattern
- x_mitre_version: 1.1
- x_mitre_domains: enterprise-attack

## Mitigations

- [[M1018-user_account_management|M1018: User Account Management]]
- [[M1026-privileged_account_management|M1026: Privileged Account Management]]
- [[M1027-password_policies|M1027: Password Policies]]
- [[M1030-network_segmentation|M1030: Network Segmentation]]
- [[M1042-disable_or_remove_feature_or_program|M1042: Disable or Remove Feature or Program]]

## Platforms

- Linux
- macOS
- Windows

