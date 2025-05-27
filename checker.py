def assess_claim_viability(estimate, deductible, damage_type, days_since_damage):
    messages = []

    if estimate < deductible * 1.25:
        messages.append("⚠️ Damage may not exceed deductible. Filing might not be worth it.")
    else:
        messages.append("✅ Damage likely exceeds deductible. Filing may be valid.")

    if damage_type.lower() in ["hail", "fire", "water"]:
        messages.append(f"💡 {damage_type.title()} claims are often covered.")
    else:
        messages.append("ℹ️ Coverage may depend on your policy wording.")

    if days_since_damage > 90:
        messages.append("⚠️ Claims older than 90 days may be denied due to late reporting.")

    return "\n".join(messages)
