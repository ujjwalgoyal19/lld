class Location:
    def __init__(self, plot_no, street, city, state, country, zipcode, lat, lng):
        self.city = city
        self.state = state
        self.country = country
        self.address_string = plot_no + street + city + state + country + zipcode
        self.lat = lat
        self.lng = lng

    def get_coord(self):
        return self.lat, self.lng

    def get_address_string(self):
        return self.address_string
