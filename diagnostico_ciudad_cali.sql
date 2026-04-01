SELECT caespecie AS especie, COUNT(DISTINCT id) AS registros
FROM censo_arboreo
GROUP BY especie ORDER BY registros DESC;