FROM python:3.7.6

WORKDIR /flask_regression
#sam dir on docker
ADD . /flask_regression

RUN apt-get update
RUN apt-get -y install libc-dev
RUN apt-get -y install build-essential
RUN pip install -U pip
RUN pip install -r requirements.txt

CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5000"]
CMD ["python","webapp.py"]