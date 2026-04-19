
# 📘 MITRE ATT&CK Obsidian Vault – Design Context

## 🎯 Purpose

Build an Obsidian knowledge base from MITRE ATT&CK that is:

* Human-readable
* Operationally useful (SOC / pentesting)
* Fully cross-linked
* Rebuilt from scratch each run

---

# 🧱 Core Structure

```
kb/
├── tactics/
├── techniques/
├── mitigations/
├── tools/
```

---

# 🔗 Data Model (Critical)

## Tactics

* Top-level ATT&CK categories
* Link to techniques

## Techniques (PRIMARY OBJECT)

* One file per **parent technique**
* Subtechniques are **NOT files**
* Subtechniques are **sections inside parent files**

---

## Subtechniques

### Design Decision

* Stored as **headings**, not files
* Linked via **block IDs**

### Format

```markdown
### T1059.001: PowerShell
^t1059001-powershell
```

### Linking Format

```markdown
[[T1059-command_and_scripting_interpreter#^t1059001-powershell]]
```

---

## Mitigations

### Design Decision

* Only valid mitigation objects (`type == course-of-action`)
* Must have ATT&CK ID starting with `M`
* Skip if no linked techniques

### Structure

* Parent techniques = top-level bullet
* Subtechniques = indented block links

```markdown
- [[T1003-os_credential_dumping]]
    - [[T1003-os_credential_dumping#^t1003001-lsass-memory]]
```

---

## Tools (Phase 2)

### Design Decision

* Use `get_software()`
* Filter: `type == "tool"`
* DO NOT include malware

### Structure

#### Technique → Tools

```markdown
## Tools
- [[Mimikatz]]
```

#### Tool → Techniques

Same structure as mitigations:

* Parent techniques
* Subtechniques nested under parent

---

# ⚠️ Key Library Constraints

## mitreattack-python quirks

* `get_tools()` ❌ does NOT exist

* Use:

  * `get_software()`
  * `get_all_software_using_all_techniques()`

* `get_mitigations()` returns:

  * valid mitigations
  * deprecated objects
  * historical objects (sometimes with `Txxxx` IDs)

---

# 🧼 Rebuild Strategy (IMPORTANT)

### Design Decision

Vault must rebuild cleanly every run

### Implementation

```python
def clear_markdown_files(folder_path):
    for file in folder_path:
        delete .md files
```

Apply to:

* tactics
* techniques
* mitigations
* tools

---

# 🚨 Common Bugs (Already Solved)

## 1. Subtechniques linking incorrectly

Cause:

* Treated as standalone files

Fix:

* Always link via block IDs inside parent technique

---

## 2. Orphan mitigation files (e.g. T1499-...)

Cause:

* Old ATT&CK format OR invalid object type

Fix:

* Enforce:

  * `type == course-of-action`
  * ID starts with `M`
  * has linked techniques

---

## 3. Tool pages missing subtechniques

Cause:

* Same mistake as mitigations (flat linking)

Fix:

* Reuse mitigation-style parent/sub grouping

---

## 4. Orphan files persisting

Cause:

* No cleanup before rebuild

Fix:

* Delete all `.md` files before generation

---

# 🧠 Phase 1 (Operational Value)

Added to **technique pages**:

## Detection

`x_mitre_detection`

## Data Sources

`x_mitre_data_sources`

## Platforms

`x_mitre_platforms`

## Required Permissions

`x_mitre_permissions_required`

---

# 🧠 Phase 2 (Partial)

Included:

* Tools

Excluded:

* Groups
* Malware

---

# 🧭 Design Philosophy

## 1. No abstraction for juniors

* Explicit functions
* No complex loops
* Clear sections

## 2. Vault reflects reality

* Parent techniques = files
* Subtechniques = sections

## 3. Relationships > raw data

* Only include objects that connect to something useful

---

# 🧩 Future Improvements

## High value next steps

### 1. Data Source → Technique mapping

> “What can I detect with X logs?”

### 2. Detection engineering notes

Custom section per technique

### 3. SIEM mappings

Link techniques to detection rules

---

# 🧾 How to reuse this

In a future chat, just paste:

```
Here is my MITRE Obsidian vault design:
[paste this file]
```

Then ask:

* “extend it”
* “fix a bug”
* “add feature”

And I won’t need to re-derive anything.


