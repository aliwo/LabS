FROM python:3.7
MAINTAINER SeungWon "recordable0711@gmail.com"

COPY . /LabS
WORKDIR /LabS
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["gunicorn", "--workers=4", "'run:api'"]
