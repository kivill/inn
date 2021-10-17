FROM node:10-alpine

WORKDIR /app
COPY ./package.json ./
RUN npm install
COPY . .
ENV NODE_ENV production
EXPOSE 3041
CMD ["node", "index.js"]