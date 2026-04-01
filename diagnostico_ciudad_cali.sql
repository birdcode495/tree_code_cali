---- Diagnostico de especies por abundancia en la ciudad de Cali

SELECT caespecie AS especie, COUNT(DISTINCT id) AS registros
FROM censo_arboreo
GROUP BY especie ORDER BY registros DESC;

---- Tabla para matching con GBIF API

SELECT DISTINCT caespecie AS scientificName
FROM censo_arboreo;

