# Nexo-DevOps-Task

## Local environment

Local environment can be started with:

    $ docker-compose up --build

## Environment

1. The environment consists of minikube kubernetes cluster installed on Windows via virtual box driver.
2. Services are deployed in the kubernetes cluster with helm via the following commands executed in the root directories of the services:
    * helm install nexo-app application-helm-chart
    * helm install mysql-db mysql-db-helm-chart
3. Images during the creating of the service pods are pulled from private ghcr repositories. Credentials to access the private repository are obtained via kubernetes secrets.

## Images

Each service has its own repository in GitHub ghcr:
   * ghcr.io/ivoilieviliev/nexo-app:latest
   * ghcr.io/ivoilieviliev/mysql-db-instance:latest

The image repositories are private and cannot be accessed publicly.

