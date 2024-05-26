CREATE EXTENSION postgis;

SELECT DISTINCT nombre_cie AS nombre_cientifico,  
COUNT(DISTINCT id) AS reg FROM censo_arboreo_cali
GROUP BY nombre_cientifico ORDER BY reg DESC;

SELECT DISTINCT nombre_cie AS nombre_cientifico, COUNT(DISTINCT id) AS reg
FROM especies_autoctonas_cali
GROUP BY nombre_cientifico ORDER BY reg DESC;