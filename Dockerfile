FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Install pipenv
RUN pip install --upgrade pip && pip install pipenv

# Copy project files
COPY . .

# Install dependencies using Pipenv
RUN pipenv install --deploy --system

# Expose port
EXPOSE 8000

# Run Django dev server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

CMD python manage.py migrate && \
    python manage.py runserver 0.0.0.0:8000
