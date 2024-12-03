FROM python:3.11-alpine
WORKDIR /src
ENTRYPOINT ["python", "-m"]

# Just be lazy and copy everything
COPY . .

# Install all the plugins
RUN pip install brewtils
RUN find . -maxdepth 1 -type d ! -name ".*" -not -name "autobrew" -not -name "echo-http-server" | xargs pip install --no-cache-dir
