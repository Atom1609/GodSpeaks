from zodiac import get_zodiac_sign, get_sign_traits

def generate_daily_horoscope(user, planetary_positions):
    """Generate a personalized horoscope."""
    zodiac_sign = get_zodiac_sign(user['birth_day'], user['birth_month'])
    traits = get_sign_traits(zodiac_sign)
    
    horoscope = (
        f"Hello, {user['name']}! As a {zodiac_sign}, you are known for being {traits}. "
        f"Today's planetary influences are as follows:\n"
    )
    
    for planet, position in planetary_positions.items():
        horoscope += f"- {planet}: {position}\n"

    horoscope += "Make the most of today's celestial energy!"
    return horoscope
