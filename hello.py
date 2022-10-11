from InquirerPy import prompt

import os

git_url = "https://github.com/kitfactory/hello_py.git"

basename = os.path.basename(git_url)
project = basename[:-4]
print(project)

dockerfile_str = []

cuda_question = [
    {
        "type": "list",
        "message": "Select CUDA version:",
        "choices": ["CUDA 11.2", "CUDA 10.2" ],
        "default": "CUDA 11.2",
        # "multiselect": True,
    }]
cuda_answer = prompt(cuda_question)

python_question = [
        {
            "type": "list",
            "message": "Select Python version:",
            "choices": ["Python 3.9", "Python 3.8", "Python 3.7", "None" ],
            "default": None,
        # "multiselect": True,
        }
    ]
python_answer = prompt(python_question)

if python_answer[0] == 'None':
    enable_python = False
else:
    enable_python = True

tz_question = [
        {
            "type": "list",
            "message": "Select Your Timezone:",
            "choices": ["Asia/Tokyo", "Europe/London", "Europe/Paris", "America/New_York"],
            "default": "Asia/Tokyo",
            # "multiselect": True,
        }
    ]
tz_answer = prompt(tz_question)

git_question =[
        {
            "type": "input",
            "message": "Input url of the git repository, if you use git repo :",
            "default": '',
            # "multiselect": True,            
        }
    ]
git_answer = prompt(git_question)

git_answer[0]=git_url

def build_dockerfile():
    print( cuda_answer[0])

    if git_answer[0] != '':
        enable_git = True
    else:
        enable_git = False
    print("enable_git" , enable_git)

    if cuda_answer[0] == 'CUDA 11.2':
        dockerfile_str.append('FROM nvidia/cuda:11.2.0-cudnn8-devel-ubuntu20.04')
    else:
        dockerfile_str.append( 'FROM nvidia/cuda:10.2-cudnn8-devel-ubuntu18.04' )

    dockerfile_str.append("ENV TZ=" + tz_answer[0])
    dockerfile_str.append("RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone")

    dockerfile_str.append("RUN apt-get update -y")
    dockerfile_str.append("RUN apt-get upgrade -y")
    dockerfile_str.append("RUN apt-get install -y git")

    if enable_python:
        dockerfile_str.append("RUN apt-get install -y build-essential libssl-dev zlib1g-dev \\")
        dockerfile_str.append("\tlibbz2-dev libreadline-dev libsqlite3-dev curl llvm \\")
        dockerfile_str.append("\tlibncursesw5-dev tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev libopencv-dev")
        dockerfile_str.append("RUN git clone https://github.com/pyenv/pyenv.git /home/.pyenv")
        dockerfile_str.append("RUN echo 'eval \"$(pyenv init -)\"' >> ~/.bashrc")

        dockerfile_str.append("ENV PYENV_ROOT /home/.pyenv")
        dockerfile_str.append("ENV PATH /home/.pyenv/bin:$PATH")
        dockerfile_str.append("ENV PATH /home/.pyenv/shims:$PATH")

        if python_answer[0] == "Python 3.9":
            dockerfile_str.append("RUN pyenv install 3.9.14")
            dockerfile_str.append("RUN pyenv global 3.9.14")
        elif python_answer[0] =="Python 3.8":
            dockerfile_str.append("RUN pyenv install 3.8.14")
            dockerfile_str.append("RUN pyenv global 3.8.14")
        elif  python_answer[0] =="Python 3.7":
            dockerfile_str.append("RUN pyenv install 3.7.14")
            dockerfile_str.append("RUN pyenv global 3.7.14")


    if enable_git:
        project = os.path.basename(git_answer[0])[:-4]
        dockerfile_str.append("ENV PROJECT " + project )
        dockerfile_str.append("RUN git clone " + git_answer[0])
        dockerfile_str.append("WORKDIR $PROJECT")
        dockerfile_str.append("RUN pip install -r requirements.txt")

    dockerfile_str.append( 'CMD ["python" , "--version"]')


build_dockerfile()
with open("Dockerfile", mode="w", encoding="utf8") as dockerfile:

    for l in dockerfile_str:
        dockerfile.write(l)
        dockerfile.write("\n")

exit()

questions = [
    {
        "type": "list",
        "message": "Select CUDA version:",
        "choices": ["CUDA 11.2", "CUDA 10.2" ],
        "default": None,
        # "multiselect": True,
    },
    {
        "type": "list",
        "message": "Select Python version:",
        "choices": ["Python 3.9", "Python 3.8", "Python 3.7" ],
        "default": None,
        # "multiselect": True,
    },
    {
        "type": "input",
        "message": "Input url of the git repository :",
        "default": '',
        # "multiselect": True,
    },
    {
        "type": "input",
        "message": "Input start up command (Default None):",
        "default": '',
        # "multiselect": True,
    }
]

answers = prompt(questions)
print(answers)




s = ''

if answers[0] == 'CUDA 11.2':
    print( "CUDA 11.2")
    s = 'FROM nvidia/cuda:11.2.0-cudnn8-devel-ubuntu20.04\n'
else:
    s = 'FROM nvidia/cuda:11.2.0-cudnn8-devel-ubuntu20.04\n'
    print( "CUDA 10.2")


# docker run -p 9000:9000 -p 9090:9090 --name minio1 -e "MINIO_ROOT_USER=ROOTUSER" -e "MINIO_ROOT_PASSWORD=CHANGEME123" -v ./data quay.io/minio/minio server /data --console-address ":9090"
