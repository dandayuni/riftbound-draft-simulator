from draft.card import load_cards

cards = load_cards("card-data/cards.json")

for card in cards:
    print(card)