FROM ubuntu:14.04
RUN cd /
#ADD /home/wephone/DSP/webFreqz.py /DSP
RUN echo "deb http://mirrors.aliyun.com/ubuntu/ trusty main multiverse restricted universe" > /etc/apt/sources.list \
    && echo "deb http://mirrors.aliyun.com/ubuntu/ trusty-backports main multiverse restricted universe" >> /etc/apt/sources.list \
    && echo "deb http://mirrors.aliyun.com/ubuntu/ trusty-proposed main multiverse restricted universe" >> /etc/apt/sources.list \
    && echo "deb http://mirrors.aliyun.com/ubuntu/ trusty-security main multiverse restricted universe" >> /etc/apt/sources.list \
    && echo "deb http://mirrors.aliyun.com/ubuntu/ trusty-updates main multiverse restricted universe" >> /etc/apt/sources.list \
    && echo "deb-src http://mirrors.aliyun.com/ubuntu/ trusty main multiverse restricted universe" >> /etc/apt/sources.list \
    && echo "deb-src http://mirrors.aliyun.com/ubuntu/ trusty-backports main multiverse restricted universe" >> /etc/apt/sources.list \
    && echo "deb-src http://mirrors.aliyun.com/ubuntu/ trusty-proposed main multiverse restricted universe" >> /etc/apt/sources.list \
    && echo "deb-src http://mirrors.aliyun.com/ubuntu/ trusty-security main multiverse restricted universe" >> /etc/apt/sources.list \
    && echo "deb-src http://mirrors.aliyun.com/ubuntu/ trusty-updates main multiverse restricted universe" >> /etc/apt/sources.list \
    && apt-get -y update \
    && apt-get -y upgrade \
    && apt-get -y install python3-pip \
    && pip3 install flask -i http://mirrors.aliyun.com/pypi/simple \
    && pip3 install numpy -i http://mirrors.aliyun.com/pypi/simple \
    && apt-get -y install libfreetype6-dev libxft-dev \
    && pip3 install matplotlib -i http://mirrors.aliyun.com/pypi/simple \
    && apt-get -y install libatlas-base-dev gfortran \
    && pip3 install scipy -i http://mirrors.aliyun.com/pypi/simple \
    && apt-get -y install git
#    不可以写很多个run 会造成容器的层级太多 导致镜像过大！
#RUN echo "" >> /etc/apt/sources.list
#RUN ping -c 10 baidu.com
#RUN ping -c 10 mirrors.aliyun.com
#RUN git clone https://github.com/wephone/DSP.git

EXPOSE 5000:5000
#RUN python3 /DSP/webFreqz.py