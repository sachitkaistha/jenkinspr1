FROM redhat/ubi8
RUN yum install -y python3 python3-pip && python3 -m pip install flask
COPY app.py /app.py
CMD ["python3","app.py"]
