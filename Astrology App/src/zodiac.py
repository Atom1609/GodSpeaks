def get_zodiac_sign(day, month):
    """Determine the zodiac sign based on the day and month."""
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 11 and day >= 29) or (month == 12 and day <= 17):
        return "Ophiuchus"  # Include the 13th sign
    else:
        return "Unknown"

def get_sign_traits(sign):
    """Return traits for a zodiac sign."""
    traits = {
        "Aries": "Bold and adventurous.",
        "Taurus": "Reliable and patient.",
        "Ophiuchus": "Spiritual and transformative."
    }
    return traits.get(sign, "Traits not available.")
