import csv
import json


class Writer(object):
    @staticmethod
    def write_csv(data: list, filename):
        keys = data[-1].keys()

        with open(filename, "w", newline="", encoding='utf-8') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(data)

    @staticmethod
    def write_json(data: list, filename):
        with open(filename, "w", encoding='utf-8') as fp:
            json_string = json.dumps(data, ensure_ascii=False, indent=4).encode("utf-8")
            fp.write(json_string.decode())

