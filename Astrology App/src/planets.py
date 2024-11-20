from skyfield.api import load
from datetime import datetime

def get_planet_positions():
    """Calculate today's planetary positions."""
    eph = load('de421.bsp')  # Download and place ephemeris in /data/ephemeris/
    ts = load.timescale()
    t = ts.now()
    planets = ['Sun', 'Moon', 'Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn']
    positions = {}

    for planet in planets:
        body = eph[planet]
        ra, dec, dist = body.at(t).radec()
        positions[planet] = f"RA: {ra.hours:.2f}h, Dec: {dec.degrees:.2f}°"

    return positions
