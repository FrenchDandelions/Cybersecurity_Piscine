FROM nginx:1.27.1

COPY ./srcs/nginx.conf /etc/nginx/nginx.conf

COPY ./srcs/index.html /usr/share/nginx/html

RUN apt install apt-transport-https

RUN cat /etc/debian_version

RUN echo "\
    Types: deb deb-src\
    Components: main\
    Suites: bookworm\
    URIs: tor+http://apow7mjfryruh65chtdydfmqfpj5btws7nbocgtaovhvezgccyjazpqd.onion/torproject.org\
    Architectures: amd64 arm64 i386\
    Signed-By: /usr/share/keyrings/deb.torproject.org-keyring.gpg\
    " | tee -a /etc/apt/sources.list.d/tor.sources > /dev/null

RUN apt update -y && apt list --upgradable && apt install -y tor systemctl

COPY ./srcs/torrc /etc/tor/torrc

RUN systemctl start tor

RUN rm -rf /etc/nginx/sites-enabled/default

ENTRYPOINT ["nginx", "-g", "daemon off;"]