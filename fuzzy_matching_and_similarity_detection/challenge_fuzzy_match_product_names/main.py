from difflib import SequenceMatcher

# Official catalog names
catalog_names = ["Apple iPhone 14", "Samsung Galaxy S22", "Sony WH-1000XM5", "Dell Inspiron 15"]

# Incoming supplier names
incoming_names = ["Iphone14", "Galaxy S-22", "Sony 1000 XM5", "Dell Inspiron15"]

# Initializing the result dictionary
matched_products = {}

# Looping through incoming names
for name in incoming_names:
    best_match = None
    best_score = -1

    # Looping through catalog names
    for catalog_item in catalog_names:
        score = SequenceMatcher(None, name, catalog_item).ratio()

        if score > best_score:
            best_score = score
            best_match = catalog_item

    matched_products[name] = best_match

print(matched_products)