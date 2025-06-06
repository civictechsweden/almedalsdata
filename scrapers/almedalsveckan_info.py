from services.downloader import Downloader

PROGRAM_2025 = "https://gotland.se/appresource/4.4e8c940c1946e1ba5811593f/12.4e8c940c1946e1ba581159d0/items?startDate=2025-06-23&endDate=2025-06-27&start="


def get_list():
    i = 0
    count = 30
    items = []

    while len(items) < count:
        response = Downloader.get_json(PROGRAM_2025 + str(i))
        if response["count"] != count:
            count = response["count"]
            print(f"Found {count} items")
        print(f"Fetching items {i + 1}-{(i + 30)}...")
        items.extend(response["items"])
        i += 30

    items = remove_empty_keys(items)
    items = clean_data(items)
    return items


def remove_empty_keys(data):
    # If it's a list, apply the function to each element
    if isinstance(data, list):
        return [remove_empty_keys(item) for item in data]

    # If it's a dictionary, filter the keys
    if isinstance(data, dict):
        return {k: remove_empty_keys(v) for k, v in data.items() if k != ""}

    # If it's neither a list nor a dictionary, return it as is
    return data


def clean_data(data):

    # If it's a list, apply the function to each element
    if isinstance(data, list):
        return [clean_data(item) for item in data]

    # If it's a dictionary, filter the keys and strip string values
    if isinstance(data, dict):
        return {
            k: clean_data(v)
            for k, v in data.items()
            if k != ""
            and k != "dateISO"
            and k != "url"
            and k != "weekDayName"
            and k != "shortDate"
            and (not isinstance(v, str) or v.strip())
        }

    # If it's a string, strip whitespace
    if isinstance(data, str):
        return data.strip()

    # If it's neither a list, dictionary, nor string, return it as is
    return data
