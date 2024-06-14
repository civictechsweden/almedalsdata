import json
import scrapers.almedalsveckan_info as ai
from services.writer import Writer

ONLY_REFETCH_CURRENT_YEAR = True
CURRENT_YEAR = ai.AVAILABLE_YEARS[-1]

all_events = []

for year in ai.AVAILABLE_YEARS:
    events = []

    if ONLY_REFETCH_CURRENT_YEAR and year != CURRENT_YEAR:
        print(f"Loading {year} from file...")
        with open(f"{year} - events.json") as file_json:
            events = json.load(file_json)
    else:
        print(f"Downloading {year} from source...")
        for type in ai.AVAILABLE_TYPES:
            print(f"Fetching {type} events for {year}...")
            type_events = ai.get_detailed_list(year, type)
            filename = f"{year} - {type}"

            if type_events:
                Writer.write_csv(type_events, filename + ".csv")
                Writer.write_json(type_events, filename + ".json")

                events.extend(type_events)

        Writer.write_csv(events, f"{year} - events.csv")
        Writer.write_json(events, f"{year} - events.json")

    all_events.extend([ai.reduce_event(event) for event in events])

if all_events:
    Writer.write_csv(all_events, "summary.csv")
    Writer.write_json(all_events, "summary.json")
