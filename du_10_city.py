class City:
    def __init__(self, name, region, country, citizens, zipcode, areacode):
        self.name = name
        self.region = region
        self.country = country
        self.citizens = citizens
        self.zipcode = zipcode
        self.areacode = areacode

    def get_props(self):
        return(self.name, self.region, self.country, self.citizens, self.zipcode, self.areacode)
    def print_props(self):
        print(f"""city: {self.name} 
region: {self.region}
country: {self.country}
citizens: {self.citizens}
zipcode: {self.zipcode}
areacode: {self.areacode}
              """)

this_city = City(name = "IpD", region="BSK", country="SK",citizens="10000",zipcode="90028",areacode=None)

print(this_city.get_props())
this_city.print_props()