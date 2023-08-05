docker build -t my_postgres_image:v1.0 .
docker run -d --name my_postgres_container -p 5432:5432 my_postgres_image:v1.0
docker start 2e53fbc0116c632837e8cd452a1ee3e9ca1f959d435578e94cf1b94d21fabaa3
docker exec -it my_postgres_container psql -U user -d ecommerce -f /docker-entrypoint-initdb.d/ecommerce_ddl.sql
docker exec -it my_postgres_container psql -U user -d ecommerce -f /sql-scripts/insert.sql
docker exec -it my_postgres_container psql -U user -d ecommerce -f /sql-scripts/query.sql