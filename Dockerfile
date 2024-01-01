# Start from an existing image with Miniconda installed
FROM continuumio/miniconda3
MAINTAINER Ben Johnson
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=geodjango_project.settings

# Ensure that everything is up-to-date
RUN apt-get -y update && apt-get -y upgrade
RUN conda update -n base conda && conda update -n base --all

# Make a working directory in the image and set it as working dir.
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Copy the Conda environment file
COPY ENV.yml /usr/src/app

# Create and activate the Conda environment
RUN conda env create -n geodjango_project --file ENV.yml

RUN echo "conda activate geodjango_project" >> ~/.bashrc
SHELL ["/bin/bash", "--login", "-c"]

# Set up conda to match our test environment
RUN conda config --add channels conda-forge && conda config --set channel_priority strict

RUN cat ~/.condarc
RUN conda install uwsgi
RUN pip install django-crispy-forms django-leaflet djangorestframework django-pwa

# Copy everything in your Django project to the image.
COPY . /usr/src/app

# Install dependencies using Conda and Pip
RUN conda install gdal=3.7.2

# Make sure that static files are up to date and available
RUN python manage.py collectstatic --no-input

# Expose port 8000 on the image. We'll map a localhost port to this later.
EXPOSE 8080

# Run "uwsgi". uWSGI is a Web Server Gateway Interface (WSGI) server implementation
CMD uwsgi --ini uwsgi.ini
