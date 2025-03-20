# FROM nginx:1.27.1

# RUN mkdir -p /srcs

# RUN chmod 755 /srcs

# RUN apt update -y && apt upgrade -y && \
#     apt install -y python3 python3-pip python3.11-venv python3-xyz

# WORKDIR /srcs

# RUN python3 -m venv myenv && . myenv/bin/activate

# RUN pip install --upgrade pip && pip install pycryptodome

# ENTRYPOINT [ "nginx", "-g", "daemon off;" ]

# Use the official Python image as a base
FROM python:3.11-slim

RUN mkdir -p /srcs

RUN mkdir -p /root/infection

COPY ./srcs/infection /root/infection

RUN chmod 755 /srcs

# Set up your working directory
WORKDIR /srcs

# Install dependencies inside the virtual environment
RUN pip install --upgrade pip && pip install pycryptodome

# Keep the container running (simple bash command)
CMD ["bash", "-c", "sleep infinity"]
