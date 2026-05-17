--CONSULTA PARA EL EJERCICIO No. 3

SELECT 
    CONCAT(customers.first_name, ' ', customers.last_name) AS customer,
    COUNT(*) AS failures
FROM customers --seleccionamos a los customers
JOIN campaigns
    ON customers.id = campaigns.customer_id
JOIN events
    ON campaigns.id = events.campaing_id --Aquí hacemos JOIN entre la tabla customers y campaign por id
WHERE events.status = 'failure' --Separamos los eventos por fallo
GROUP BY customers.id -- agrupamos por id
HAVING COUNT(*) > 3 -- contamos los eventos de fallo que sean mayores a 3
ORDER BY failures DESC; --ordena de mayor a menor cantidad de fallas



