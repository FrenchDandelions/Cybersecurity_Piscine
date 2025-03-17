FROM nginx:1.27.1

RUN mkdir -p /srcs

RUN chmod 755 /srcs

RUN apt update -y && apt upgrade -y && apt install -y python

ENTRYPOINT [ "nginx", "-g", "daemon off;" ]