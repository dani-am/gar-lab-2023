FROM ubuntu:20.04

# Instalación de dependencias necesarias
RUN apt-get update && apt-get install -y \
    docker.io \
    apt-transport-https \
    curl \
    iptables

# Instalación de Kubernetes
RUN curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
RUN echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | tee /etc/apt/sources.list.d/kubernetes.list
RUN apt-get update && apt-get install -y \
    kubelet \
    kubeadm \
    kubectl

# Configuración de iptables
RUN modprobe br_netfilter
RUN echo "br_netfilter" >> /etc/modules-load.d/k8s.conf
RUN echo "net.bridge.bridge-nf-call-iptables=1" >> /etc/sysctl.conf
RUN sysctl -p

# Copia de los archivos necesarios para iKubernetes al contenedor
COPY cluster.yaml /app/cluster.yaml

# Configuración del entorno de Kubernetes en el contenedor
ENV KUBECONFIG=/app/config

# Comando por defecto para el contenedor
CMD ["/bin/bash"]
