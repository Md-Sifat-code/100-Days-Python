travel_log = [
    {
        "country": "Bangladesh",                # First dictionary in the list
        "cities_visited": ["Paris", "Lille", "Dijon"],  # Nested list within dictionary
        "total_visits": 12
    },
    {
        "country": "France",                    # Second dictionary in the list
        "cities_visited": ["Berlin", "West Ham", "Brasil", "Portugal"],
        "total_visits": 5
    }
]

add_new_country ={
    "Country":"Russia",
    "cities_visited": ["Dhaka","Bangladesh","Singa","Motherland"],
    "total_visited":8
}

travel_log.append(add_new_country)
print(f"{travel_log} \n")