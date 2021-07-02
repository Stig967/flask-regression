from webapp import app, traffic_db
from flask import render_template, request, url_for, redirect
from models import Traffic
from predict import Predict
import forms

from datetime import datetime
from multiprocessing import Value
import logging
import time


counter = Value("i", 0)


@app.route("/predict", methods=["GET", "POST"])
def predict():
    # the endpoint has to take n previous values of the traffic to predict the new one
    # return 'Prediction result from the model'

    with counter.get_lock():
        counter.value += 1
        out = counter.value

    form = forms.PredictionRequestForm()
    if request.method == "POST":
        if form.is_submitted:
            # here look at last 10 seconds predition

            hits_per_sec_list = [
                record.per_sec_hits
                for record in traffic_db.session.query(Traffic).order_by(Traffic.id)
            ]
            date_list = [
                record.date
                for record in traffic_db.session.query(Traffic).order_by(Traffic.id)
            ]
            last_date = None
            predicted_val = None

            if len(hits_per_sec_list) > 9:  # minimal size of record is 10
                last_ten_records = hits_per_sec_list[-10:]
                last_date = date_list[-1]

                app.logger.info("Request for prediction was submitted.")
                app.logger.info(
                    "Database traffic.db content size {}: ".format(
                        len(hits_per_sec_list)
                    )
                )

                predictor = Predict()
                predicted_val = predictor.predict(last_date, last_ten_records)

            return render_template(
                "predict.html",
                form=form,
                for_now_hardcode=predicted_val,
                datetime_pred=last_date,
            )

    return render_template("predict.html", form=form)


@app.route("/metrics")
def metrics():
    # return 'Request per seconds to the /predict endpoint'

    all_traffic = Traffic.query.all()
    return render_template("metrics.html", traffic_list=all_traffic)


@app.route("/")
def main_page():
    app.logger.info("Flushing acutal database and prepare new.")
    traffic_db.session.query(Traffic).delete()
    traffic_db.session.commit()
    app.logger.info("Database clear.")
    for id in range(20):
        previous_hits = counter.value
        time.sleep(1)  # one second interval
        hits_in_interval = counter.value - previous_hits
        record = Traffic(per_sec_hits=hits_in_interval, date=datetime.utcnow())
        logging.debug(
            "Added record {} on time {}".format(record.per_sec_hits, record.date)
        )
        traffic_db.session.add(record)

    traffic_db.session.commit()
    app.logger.info("Database for metrics prepared.")
    return render_template("main_page.html")
