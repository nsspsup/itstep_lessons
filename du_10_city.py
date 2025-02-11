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

class otherCity(City):
    def __init__(self, name, region, country, citizens, zipcode, areacode, pubs):
        super.__init__(name, region, country, citizens, zipcode, areacode)
        self.pubs = pubs

        def get_props(self):
            return super().get_props() + (self.pubs)

this_city = City(name = "IpD", region="BSK", country="SK",citizens=10000,zipcode=90028,areacode=None)
HornaDolna = otherCity(name = "HornaDolna", region="unknown", country="SK",citizens=5.5,zipcode=12345, areacode=None, pubs=1 )



print(this_city.get_props())
this_city.print_props()
print(HornaDolna.__getattribute__("pubs"))

