# Given list of customer records
customers = [
    {"name": "Alice Johnson", "email": "alice@example.com"},
    {"name": "A. Johnson", "email": "alice@example.com"},
    {"name": "Bob Smith", "email": "bob@example.com"},
    {"name": "Robert Smith", "email": "bob@example.com"},
    {"name": "Charlie Reed", "email": "charlie@example.com"}
]

# Initializing dictionary for unique customers
unique_customers = {}  # Dictionary keyed by email

# Looping through customer records
for record in customers:
    email = record["email"]

    # Adding only first occurrence of each email
    if email not in unique_customers:
        unique_customers[email] = record  # Assigning the record

# Creating a deduplicated list
deduplicated_list = list(unique_customers.values())  # List of unique customer dictionaries