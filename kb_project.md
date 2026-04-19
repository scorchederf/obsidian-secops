# MITRE ATT&CK Obsidian Vault – Project Context

## Purpose
Build an Obsidian knowledge base from MITRE ATT&CK that is:

- Human-readable
- Operationally useful
- Fully cross-linked
- Rebuilt from scratch on every run

## Directory Structure

```text
kb/
├── tactics/
├── techniques/
├── mitigations/
├── tools/
```

## Core Data Model

### Tactics
- One file per tactic
- Tactic files link to parent techniques
- Tactic files link to subtechniques as block links into the parent technique file

### Techniques
- One file per parent technique
- Technique filename format:
  - `Txxxx-technique_name.md`

### Subtechniques
- Subtechniques are not standalone files
- Subtechniques are sections inside the parent technique file
- Each subtechnique uses:
  - a human-readable heading
  - a stable Obsidian block ID

Example:

```markdown
### T1003.002: Security Account Manager
^t1003002-security-account-manager
```

Link format:

```markdown
[[T1003-os_credential_dumping#^t1003002-security-account-manager|T1003.002: Security Account Manager]]
```

### Mitigations
- One file per valid mitigation
- Mitigation filename format:
  - `Mxxxx-mitigation_name.md`
- Keep only:
  - `type == "course-of-action"`
  - ATT&CK ID starts with `M`
  - mitigation must actually link to at least one technique/subtechnique

### Tools
- Tools are included
- Malware is excluded
- Tools come from `get_software()` and are filtered by:
  - `type == "tool"`
- Tool filenames use name only by default
- If two tools normalize to the same filename, append the ATT&CK ID

Examples:

```text
mimikatz.md
procdump.md
some_tool-s1234.md
```

## Rebuild Strategy
The vault rebuilds from scratch each run.

Delete all `.md` files in:
- tactics
- techniques
- mitigations
- tools

This avoids:
- orphan files
- stale filenames
- broken links from earlier refactors

## Key Decisions

### 1. No standalone subtechnique files
Subtechniques live inside parent technique files.

### 2. Human-readable subtechnique headings
Use:

```markdown
### T1001.003: Protocol or Service Impersonation
^t1001003-protocol-or-service-impersonation
```

Do not use machine-only headings.

### 3. Block links for subtechniques
Subtechniques are linked with stable block IDs, not fake filenames.

### 4. Properties function calls are commented out
The functions remain in the script, but the calls are disabled for now.

### 5. Data sources are only added to technique pages
No separate `data_sources` folder is used.

### 6. Required Permissions may be empty
That field is inconsistently populated in ATT&CK data.

### 7. Tools use name-first filenames
Names are more natural in Obsidian. Collision handling is built in.

## Library Constraints

### Working methods
- `get_tactics()`
- `get_techniques()`
- `get_subtechniques_of_technique(...)`
- `get_mitigations()`
- `get_all_mitigations_mitigating_all_techniques()`
- `get_software()`
- `get_all_software_using_all_techniques()`

### Not available in this environment
- `get_tools()`
- generic relation helpers like `get_objects_by_relation(...)`

## Technique Pages Currently Include
- YAML frontmatter
- Tactic link
- Description
- Subtechniques
- Mitigations
- Detection
- Data Sources
- Platforms
- Required Permissions
- Tools

Properties section is present in code but disabled in output.

## Mitigation Pages Include
- YAML frontmatter
- Description
- Properties
- Techniques mitigated

Parent techniques are top-level bullets.
Subtechniques are nested under parents.

## Tool Pages Include
- YAML frontmatter
- Description
- Properties
- Techniques used

Parent techniques are top-level bullets.
Subtechniques are nested under parents.

## Historical Bugs Already Solved

### Broken subtechnique links
Cause:
- subtechniques were treated as standalone files

Fix:
- block links into parent technique files

### Orphan mitigation files like `Txxxx...`
Cause:
- historical or invalid mitigation objects were being written

Fix:
- require `type == "course-of-action"`
- require ID starts with `M`
- skip empty mitigation files

### Tool pages broke on subtechniques
Cause:
- flat technique linking

Fix:
- same parent/sub structure as mitigation pages

### Orphan files persisted
Cause:
- no cleanup before regeneration

Fix:
- delete markdown files before every run

### Tool filename refactor caused broken calls
Cause:
- helper signature changed but call sites still passed `tool_id`

Fix:
- centralize with `tool_filename_map`

## Philosophy
- Keep code explicit and junior-friendly
- Prefer simple helpers
- Avoid clever abstractions
- Keep relationships accurate to vault structure

## Good Future Additions
- Groups
- Malware
- Reverse data-source mapping
- SIEM mapping notes
- Validation script for broken links and orphan files

## Reuse Instructions
Paste this file into a future chat and say:

> Use this as the project context for my MITRE Obsidian vault script.
