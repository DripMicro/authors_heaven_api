FROM nginx:1.21.5-alpine
# We remove the default conf that comes with the images and replace it with ours
RUN rm /etc/nginx/conf.d/default.conf
COPY ./default.conf /etc/nginx/conf.d/default.conf