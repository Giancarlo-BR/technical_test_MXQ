-- =============================================================
-- Questão 3 — SQL 
-- =============================================================


-- a) Listar o nome de todos os clientes ativos que fizeram
--    pelo menos um pedido com status 'pago'.

SELECT DISTINCT c.nome
FROM clientes c
INNER JOIN pedidos p ON p.cliente_id = c.id
WHERE c.ativo = TRUE
  AND p.status = 'pago';


-- b) Retornar o valor total gasto por cada cidade,
--    considerando apenas pedidos com status 'pago'.
--    Ordenar do maior para o menor.

SELECT c.cidade,
       SUM(p.valor) AS total_gasto
FROM clientes c
INNER JOIN pedidos p ON p.cliente_id = c.id
WHERE p.status = 'pago'
GROUP BY c.cidade
ORDER BY total_gasto DESC;


-- c) Encontrar clientes que nunca fizeram nenhum pedido.

SELECT c.nome
FROM clientes c
LEFT JOIN pedidos p ON p.cliente_id = c.id
WHERE p.id IS NULL;
