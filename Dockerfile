FROM hugomods/hugo:exts-0.140.2
COPY . /src
WORKDIR /src
RUN [[ -f package-lock.json || -f npm-shrinkwrap.json ]] && npm ci || true
ENTRYPOINT ["/bin/sh", "./startup.sh"]