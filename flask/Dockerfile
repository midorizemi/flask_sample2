FROM python:3.8.5-slim-buster

ARG project_dir=/project/
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

COPY src/sample/requirements.txt $project_dir

WORKDIR $project_dir

RUN pip install --upgrade pip && \
    pip install --no-cache pylint \
                          Flask \
                          pylint-flask \
                          SQLAlchemy \
                          Flask-SQLAlchemy \
                          Flask-Migrate \
                          PyMySQL \
                          marshmallow \
                          marshmallow-sqlalchemy \
                          flask-marshmallow
    # pip install --no-cache-dir -r requirements.txt

EXPOSE 5000