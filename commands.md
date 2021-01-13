docker pull 'image'                                         -> pull from docker repo hub.docker default :latesyt
docker images                                               -> images on local machine
docker pull ubuntu 'image:tag'                              -> docker pull ubuntu:18.04 -> specific version of image
docker rmi 'imagen:tag' | docker rmi 'IMAGE ID'             -> remove specific image
docker rmi 'image id' --force                               -> forcing removing image
docker 'command' help                                       -> help for command
docker rmi 'image1:tag' 'image2:tag' | 'image id'           -> removing multiple images
docker run 'image:tag'                                      -> run image
docker ps                                                   -> show run processes
docker ps -a                                                -> show all processes -> run and killed

docker run -it 'ubuntu:latest' bash                             -> run bash console from  -> exit -> exit form console
docker run -it python:3.8.3-slim-buster                         -> default python interpreter run -> exit()
docker run -it 'ubuntu:latest'                                  -> run ubuntu bash default
docker run -it python:3.8.3-slim-buster bash                    -> run bash with python

docker system prune                                             -> cleaning run killed containters
docker rm 'image1 id' 'image2 id'                               -> remove specific containers

docker run -it --name my_container ubuntu                       -> run with name of container -it (terminal of container)

docker stop                                                     -> stop of working container -> gracefull shutdown
docker kill 'name'                                              -> kill container

docker -it -v 'path to file':'path to file in container' 'image'  -> run image with munted disk resources
docker run -it -v$PWD/my_data:/my_data  ubuntu                  -> ubuntu with disk resources        
                                                                -> editing files on localhost -> mounted file in container is also edited ->  lineked files

docker run -it -v'path':'path' -p8000:8000 image                -> run on port 8000 image with mounted disk resources

-p localhost_post:port on container             

docker run -it -v $PWD/my_data:/my_data -p:8000:8000 python:3.8.3-slim-buster bash   -> with disk res on port 8000 run bash with python


docker run -it -p:8000:8000 python:3.8.3-slim-buster bash                            -> miking files in container -> serving on 8000
in bash # apt update && apt install nano -y
        # mkdir my_data
        # touch srv.py
        # touch index.html
        # nano srv.py -> write python script
        # nano index.html -> write python script
        # python srv.py -> serving on port 8000

docker image rm [OPTIONS] IMAGE [IMAGE...]                                           -> remove image
------------------------------------------------------------------------------------------------------------------------------
Build Dockerfiles

docker build -t tm/ubuntu-env .                                     -> build image based on dockerfile with tag (default latest version)
                                                                     context folder with dockerfile after tag (. - current dir)


docker build -t tm/ubuntu-env directory_with_dockerfile/  -> path to dockerfile if ofher name of dockefile 

docker build -t tm/ubuntu-env:0.0.1                                   -> with viersion nr 0.0.1

docker run -it tm/ubuntu-env:0.0.1 bash                               -> run built image -it -> bash

build based on specific Dockerfile in directory:

docker build -f dockerfiles/ubuntu_curl/Dockerfile-curl -t tm/ubuntu-env:0.0.2 . -> -f path to dockerfile / or Dockerfile_name . 
                                                                                        name of file and . as context -> maybe current dir

after change of dockerfile -> docker build ......

docker run -e CURL_HOST=https://wp.pl tm/ubuntu-env:0.0.1           -> run image with params env



WORKDIR name -> in Dockerfile making dir name and moving to them

ADD          -> add unpack tar from url           
COPY         -> copy file / dir  

EXPOSE 8000  -> put out port 8000

good pracice to kill container -> other terminal docker ps -> docker kill 

docker run -p8000:8000 --name pysrv -d tm/container:latest          ->  -d run as deamon (in background)

docker run -p5000:3000 --name blabla                                -> from port 3000 on port 5000

docker logs id / cont_name                                          -> get logs from container

docker logs -f pysrv                                                -> show logs during containe live


-----------------------------------------------------------------------------------------------------------------------------

Docker-compose


docker-compose build                                                -> building image based on docker-compose
docker-compose up                                                   -> run image 
docker-compose down                                                 -> removing container docker, network is cleaned
CRTL+C                                                              -> stopping without removing network

docker network ls                                                   -> networks available

docker exec -it src_api_1 bash                                      -> go to bash of existing container

after updating dockerfile -> docker-compose build context

docker-compose file                                                 -> .yml based on docker-compose.yml 
.env file in the same location as docker-compose                    -> store env variables

with mulitple services in one docker-compose                        -> docker-compose up name_service

docker-compose run --use-aliases api-test                           -> run container in -it mode used docker-compose



it is possible to send request to second container in the same network -> http://workdir:port/
--use-aliases                                                       -> possible to use workdir in path


overwirting of comments from docker run...................

depends on in yaml                                                  -> one service is waitng for other
------------------------------------------------------------------------------------------------------------------------------

Bash -> short reminder

echo 'new text' > my_data/new_file.txt                          -> simple method to write text in new file -> one line method
cat > my_data/new_file.txt                                      -> multiline text -> one line method
cat my_data/new_file.txt                                        -> read text from file
ls my_data                                                      -> list files in directory
echo $PWD                                                       -> write path to current dir
apt update && apt install nano -y                               -> update packages and install nano , yes for all steps
mv srv.py data                                                  -> move file srv.py to data directory
cp -r path_to_dir path_to_dir                                   -> copy directory
cd -                                                            -> go to previous localization
