FROM nvidia/cuda:11.2.0-cudnn8-devel-ubuntu20.04
ENV TZ=Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y git
RUN apt-get install -y build-essential libssl-dev zlib1g-dev \
	libbz2-dev libreadline-dev libsqlite3-dev curl llvm \
	libncursesw5-dev tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev libopencv-dev
RUN git clone https://github.com/pyenv/pyenv.git /home/.pyenv
RUN echo 'eval "$(pyenv init -)"' >> ~/.bashrc
ENV PYENV_ROOT /home/.pyenv
ENV PATH /home/.pyenv/bin:$PATH
ENV PATH /home/.pyenv/shims:$PATH
RUN pyenv install 3.9.14
RUN pyenv global 3.9.14
ENV PROJECT hello_py
RUN git clone https://github.com/kitfactory/hello_py.git
WORKDIR $PROJECT
