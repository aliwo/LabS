FROM python:3.7
MAINTAINER SeungWon "recordable0711@gmail.com"

COPY . /LabS
WORKDIR /LabS
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["gunicorn", "-w", "4", "--chdir", "/LabS/api", "app:app"]
