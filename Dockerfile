FROM python:3.11-slim-bookworm
RUN mkdir /app   
COPY pyproject.toml /app 
WORKDIR /app  
ENV PYTHONPATH=${PYTHONPATH}:${PWD} 
RUN pip3 install poetry  
RUN poetry config virtualenvs.create false  
RUN poetry install --no-dev
COPY . /app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]