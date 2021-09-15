FROM python:3.9-slim as base

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

RUN pip install pipenv


FROM base AS python-deps

# Install python dependencies in /.venv
COPY Pipfile Pipfile.lock /
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy


FROM python-deps AS runtime

WORKDIR /code
COPY --from=python-deps /.venv /.venv
ENV PATH="/.venv/bin:$PATH"
RUN chown -R www-data:www-data /code
USER www-data

# Install application into container
COPY . /code/
