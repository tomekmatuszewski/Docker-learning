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

docker run -it --name my_container ubuntu                       -> run with name of container

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
        



------------------------------------------------------------------------------------------------------------------------------

Bash -> short reminder

echo 'new text' > my_data/new_file.txt                          -> simple method to write text in new file -> one line method
cat > my_data/new_file.txt                                      -> multiline text -> one line method
cat my_data/new_file.txt                                        -> read text from file
ls my_data                                                      -> list files in directory
echo $PWD                                                       -> write path to current dir
apt update && apt install nano -y                               -> update packages and install nano , yes for all steps