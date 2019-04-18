FROM library/python:2


WORKDIR /opt
COPY requirements.txt /opt/requirements.txt

RUN pip install -r requirements.txt

COPY . /opt/

CMD ["python", "app.py"]