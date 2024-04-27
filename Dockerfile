from hugomods/hugo
COPY . /src
WORKDIR /src
RUN [[ -f package-lock.json || -f npm-shrinkwrap.json ]] && npm ci || true
ENTRYPOINT ["/bin/sh", "./startup.sh"]