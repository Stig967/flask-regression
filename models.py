from webapp import traffic_db


class Traffic(traffic_db.Model):
    id = traffic_db.Column(traffic_db.Integer, primary_key=True)
    per_sec_hits = traffic_db.Column(traffic_db.Integer, nullable=False)
    date = traffic_db.Column(traffic_db.DateTime, nullable=False)

    def __repr__(self):
        return (
            f'{self.per_sec_hits} ceated on {self.date.strftime("%Y-%m-%d %H:%M:%S")}'
        )
