FROM ubuntu:18.04
LABEL maintainer "ParkGyeongTae"

# apt 설치시 입력요청 무시
ENV DEBIAN_FRONTEND=noninteractive

# apt 미러서버 미국(default) -> 한국 변경
RUN sed -i 's@archive.ubuntu.com@kr.archive.ubuntu.com@g' /etc/apt/sources.list

WORKDIR /home

# 자주 사용하는 패키지 설치
RUN apt-get update && \
    apt-get install net-tools -y && \
    apt-get install iputils-ping -y && \
    apt-get install vim -y && \
    apt-get install wget -y

# PostgreSQL 설치 (12.10)
RUN apt-get install gnupg -y && \
    echo "deb http://apt.postgresql.org/pub/repos/apt/ bionic-pgdg main" | tee /etc/apt/sources.list.d/pgdg.list && \
    wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - && \
    apt-get update && \
    apt-get install postgresql-12 -y && \
    apt-get install sudo -y

# postgresql 기존 설정파일 제거
RUN rm -rf /etc/postgresql/12/main/postgresql.conf && \
    rm -rf /etc/postgresql/12/main/pg_hba.conf

# postgresql 설정파일 옮기기
COPY ./postgresql-airflow/postgresql-airflow-conf/postgresql.conf /etc/postgresql/12/main/postgresql.conf
COPY ./postgresql-airflow/postgresql-airflow-conf/pg_hba.conf /etc/postgresql/12/main/pg_hba.conf

# postgresql 설정파일 권한 수정
RUN chown postgres:postgres /etc/postgresql/12/main/postgresql.conf && \
    chown postgres:postgres /etc/postgresql/12/main/pg_hba.conf

# entrypoint 파일 옮기기
COPY ./postgresql-airflow/postgresql-airflow-entrypoint/entrypoint-postgresql.sh /usr/local/bin/

ENTRYPOINT ["entrypoint-postgresql.sh"]