---
id: M1039
name: Environment Variable Permissions
created: 2019-06-11 16:40:14.543000+00:00
modified: 2024-12-11 17:54:05.697000+00:00
type: course-of-action
---

# Environment Variable Permissions

Restrict the modification of environment variables to authorized users and processes by enforcing strict permissions and policies. This ensures the integrity of environment variables, preventing adversaries from abusing or altering them for malicious purposes. This mitigation can be implemented through the following measures:

Restrict Write Access:

- Use Case: Set file system-level permissions to restrict access to environment variable configuration files (e.g., `.bashrc`, `.bash_profile`, `.zshrc`, `systemd` service files).
- Implementation: Configure `/etc/environment` or `/etc/profile` on Linux systems to only allow root or administrators to modify the file.

Secure Access Controls:

- Use Case: Limit access to environment variable settings in application deployment tools or CI/CD pipelines to authorized personnel.
- Implementation: Use role-based access control (RBAC) in tools like Jenkins or GitLab to ensure only specific users can modify environment variables.

Restrict Process Scope:

- Use Case: Configure policies to ensure environment variables are only accessible to the processes they are explicitly intended for.
- Implementation: Use containerized environments like Docker to isolate environment variables to specific containers and ensure they are not inherited by other processes.

Audit Environment Variable Changes:

- Use Case: Enable logging for changes to critical environment variables.
- Implementation: Use `auditd` on Linux to monitor changes to files like `/etc/environment` or application-specific environment files.

## Mitigates Techniques

- [[T1070-indicator_removal|T1070: Indicator Removal]]
    - [[T1070-indicator_removal#^t1070003-clear-command-history|T1070.003: Clear Command History]]
- [[T1562-impair_defenses|T1562: Impair Defenses]]
    - [[T1562-impair_defenses#^t1562003-impair-command-history-logging|T1562.003: Impair Command History Logging]]

