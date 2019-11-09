# myGrades

Website to make management of marks and grades easier for both students and teachers. Teachers can easily add marks for all students while students have the ability to view their own marks only. All students of the same branch are grouped together so that teachers can send group notifications and upload notes or other media to the entire class.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Python Environment and a Virtual Environment Manager is required to run this project.

```
python --version
```

### Installing

Using Conda environment manager to get the project up and running. All these commands are run on Ubuntu 18.04 Bash

```
conda create -n envName python=3.6.5
```

Installing Django within the Virtual Environment

```
pip install django=2.2.5
```

Open the project folder and run migrations, This is necessary for creating the database tables

```
python manage.py makemigrations gradesApp
```
```
python manage.py migrate 
```
Finally run the server and enter the localhost address that is returned

```
python manage.py runserver
```


## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* Django [Web Framework]
* HTML,CSS,Bootstrap [Frontend]
* SQLite [Backend]


## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Name** - *Initial work* - [Github Name](https://github.com/link)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.


## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

