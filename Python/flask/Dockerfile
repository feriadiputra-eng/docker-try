FROM python:slim

WORKDIR /app

copy . .

RUN pip install --upgrade pip && pip install -r requirements.txt

ENV FLASK_APP=server.py
ENV FLASK_ENV=production

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
