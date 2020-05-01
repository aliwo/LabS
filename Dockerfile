FROM python:3.7
MAINTAINER SeungWon "recordable0711@gmail.com"

COPY . /LabS
WORKDIR /LabS
RUN pip install -r requirements.txt
EXPOSE 8000

ENTRYPOINT ["gunicorn"]
CMD ["-w", "4", "-b", "0.0.0.0:8000", "--preload", "dummy:dummy_app"]
