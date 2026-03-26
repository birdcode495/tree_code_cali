---- Diagnostico preliminar de riqueza de especies arboreas por comuna

SELECT comuna, COUNT(DISTINCT caespecie) AS riqueza_especies
FROM comunas, censo_arboreo
WHERE ST_Intersects(comunas.geom, censo_arboreo.geom)
GROUP BY comuna ORDER BY riqueza_especies DESC;

