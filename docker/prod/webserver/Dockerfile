FROM node:23-alpine3.19 as build-stage

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build --omit=dev


FROM nginx:alpine

COPY nginx.conf /etc/nginx.conf

COPY --from=build-stage /app/dist /usr/share/nginx/html

COPY resume.pdf /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]