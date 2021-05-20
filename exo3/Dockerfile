FROM python:3.8.10-alpine3.13

EXPOSE 5000

WORKDIR /app

COPY install.txt .
RUN pip install -r install.txt

COPY app.py .

CMD python app.py
