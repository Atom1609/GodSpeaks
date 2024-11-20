from user_data import get_user_details
from horoscope import generate_daily_horoscope
from planets import get_planet_positions
from zodiac import get_zodiac_sign, get_sign_traits
from teachings import load_daily_teaching

def main():
    print("Welcome to the Astrology & Faith App!")
    
    # Step 1: Get user details
    user = get_user_details()
    
    # Step 2: Display today's planetary positions
    print("\nToday's Planetary Positions:")
    planetary_positions = get_planet_positions()
    for planet, position in planetary_positions.items():
        print(f"{planet}: {position}")
    
    # Step 3: Display daily teaching
    print("\nToday's Teaching:")
    teaching = load_daily_teaching()
    print(f"Event: {teaching['event']}")
    print(f"Teaching: {teaching['teaching']}")
    print(f"Practice: {teaching['practice']}")
    
    # Step 4: Generate and display daily horoscope
    print("\nYour Daily Horoscope:")
    horoscope = generate_daily_horoscope(user, planetary_positions)
    print(horoscope)

if __name__ == "__main__":
    main()
