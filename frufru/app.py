import falcon

from frufru.resources import CarResource, RateResource, PopularResource


app = application = falcon.App()

cars = CarResource()
rate = RateResource()
popular = PopularResource()

app.add_route("/cars", cars)
app.add_route("/rate", rate)
app.add_route("/popular", rate)
