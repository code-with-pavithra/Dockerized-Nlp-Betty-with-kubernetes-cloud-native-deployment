FROM python:3.9.5-slim-buster

ADD . /app

WORKDIR /app

ENV GOOGLE_API_KEY="AIzaSyCA7wee7PKAGoT6YNQ-xQJT-TMvmMxbpj4"

RUN pip3 install -r requirements.txt

CMD ["streamlit", "run","app.py"]