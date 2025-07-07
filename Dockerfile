FROM redhat/ubi8
RUN yum install python3 -y && pip3 install flask -y
COPY app.py /app.py
CMD ["python3","app.py"]
