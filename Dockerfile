FROM python:3.11-alpine
WORKDIR /src
ENTRYPOINT ["python", "-m"]

# Just be lazy and copy everything
COPY . .

# Install all the plugins
RUN pip install brewtils \
  && find . -maxdepth 1 -type d ! -name ".*" -not -name "autobrew" | xargs pip install --no-cache-dir
