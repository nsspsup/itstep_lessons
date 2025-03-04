import pickle


class Country():
    def __init__(self):
    # Dictionary to store country-capital data
        self.country_capitals = {}


    def add_country(self,country, capital):
        self.country_capitals[country] = capital
        print(f"Added: {country} -> {capital}")


    def delete_country(self,country):
        if country in self.country_capitals:
            del self.country_capitals[country]
            print(f"Deleted: {country}")
        else:
            print(f"{country} not found.")


    def find_country(self,country):
        return self.country_capitals.get(country, "Not found")


    def edit_country(self,country, new_capital):
        if country in self.country_capitals:
            self.country_capitals[country] = new_capital
            print(f"Updated: {country} -> {new_capital}")
        else:
            print(f"{country} not found.")

    def show_all(self):
        for key,val in self.country_capitals.items():
            print(key,val)


    def save_data(self,filename="countries.pkl"):
        with open(filename, "wb") as file:
            pickle.dump(self.country_capitals, file)
        print("Data saved successfully.")


    def load_data(self,filename="countries.pkl"):
        try:
            with open(filename, "rb") as file:
                self.country_capitals = pickle.load(file)
            print("Data loaded successfully.")
        except FileNotFoundError:
            print("No saved data found.")


# Sample usage
if __name__ == "__main__":
    cntr = Country()
    while True:
        print("\nOptions: add, delete, find, edit, show_all, save, load, exit")
        action = input("Enter action: ").strip().lower()

        if action == "add":
            country = input("Enter country name: ")
            capital = input("Enter capital: ")
            cntr.add_country(country, capital)

        elif action == "delete":
            country = input("Enter country to delete: ")
            cntr.delete_country(country)

        elif action == "find":
            country = input("Enter country to find: ")
            print(f"Capital: {cntr.find_country(country)}")

        elif action == "edit":
            country = input("Enter country to edit: ")
            new_capital = input("Enter new capital: ")
            cntr.edit_country(country, new_capital)

        elif action == "show_all":
            cntr.show_all()

        elif action == "save":
            cntr.save_data()

        elif action == "load":
            cntr.load_data()

        elif action == "exit":
            print("Exiting program.")
            break

        else:
            print("Invalid action, please try again.")
