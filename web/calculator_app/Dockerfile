FROM node:alpine

WORKDIR /opt/app
COPY package.json package.json

RUN yarn

COPY index.js index.js
COPY index.html index.html
COPY flag.txt flag.txt

RUN mv flag.txt /flag.txt \
  && chmod 444 /flag.txt \
  && chmod 444 ./index.js
USER node

CMD node index.js
