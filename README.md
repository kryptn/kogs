# kogs

Modify `environment` to make relevant:

* change `REMOTE_CONFIG` to your gogs address  
* change `DATABASE_CONFIG` to the relevant info

make sure you have docker and docker-compose installed

## Starting

    docker-compose up -d

## Stopping

    docker-compose stop

## Issues

* no ssh for gogs

## To Do

* automate gogs setup
* automate some env vars
* letsencrypt? ssl? i have nginx already, ssl would be easy
* squid to foward ssh? no clue on this one
