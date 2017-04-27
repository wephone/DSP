FROM ubuntu:14.04
RUN cd /
#ADD /home/wephone/DSP/webFreqz.py /DSP
RUN echo "deb http://mirrors.aliyun.com/ubuntu/ trusty main multiverse restricted universe" > /etc/apt/sources.list
RUN echo "deb http://mirrors.aliyun.com/ubuntu/ trusty-backports main multiverse restricted universe" >> /etc/apt/sources.list
RUN echo "deb http://mirrors.aliyun.com/ubuntu/ trusty-proposed main multiverse restricted universe" >> /etc/apt/sources.list
RUN echo "deb http://mirrors.aliyun.com/ubuntu/ trusty-security main multiverse restricted universe" >> /etc/apt/sources.list
RUN echo "deb http://mirrors.aliyun.com/ubuntu/ trusty-updates main multiverse restricted universe" >> /etc/apt/sources.list
RUN echo "deb-src http://mirrors.aliyun.com/ubuntu/ trusty main multiverse restricted universe" >> /etc/apt/sources.list
RUN echo "deb-src http://mirrors.aliyun.com/ubuntu/ trusty-backports main multiverse restricted universe" >> /etc/apt/sources.list
RUN echo "deb-src http://mirrors.aliyun.com/ubuntu/ trusty-proposed main multiverse restricted universe" >> /etc/apt/sources.list
RUN echo "deb-src http://mirrors.aliyun.com/ubuntu/ trusty-security main multiverse restricted universe" >> /etc/apt/sources.list
RUN echo "deb-src http://mirrors.aliyun.com/ubuntu/ trusty-updates main multiverse restricted universe" >> /etc/apt/sources.list
#RUN echo "" >> /etc/apt/sources.list
#RUN ping -c 10 baidu.com
#RUN ping -c 10 mirrors.aliyun.com
EXPOSE 5000:5000
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get -y install python3-pip
RUN pip3 install flask -i http://mirrors.aliyun.com/pypi/simple
RUN pip3 install numpy -i http://mirrors.aliyun.com/pypi/simple
RUN apt-get -y install libfreetype6-dev libxft-dev
RUN pip3 install matplotlib -i http://mirrors.aliyun.com/pypi/simple
RUN apt-get -y install libatlas-base-dev gfortran
RUN pip3 install scipy -i http://mirrors.aliyun.com/pypi/simple
RUN apt-get -y install git
RUN git clone https://github.com/wephone/DSP.git
#RUN python3 /DSP/webFreqz.py