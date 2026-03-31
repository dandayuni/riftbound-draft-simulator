import json

# Card Class
class Card:
    def __init__(self, name, rarity, card_type, domain, set_name=None):
        self.name = name
        self.rarity = rarity
        self.card_type = card_type
        self.domain = domain
        self.set_name = set_name

    def __repr__(self):
        return f"{self.name}"


# Card Loader
def load_cards(filepath):
    with open(filepath, "r") as f:
        data = json.load(f)

    cards = []

    for card_data in data:
        card = Card(
            name=card_data["name"],
            rarity=card_data["rarity"],
            card_type=card_data["type"],
            domain = card_data["domain"],
            set_name=card_data.get("set")
        )
        cards.append(card)

    return cards