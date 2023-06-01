FROM ubuntu:latest

# Instala las dependencias necesarias para Checkmk
RUN apt-get update && apt-get install -y wget

# Descarga el paquete de instalación de Checkmk desde el sitio oficial
RUN wget -O checkmk.deb "https://checkmk.com/support/2.0.0p6/check-mk-raw-2.0.0p6_0.bionic_amd64.deb"

# Instala el paquete de Checkmk
RUN dpkg -i checkmk.deb && rm checkmk.deb

# Expone el puerto necesario para acceder a la interfaz web de Checkmk (por ejemplo, el puerto 5000)
EXPOSE 5000

# Configura y realiza cualquier otro paso necesario para Checkmk

# Define el comando de inicio del servicio Checkmk
CMD ["omd", "start"]
