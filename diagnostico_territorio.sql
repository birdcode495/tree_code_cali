---- Diagnostico preliminar de riqueza de especies arboreas por comuna

SELECT comuna, COUNT(DISTINCT caespecie) AS riqueza_especies
FROM comunas, censo_arboreo
WHERE ST_Intersects(comunas.geom, censo_arboreo.geom)
GROUP BY comuna ORDER BY riqueza_especies DESC;

---- Construccion de tabla de especies por comunas

SELECT caespecie, COUNT(DISTINCT censo_arboreo.id) AS reg
FROM censo_arboreo, comunas
WHERE ST_Intersects(censo_arboreo.geom, comunas.geom) AND comuna = 1
GROUP BY caespecie ORDER BY reg DESC;


