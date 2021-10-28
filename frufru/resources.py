import socket

import falcon
import requests
from sqlalchemy.exc import IntegrityError

from frufru import models

# move that part to the validation step
VEHICLES_API = "https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{}?format=json"
TIMEOUT = 5


class CarResource:
    def on_get(self, req, resp):
        # model_list = models.Car.get_list(self.db.session)
        # cars = [model.as_dict for model in model_list]

        resp.status = falcon.HTTP_200
        # resp.media = cars

    def on_post(self, req, resp):
        make = req.media.get("make")
        model = req.media.get("model")

        # cache response?
        resp = requests.get(VEHICLES_API.format(make), timeout=TIMEOUT)

        if resp.status_code != 200:
            raise Exception("Wrong API response code")

        all_models = [m["Model_Name"].lower() for m in resp.json()["Results"]]

        if model.lower() not in all_models:
            raise Exception(f"Model {model} does not exist for make {make}")

        car = models.Car(make=make, model=model)
        # try:
        #     model.save(self.db.session)

        # except IntegrityError:
        #     raise falcon.HTTPBadRequest(
        #         "Car exists! Could not create car due to model already existing!"
        #     )

        print(car)

        resp.status = falcon.HTTP_201
        resp.media = {"id": model.id}

    def on_delete(self, req, resp):
        pass


class RateResource:
    def on_post(self, req, resp):
        model = models.Rate(mark=req.media.get("mark"), car_id=req.media.get("car_id"))
        model.save(self.db.session)

        resp.status = falcon.HTTP_201
        resp.media = {"id": model.id}


class PopularResource:
    def on_get(self, req, resp):
        car_id = req.media.get("car_id")

        return car_id
