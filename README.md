Academic staff assessment 
===

## Introduction

This repository contains software project of our team. The idea is to replace google forms with something more manageble, with better statistics, easier for students and professors to use. We decided to use django for backend and bootstrap for frontend. 

## To run

It is already running on [heroku](https://anonymous-feedback-swp.herokuapp.com/). However, if you want to test it in localhost, you can just go to the `Academic-staff-assesment` submodule and use `docker-compose`. In this case you will need to run `docker exec -it django bash` and then create admin
with `python manage.py createsuperuser`. This admin account then can be used for CRUD surveys, however we are working now on writing our own admin panel. 

## Structure

In main repository here are all artifacts we've done this semster, as well as submodule, which Matvey uses to push to his heroku. In submodule there is a django application which consists of two apps: survey, which is definitely used to manage surveys, and students, which is now used only for student login, but later will be renamed and responsible the whole UI oauth part. 

## Authors 

Sergey Makarov, Ruslan Mihaylov, Anatoliy Baskakov, Matvey Plevako, Asanali Fazylzhan