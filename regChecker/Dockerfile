FROM tiangolo/uwsgi-nginx:python3.8-alpine
WORKDIR /app
COPY . /app
COPY . .
EXPOSE 3042
ENTRYPOINT [ "python" ]
CMD [ "flask_app.py" ]