# Используем официальный образ Apache Airflow
FROM apache/airflow:2.5.1

# Переключаемся на пользователя root для установки зависимостей системы
USER root

# Install OpenJDK-11
RUN apt-get update && apt-get install -y openjdk-11-jdk procps wget

# Set JAVA_HOME
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64
ENV PATH=$JAVA_HOME/bin/java

RUN wget -qO- https://downloads.apache.org/spark/spark-3.5.1/spark-3.5.1-bin-hadoop3.tgz | tar xvz -C /opt/ && \
    ln -s /opt/spark-3.5.1-bin-hadoop3 /opt/spark
ENV SPARK_HOME=/opt/spark
ENV PATH=$PATH:$SPARK_HOME/bin

#RUN export JAVA_HOME

# Переключаемся на пользователя airflow
USER airflow

COPY requirements.txt .
RUN pip install -r requirements.txt
