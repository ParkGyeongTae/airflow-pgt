FROM ubuntu:18.04
LABEL maintainer "ParkGyeongTae"

# apt 설치시 입력요청 무시
ENV DEBIAN_FRONTEND=noninteractive

# 가끔 구글 프록시 엇갈리는 문제
# RUN set -x \
# && { \
# echo 'Acquire::http::Pipeline-Depth 0;'; \
# echo 'Acquire::http::No-Cache true;'; \
# echo 'Acquire::BrokenProxy    true;'; \
# } > /etc/apt/apt.conf.d/99fixbadproxy

# apt 미러서버 미국(default) -> 한국 변경
RUN sed -i 's@archive.ubuntu.com@kr.archive.ubuntu.com@g' /etc/apt/sources.list

# 자주 사용하는 패키지 설치
RUN apt-get update && \
    apt-get install net-tools -y && \
    apt-get install iputils-ping -y && \
    apt-get install vim -y && \
    apt-get install wget -y

WORKDIR /home

# python 3.8.0
RUN apt-get install python3.8 -y && \
    apt-get install python3-pip -y && \
    rm -rf /usr/bin/python3 && \
    ln -s /usr/bin/python3.8 /usr/bin/python && \
    ln -s /usr/bin/python3.8 /usr/bin/python3

# pip3 설정 및 pip3 버전 업데이트 (22.0.4)
RUN mkdir /root/.pip && \
    set -x \
    && { \
    echo '[global]'; \
    echo 'timeout = 60'; \
    echo '[freeze]'; \
    echo 'timeout = 10'; \
    echo '[list]'; \
    echo 'format = columns'; \
    } > /root/.pip/pip.conf && \
    pip3 install --upgrade pip

# 로케일 설정
ENV LC_ALL=C.UTF-8

# # 필요한 패키지 설치
COPY ./airflow/airflow-conf/requirements.txt /home/requirements.txt
RUN pip3 install -r /home/requirements.txt

# airflow 설정파일 옮기기
RUN rm -rf /usr/local/lib/python3.8/dist-packages/airflow/config_templates/default_airflow.cfg && \
    mkdir /home/dags && \
    mkdir /home/logs
COPY ./airflow/airflow-conf/airflow.cfg /usr/local/lib/python3.8/dist-packages/airflow/config_templates/default_airflow.cfg

# dag 로컬과 연동
COPY ./airflow/airflow-dags /home/dags

RUN mkdir /home/code
COPY ./airflow/airflow-code /home/code

# entrypoint 파일 옮기기
COPY ./airflow/airflow-entrypoint/entrypoint-airflow.sh /usr/local/bin/

# EXPOSE 8080

# ENTRYPOINT entrypoint-airflow.sh