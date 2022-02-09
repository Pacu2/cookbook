FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /cookbook
COPY requirements.txt /cookbook/
RUN pip install -r requirements.txt
COPY . /cookbook/