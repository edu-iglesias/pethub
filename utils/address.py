
def get_full_address(address1, address2, city, state, country):
    full_address = ""

    if address1:
        full_address += address1
        full_address += " "

    if address2:
        full_address += address2
        full_address += " "

    if city:
        full_address += city
        full_address += " "

    if state:
        full_address += state
        full_address += " "

    if country:
        full_address += country
        full_address += " "

    return full_address
