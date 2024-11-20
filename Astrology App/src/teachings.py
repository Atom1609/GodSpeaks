import json
from datetime import datetime

def load_daily_teaching():
    """Load today's teaching from the JSON database."""
    with open("data/teachings.json", "r") as file:
        teachings = json.load(file)
    
    today = datetime.now().strftime("%Y-%m-%d")
    for teaching in teachings:
        if teaching["date"] == today:
            return teaching
    
    # Default teaching if none is found
    return {
        "event": "General Reflection",
        "teaching": "Take time to reflect on your connection with the universe.",
        "practice": "Spend 5 minutes in silence, asking God to guide your thoughts."
    }
