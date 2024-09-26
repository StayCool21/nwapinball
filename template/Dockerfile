FROM python:3.9-slim

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV HOST 0.0.0.0

COPY requirements.txt .
# install python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# running migrations
RUN python manage.py migrate

# # expose port 8080
EXPOSE 8080

# gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "core.wsgi:application"]