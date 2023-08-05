FROM postgres:14.3
RUN localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LANG en_US.utf8

# set environment variables for PostgreSQL
ENV POSTGRES_USER user
ENV POSTGRES_PASSWORD password
ENV POSTGRES_DB ecommerce

# copy SQL file to the Docker image
COPY ecommerce_ddl.sql /docker-entrypoint-initdb.d/
COPY insert.sql /sql-scripts/
COPY query.sql /sql-scripts/
