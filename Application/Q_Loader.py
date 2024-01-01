import pandas as pd
import random

import args

class CountryDescriptionReader:
    def __init__(self, excel_path=args.QUESTION_FILE):
        self.df = pd.read_excel(excel_path)
        self.used_indices = set()

    def get_random_country_description(self):
        available_indices = list(set(self.df.index) - self.used_indices)

        if not available_indices:
            # Reset used indices if all records have been used
            self.used_indices = set()
            available_indices = list(self.df.index)

        random_index = random.choice(available_indices)
        country_record = self.df.loc[random_index].to_dict()

        # Mark the index as used
        self.used_indices.add(random_index)

        return country_record

    def clear_previous_selections(self):
        self.used_indices = set()


if __name__ == "__main__":
    country_reader = CountryDescriptionReader()

    test_record_1 = country_reader.get_random_country_description()
    print(test_record_1['Country Code'])
    print(test_record_1['Description'])
    print(test_record_1['Emojis'])

    test_record_2 = country_reader.get_random_country_description()
    print(test_record_2)

    country_reader.clear_previous_selections()

