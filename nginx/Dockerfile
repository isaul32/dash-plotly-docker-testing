FROM nginx:stable-alpine
COPY ./conf.d/ /etc/nginx/conf.d/
HEALTHCHECK CMD curl -f http://localhost/health || exit 1
