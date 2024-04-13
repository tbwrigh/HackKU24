FROM node:20-alpine

WORKDIR /app

COPY . .

RUN npm install

ARG VITE_BACKEND_URL

ENV VITE_BACKEND_URL=$VITE_BACKEND_URL

RUN npm run build

EXPOSE 8080

CMD ["npm", "run", "preview"]