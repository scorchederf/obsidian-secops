---
mitre_id: "T1563"
mitre_name: "Remote Service Session Hijacking"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--5b0ad6f8-6a16-4966-a4ef-d09ea6e2a9f5"
mitre_created: "2020-02-25T18:26:16.994Z"
mitre_modified: "2025-10-24T17:48:50.118Z"
mitre_version: "1.1"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1563/"
build_date: "2026-04-21 20:44:18"
build_source: "script"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Linux"
  - "macOS"
  - "Windows"
mitre_tactic_ids:
  - "TA0008"
---

# T1563: Remote Service Session Hijacking

Adversaries may take control of preexisting sessions with remote services to move laterally in an environment. Users may use valid credentials to log into a service specifically designed to accept remote connections, such as telnet, SSH, and RDP. When a user logs into a service, a session will be established that will allow them to maintain a continuous interaction with that service.

Adversaries may commandeer these sessions to carry out actions on remote systems. [[T1563-remote_service_session_hijacking|T1563: Remote Service Session Hijacking]] differs from use of [[T1021-remote_services|T1021: Remote Services]] because it hijacks an existing session rather than creating a new session using [[T1078-valid_accounts|T1078: Valid Accounts]].(Citation: RDP Hijacking Medium)(Citation: Breach Post-mortem SSH Hijack)

## Tactics

- [[TA0008-lateral_movement|TA0008: Lateral Movement]]

## Subtechniques

### T1563.001: SSH Hijacking

^t1563001-ssh-hijacking

Adversaries may hijack a legitimate user's SSH session to move laterally within an environment. Secure Shell (SSH) is a standard means of remote access on Linux and macOS systems. It allows a user to connect to another system via an encrypted tunnel, commonly authenticating through a password, certificate or the use of an asymmetric encryption key pair.

In order to move laterally from a compromised host, adversaries may take advantage of trust relationships established with other systems via public key authentication in active SSH sessions by hijacking an existing connection to another system. This may occur through compromising the SSH agent itself or by having access to the agent's socket. If an adversary is able to obtain root access, then hijacking SSH sessions is likely trivial.(Citation: Slideshare Abusing SSH)(Citation: SSHjack Blackhat)(Citation: Clockwork SSH Agent Hijacking)(Citation: Breach Post-mortem SSH Hijack)

[[T1563-remote_service_session_hijacking#^t1563001-ssh-hijacking|T1563.001: SSH Hijacking]] differs from use of [[T1021-remote_services#^t1021004-ssh|T1021.004: SSH]] because it hijacks an existing SSH session rather than creating a new session using [[T1078-valid_accounts|T1078: Valid Accounts]].

### T1563.002: RDP Hijacking

^t1563002-rdp-hijacking

Adversaries may hijack a legitimate user’s remote desktop session to move laterally within an environment. Remote desktop is a common feature in operating systems. It allows a user to log into an interactive session with a system desktop graphical user interface on a remote system. Microsoft refers to its implementation of the Remote Desktop Protocol (RDP) as Remote Desktop Services (RDS).(Citation: TechNet Remote Desktop Services)

Adversaries may perform RDP session hijacking which involves stealing a legitimate user's remote session. Typically, a user is notified when someone else is trying to steal their session. With System permissions and using Terminal Services Console, `c:\windows\system32\tscon.exe [session number to be stolen]`, an adversary can hijack a session without the need for credentials or prompts to the user.(Citation: RDP Hijacking Korznikov) This can be done remotely or locally and with active or disconnected sessions.(Citation: RDP Hijacking Medium) It can also lead to [[T1018-remote_system_discovery|T1018: Remote System Discovery]] and Privilege Escalation by stealing a Domain Admin or higher privileged account session. All of this can be done by using native Windows commands, but it has also been added as a feature in red teaming tools.(Citation: Kali Redsnarf)

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

