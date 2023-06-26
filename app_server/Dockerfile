FROM python:3.6-slim-buster

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y build-essential

# Copy the requirements file and install the dependencies
RUN apt-get update && apt-get install -y libssl-dev
RUN pip3 install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get install -y m4
RUN apt-get install -y flex
RUN apt-get install -y bison
RUN apt-get install -y wget
RUN apt-get install -y openssl
RUN pip3 install tk
RUN pip3 install "cryptography<4" pyOpenSSL pymongo
RUN pip3 install azure-keyvault-secrets 
RUN pip3 install azure-identity
RUN pip3 install tk
RUN pip3 install python-dotenv
RUN pip3 install gunicorn==20.1.0

# Copy the Charm Crypto source code
COPY charm-dev /app/charm
COPY gmp-6.2.1 /app/gmp
COPY pbc-0.5.14 /app/pbc

#build gmp
RUN cd /app/gmp && ./configure && make && make check && make install
#build pbc
RUN cd /app/pbc && ./configure && make && make install
# Build Charm Crypto
RUN cd /app/charm && ./configure.sh && make && make install
RUN apt-get -y update && apt-get -y upgrade
# Copy the source code
COPY . .
# Expose the port for the Flask app
EXPOSE 8000
# Use a production-ready web server
CMD ["gunicorn", "app:app",  "--bind", "0.0.0.0:8000"]
