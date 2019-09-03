docker build -t registry.heroku.com/simple-cat-or-dog/web .
heroku login
heroku container:login
docker push registry.heroku.com/simple-cat-or-dog/web
heroku container:release web -a simple-cat-or-dog