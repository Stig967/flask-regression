import xgboost as xg
import numpy as np
from webapp import app


# This class should to be modified to improve code quality and logis
class Predict:
    def __init__(self):
        # Create and load model in to memory
        self.xgb_r = xg.XGBRegressor()
        self.xgb_r.load_model("prediction.model")

    # Example usage:
    #
    # import random
    # print(Predict().predict(datetime.now(), [random.randint(0,100) for x in range(10)]))
    #

    def predict(self, date, lastValues):
        assert len(lastValues) == 10, "model expects exactly 10 last reads"
        formattedDate = [date.day, date.hour, date.minute, date.weekday()]

        app.logger.info(
            "Prediction based on traffic from last 10 seconds on endpoint {}, values: {} ".format(
                "/prediction", lastValues
            )
        )
        app.logger.info("Last record time: {}".format(date))
        app.logger.info(
            "Final value passed to XGBRegressor: {}".format(
                [formattedDate + lastValues]
            )
        )

        return self.xgb_r.predict(np.array([formattedDate + lastValues]))[0]
