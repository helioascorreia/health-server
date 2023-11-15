FROM python:3.12-bookworm

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

ARG REQUIREMENTS

WORKDIR /app

# Creates a non-root user and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
# RUN useradd -u 10001 ubuntu && chown -R ubuntu /home/ubuntu
# USER ubuntu

# Create a non-privileged user that the app will run under.
# See https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#user
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    # --home "/nonexistent" \
    # --shell "/sbin/nologin" \
    # --no-create-home \
    --uid "${UID}" \
    appuser

# Download dependencies as a separate step to take advantage of Docker's caching.
# Leverage a cache mount to /root/.cache/pip to speed up subsequent builds.
# Leverage a bind mount to requirements.txt to avoid having to copy them into
# into this layer.
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements/base.txt,target=requirements/base.txt \
    --mount=type=bind,source=requirements/${REQUIREMENTS:-server.txt},target=requirements/${REQUIREMENTS:-server.txt} \
    python -m pip install -r requirements/${REQUIREMENTS:-server.txt} && python -m pip install --upgrade pip

# Switch to the non-privileged user to run the application.
USER appuser

# Expose the port that the application listens on.
EXPOSE 5000

COPY . .

WORKDIR /app/application

CMD [ "sanic" "server:app" "--host=0.0.0.0" "--port=5000" "--workers=2" ]