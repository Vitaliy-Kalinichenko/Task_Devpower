<!--
title: 'API for parser'
layout: Doc
language: python
authorLink: 'https://github.com/Vitaliy-Kalinichenko'
authorName: 'Kalinichenko Vitaliy'
-->

# Service that stores data on the population of countries in postgres

This is a service running through docker-compose that stores the population of countries in postgres and displays the
summary data by region on the screen.

Data source: table on page https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population

## Deployment

To clone the repository from github and go to your project folder, run this commandы in your terminal:

```
$ git clone ...
$ cd ...
```

In folder of project, rename the ```env.exe``` file to ```.env```, after which we fill in the environment variables
necessary for deployment

```
POSTGRES_USER=your_username
POSTGRES_PASSWORD=your_password
POSTGRES_DB=data_base_name
POSTGRES_HOST='db'
POSTGRES_PORT='5432'
```

Launching the deployment app

```
$ docker-compose up get_data 
$ docker-compose up print_data
```
