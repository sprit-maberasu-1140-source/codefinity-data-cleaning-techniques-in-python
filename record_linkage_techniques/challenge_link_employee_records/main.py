from difflib import SequenceMatcher

df1 = [
    {"first_name": "Alice", "last_name": "Johnson", "city": "New York"},
    {"first_name": "Bob", "last_name": "Smith", "city": "Boston"},
    {"first_name": "Charlie", "last_name": "Reed", "city": "Seattle"}
]

df2 = [
    {"first_name": "Alicia", "last_name": "Jonson", "city": "NewYork"},
    {"first_name": "Robert", "last_name": "Smyth", "city": "Bostn"},
    {"first_name": "Charley", "last_name": "Reid", "city": "Seatle"}
]

linked_records = []

for idx1, emp1 in enumerate(df1):
    key1 = (
        emp1["first_name"].lower() + " " +
        emp1["last_name"].lower() + " " +
        emp1["city"].lower()
    )

    for idx2, emp2 in enumerate(df2):
        key2 = (
            emp2["first_name"].lower() + " " +
            emp2["last_name"].lower() + " " +
            emp2["city"].lower()
        )

        score = SequenceMatcher(None, key1, key2).ratio()

        if score >= 0.80:
            linked_records.append({
                "index_df1": idx1,
                "index_df2": idx2,
                "similarity": score
            })