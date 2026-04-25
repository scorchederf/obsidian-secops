def make_safe_name(name):
    safe = str(name)
    for old, new in [(" ", "_"), ("/", "_"), ("\\", "_")]:
        safe = safe.replace(old, new)
    for char in [":", "?", '"', "*", "|", "<", ">"]:
        safe = safe.replace(char, "")
    return safe.strip("._").lower()
