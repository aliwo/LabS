FROM python:3.7
MAINTAINER SeungWon "recordable0711@gmail.com"

COPY . /LabS
WORKDIR /LabS
RUN pip install -r requirements.txt
EXPOSE 8000

# cmd 명령은 docker container run 시에 덮어 쓸 수 있습니다. 따라서 ENTRYPOINT 에는 원하는 명령어를,
# cmd 에는 명령어의 인수를 지정하면 나중에 run 할 때 인수를 바꿔칠 수 있습니다.
# docker container run -it triumph1/lab_s -w 10 # worker 가 10개가 됩니다.
ENTRYPOINT ["/LabS/entrypoint.sh"]
CMD ["-w", "4", "-b", "0.0.0.0:8000", "--chdir", "/LabS/api", "app:app"]
