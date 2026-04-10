# Dockerfile for Django API

# use Debian based Python image for better dependency support
FROM python:3.13-bookworm        
# set working directory inside container
WORKDIR /src                     
# copy dependency list
COPY ./requirements.txt .        
# install Python dependencies
RUN pip install -r requirements.txt  
# copy project source code into container
COPY . .              
# run Django with Gunicorn
CMD gunicorn --bind 0.0.0.0:8000 --workers 8 itworkedlocally_proj.wsgi:application  