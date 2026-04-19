# original version - simple, inline, kiss.

import os
import requests
from mitreattack.stix20 import MitreAttackData

#region config and setup
# ---------------------------
VAULT = "kb"
TACTICS_DIR = os.path.join(VAULT, "tactics")
TECHNIQUES_DIR = os.path.join(VAULT, "techniques")
local_json = "enterprise-attack.json"
url = "https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack.json"

# Setup
# ---------------------------
os.makedirs(TACTICS_DIR, exist_ok=True)
os.makedirs(TECHNIQUES_DIR, exist_ok=True)
if not os.path.exists(local_json):
    print("[+] Downloading MITRE ATT&CK dataset...")
    r = requests.get(url)
    r.raise_for_status()
    with open(local_json, "w", encoding="utf-8") as f:
        f.write(r.text)
#endregion

mitre = MitreAttackData(local_json)

# Loop through tactics and create individual markdown files
for tactic in mitre.get_tactics():
    filename = f"{tactic.name}.md".replace(" ", "_").lower()
    filepath = os.path.join(TACTICS_DIR, filename)
    
    with open(filepath, "w") as f:

        #region Write frontmatter YAML tags
        f.write("---\n")
        f.write(f"id: {tactic.id}\n")
        f.write(f"name: {tactic.name}\n")
        f.write(f"created: {tactic.created}\n")
        f.write(f"modified: {tactic.modified}\n")
        f.write(f"type: {tactic.type}\n")
        f.write(f"x_mitre_version: {tactic.x_mitre_version}\n")
        f.write(f"x_mitre_domains: {', '.join(tactic.x_mitre_domains)}\n")
        f.write("---\n\n")
        #endregion

        #region Write heading and description
        f.write(f"# {tactic.name}\n\n")
        f.write(f"{tactic.description}\n\n")
        #endregion

        #region Write list of properties
        f.write("## Properties\n\n")
        f.write(f"- id: {tactic.id}\n")
        f.write(f"- name: {tactic.name}\n")
        f.write(f"- created: {tactic.created}\n")
        f.write(f"- modified: {tactic.modified}\n")
        f.write(f"- type: {tactic.type}\n")
        f.write(f"- x_mitre_version: {tactic.x_mitre_version}\n")
        f.write(f"- x_mitre_domains: {', '.join(tactic.x_mitre_domains)}\n\n")
        #endregion

        #region Write list of related techniques
        # The get_techniques_by_tactic method needs the tactic's shortname
        # (e.g. "defense-evasion") and the domain (e.g. "enterprise-attack")
        tactic_shortname = tactic.x_mitre_shortname
        domain = tactic.x_mitre_domains[0]

        # Retrieve all techniques that belong to this tactic.
        # Note: this returns BOTH parent techniques and subtechniques in one flat list.
        related_techniques = mitre.get_techniques_by_tactic(tactic_shortname, domain)

        # Build a list of only the parent techniques (i.e. not subtechniques).
        # Subtechniques are flagged with x_mitre_is_subtechnique = True.
        # Each entry is a (attack_id, technique) tuple so we can sort by ID later.
        parent_techniques = []
        for technique in related_techniques:
            is_subtechnique = getattr(technique, "x_mitre_is_subtechnique", False)
            if not is_subtechnique:
                attack_id = mitre.get_attack_id(technique.id)
                parent_techniques.append((attack_id, technique))

        # Sort parent techniques by their ATT&CK ID (e.g. T1003, T1059, T1134)
        parent_techniques.sort()

        f.write("## Related Techniques\n\n")

        # Loop through each parent technique and write it as a top-level bullet
        for attack_id, technique in parent_techniques:
            # Create safe filename for the technique
            safe_name = technique.name.replace(" ", "_").replace("/", "_").lower()

            # Build link name (must match filename exactly)
            link_name = f"{attack_id}-{safe_name}"

            # Write Obsidian wiki link
            f.write(f"- [[{link_name}|{attack_id}: {technique.name}]]\n")


            #region Create markdown file for each parent technique

            # Build filename like: T1059-command_and_scripting_interpreter.md
            safe_name = technique.name.replace(" ", "_").replace("/", "_").lower()
            technique_filename = f"{attack_id}-{safe_name}.md"
            technique_filepath = os.path.join(TECHNIQUES_DIR, technique_filename)

            # Open file for writing
            with open(technique_filepath, "w", encoding="utf-8") as tf:

                # ---------------------------
                # Write frontmatter YAML
                # ---------------------------
                tf.write("---\n")
                tf.write(f"id: {attack_id}\n")
                tf.write(f"name: {technique.name}\n")
                tf.write(f"created: {technique.created}\n")
                tf.write(f"modified: {technique.modified}\n")
                tf.write(f"type: {technique.type}\n")

                # Some fields may not always exist, so check safely
                if hasattr(technique, "x_mitre_version"):
                    tf.write(f"x_mitre_version: {technique.x_mitre_version}\n")

                if hasattr(technique, "x_mitre_domains"):
                    tf.write(f"x_mitre_domains: {', '.join(technique.x_mitre_domains)}\n")

                tf.write("---\n\n")

                # ---------------------------
                # Heading and description
                # ---------------------------
                tactic_safe_name = tactic.name.replace(" ", "_").lower()

                tf.write("## Tactic\n\n")
                tf.write(f"- [[{tactic_safe_name}|{tactic.name}]]\n\n")

                if hasattr(technique, "description"):
                    tf.write(f"{technique.description}\n\n")

                # ---------------------------
                # Properties section
                # ---------------------------
                tf.write("## Properties\n\n")
                tf.write(f"- id: {attack_id}\n")
                tf.write(f"- name: {technique.name}\n")
                tf.write(f"- created: {technique.created}\n")
                tf.write(f"- modified: {technique.modified}\n")
                tf.write(f"- type: {technique.type}\n")

                if hasattr(technique, "x_mitre_version"):
                    tf.write(f"- x_mitre_version: {technique.x_mitre_version}\n")

                if hasattr(technique, "x_mitre_domains"):
                    tf.write(f"- x_mitre_domains: {', '.join(technique.x_mitre_domains)}\n")

                tf.write("\n")

                # ---------------------------
                # Subtechniques section (detailed)
                # ---------------------------
                tf.write("## Subtechniques\n\n")

                subtechnique_entries = mitre.get_subtechniques_of_technique(technique.id)

                subtechniques = []
                for entry in subtechnique_entries:
                    sub = entry["object"]
                    sub_id = mitre.get_attack_id(sub.id)
                    subtechniques.append((sub_id, sub))

                # Sort subtechniques
                subtechniques.sort()

                # Write each subtechnique with full detail
                for sub_id, sub in subtechniques:

                    # Title
                    tf.write(f"### {sub_id}: {sub.name}\n\n")

                    # Description
                    if hasattr(sub, "description"):
                        tf.write(f"{sub.description}\n\n")

                    # Properties
                    tf.write("#### Properties\n\n")
                    tf.write(f"- id: {sub_id}\n")
                    tf.write(f"- name: {sub.name}\n")

                    if hasattr(sub, "created"):
                        tf.write(f"- created: {sub.created}\n")

                    if hasattr(sub, "modified"):
                        tf.write(f"- modified: {sub.modified}\n")

                    if hasattr(sub, "type"):
                        tf.write(f"- type: {sub.type}\n")

                    if hasattr(sub, "x_mitre_version"):
                        tf.write(f"- x_mitre_version: {sub.x_mitre_version}\n")

                    if hasattr(sub, "x_mitre_domains"):
                        tf.write(f"- x_mitre_domains: {', '.join(sub.x_mitre_domains)}\n")

                    tf.write("\n")

            #endregion











            # Get subtechniques for this parent technique.
            # This returns a list of RelationshipEntry dicts, each with an "object" key
            # holding the subtechnique, and a "relationships" key with the STIX relationship.
            subtechnique_entries = mitre.get_subtechniques_of_technique(technique.id)

            # Build a list of (attack_id, subtechnique) tuples so we can sort by ID
            subtechniques = []
            for entry in subtechnique_entries:
                subtechnique = entry["object"]
                subtechnique_attack_id = mitre.get_attack_id(subtechnique.id)
                subtechniques.append((subtechnique_attack_id, subtechnique))

            # Sort subtechniques by their ATT&CK ID (e.g. T1134.001, T1134.002)
            subtechniques.sort()

            # Write each subtechnique as an indented bullet under its parent
            for subtechnique_attack_id, subtechnique in subtechniques:
                sub_safe_name = subtechnique.name.replace(" ", "_").replace("/", "_").lower()
                sub_link_name = f"{subtechnique_attack_id}-{sub_safe_name}"

                f.write(f"    - [[{sub_link_name}|{subtechnique_attack_id}: {subtechnique.name}]]\n")
        #endregion  

