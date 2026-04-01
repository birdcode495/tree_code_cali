---- Diagnostico de especies por abundancia en la ciudad de Cali

SELECT caespecie AS especie, COUNT(DISTINCT id) AS registros
FROM censo_arboreo
GROUP BY especie ORDER BY registros DESC;

---- Tabla para matching con GBIF API

SELECT DISTINCT caespecie AS scientificName
FROM censo_arboreo;

---- Creación de campo en tabla del Censo Arboreo para crear link a la API GBIF por especie

ALTER TABLE censo_arboreo ADD COLUMN gbif_key varchar(30), ADD COLUMN gbif_link varchar(150);

UPDATE censo_arboreo SET gbif_key = matching_gbif.key
FROM matching_gbif
WHERE censo_arboreo.caespecie = matching_gbif.verbatimscientificname;

UPDATE censo_arboreo SET gbif_link = 'https://www.gbif.org/es/species/' || gbif_key;

---- Construccion de tabla de especies del Censo Arboreo para la investigacion con API GBIF

SELECT caespecie AS nombre_cientifico, canomcom AS nombre_comun, cafamilia AS familia,
COUNT(DISTINCT id) AS registros, gbif_link AS gbif
FROM censo_arboreo
GROUP BY nombre_cientifico, nombre_comun, familia, gbif
ORDER BY registros DESC;



