import tkinter as tk
from tkinter import ttk



tree_photos = [["Acacia_rubinia1.png", "Acacia_rubinia2.png", "Acacia_rubinia3.png", "Acacia_rubinia4.png", "Acacia_rubinia5.png",
"Acacia_rubinia6.png", "Acacia_rubinia7.png", "Acacia_rubinia8.png", "Acacia_rubinia9.png", "Acacia_rubinia10.png", 
"Acacia_rubinia11.png", "Acacia_rubinia12.png"], ["Dypsis_lutescens1.png", "Dypsis_lutescens2.png", "Dypsis_lutescens3.png", "Dypsis_lutescens4.png", "Dypsis_lutescens5.png"], 
["Swinglea_glutinosa1.png", "Swinglea_glutinosa2.png", "Swinglea_glutinosa3.png"], ["Mangifera_inidica1.png", "Mangifera_inidica1a.png",
"Mangifera_inidica2.png", "Mangifera_inidica3.png", "Mangifera_inidica4.png", "Mangifera_inidica5.png"], ["Ficus_benjamina1.png",
"Ficus_benjamina2.png", "Ficus_benjamina3.png", "Ficus_benjamina4.png", "Ficus_benjamina5.png", "Ficus_benjamina6.png", "Ficus_benjamina7.png",
"Ficus_benjamina8.png", "Ficus_benjamina9.png", "Ficus_benjamina10.png"], ["Caesalpinia_ebano1.png"], ["Terminalia_catappa1.png",
"Terminalia_catappa2.png", "Terminalia_catappa3.png", "Terminalia_catappa4.png", "Terminalia_catappa5.png"], ["Pithecellobium_dulce1.png",
"Pithecellobium_dulce2.png", "Pithecellobium_dulce3.png", "Pithecellobium_dulce4.png", "Pithecellobium_dulce5.png", "Pithecellobium_dulce6.png",
"Pithecellobium_dulce7.png", "Pithecellobium_dulce8.png"], ["Leucaena_leucocephala1.png", "Leucaena_leucocephala2.png", "Leucaena_leucocephala3.png",
"Leucaena_leucocephala4.png", "Leucaena_leucocephala5.png"], ["Albizia_saman1.png", "Albizia_saman2.png", "Albizia_saman3.png",
"Albizia_saman4.png", "Albizia_saman5.png", "Albizia_saman6.png", "Albizia_saman7.png", "Albizia_saman8.png", "Albizia_saman9.png",
"Albizia_saman10.png"],["Guazuma_ulmifolia1.png", "Guazuma_ulmifolia2.png", "Guazuma_ulmifolia3.png"], ["Melicoccus_bijugatus1.png", 
"Melicoccus_bijugatus2.png"], ["Crescentia_cujete1.png", "Crescentia_cujete2.png", "Crescentia_cujete3.png", "Crescentia_cujete4.png", 
"Crescentia_cujete5.png", "Crescentia_cujete6.png", "Crescentia_cujete7.png", "Crescentia_cujete8.png", "Crescentia_cujete9.png", 
"Crescentia_cujete10.png"], ["Ceiba_pentandra1.png", "Ceiba_pentandra2.png", "Ceiba_pentandra3.png", "Ceiba_pentandra4.png", "Ceiba_pentandra5.png", 
"Ceiba_pentandra6.png"], ["Couroupita_guianensis1.png", "Couroupita_guianensis2.png", "Couroupita_guianensis3.png", "Couroupita_guianensis4.png",
"Couroupita_guianensis5.png", "Couroupita_guianensis6.png", "Couroupita_guianensis7.png", "Couroupita_guianensis8.png", "Couroupita_guianensis9.png"], 
["Sterculia_apetala1.png", "Sterculia_apetala2.png", "Sterculia_apetala3.png"], ["Annona_muricata1.png", "Annona_muricata2.png", "Annona_muricata3.png"], 
["Calliandra_pittieri1.png", "Calliandra_pittieri2.png", "Calliandra_pittieri3.png", "Calliandra_pittieri4.png"],["Trichanthera_gigantea1.png",
"Trichanthera_gigantea2.png", "Trichanthera_gigantea3.png", "Trichanthera_gigantea4.png"],["Erythrina_poeppigiana1.png", "Erythrina_poeppigiana2.png",
"Erythrina_poeppigiana3.png", "Erythrina_poeppigiana4.png", "Erythrina_poeppigiana5.png", "Erythrina_poeppigiana6.png"], ["Guarea_guidonia1.png",
"Guarea_guidonia2.png", "Guarea_guidonia3.png", "Guarea_guidonia4.png", "Guarea_guidonia5.png"], ["Syzygium_jambos1.png", "Syzygium_jambos2.png", 
"Syzygium_jambos3.png", "Syzygium_jambos4.png", "Syzygium_jambos5.png", "Syzygium_jambos6.png"], ["Zanthoxylum_rhoifolium1.png", "Zanthoxylum_rhoifolium2.png",
"Zanthoxylum_rhoifolium3.png", "Zanthoxylum_rhoifolium4.png", "Zanthoxylum_rhoifolium5.png", "Zanthoxylum_rhoifolium6.png", "Zanthoxylum_rhoifolium7.png",
"Zanthoxylum_rhoifolium8.png"], ["Brownea_ariza1.png", "Brownea_ariza2.png", "Brownea_ariza3.png", "Brownea_ariza4.png", "Brownea_ariza5.png", "Brownea_ariza6.png", 
"Brownea_ariza7.png"], ["Hymenaea_courbaril1.png", "Hymenaea_courbaril2.png", "Hymenaea_courbaril3.png", "Hymenaea_courbaril4.png", "Hymenaea_courbaril5.png", 
"Hymenaea_courbaril6.png", "Hymenaea_courbaril7.png"], ["Anacardium_excelsum1.png", "Anacardium_excelsum2.png"], ["Genipa_americana1.png", "Genipa_americana2.png",
"Genipa_americana3.png", "Genipa_americana4.png", "Genipa_americana5.png", "Genipa_americana6.png", "Genipa_americana7.png", "Genipa_americana8.png"], 
["Bambusa_vulgaris1.png", "Bambusa_vulgaris2.png", "Bambusa_vulgaris3.png", "Bambusa_vulgaris4.png"], ["Persea_caerulea1.png", "Persea_caerulea2.png",
"Persea_caerulea3.png", "Persea_caerulea4.png", "Persea_caerulea5.png", "Persea_caerulea6.png", "Persea_caerulea7.png"], ["Pithecellobium_lanceolatum1.png",
"Pithecellobium_lanceolatum2.png", "Pithecellobium_lanceolatum3.png", "Pithecellobium_lanceolatum4.png", "Pithecellobium_lanceolatum5.png", 
"Pithecellobium_lanceolatum6.png", "Pithecellobium_lanceolatum7.png", "Pithecellobium_lanceolatum8.png"], ["Machaerium_capote1.png", "Machaerium_capote2.png",
"Machaerium_capote3.png", "Machaerium_capote4.png"], ["Ochroma_pyramidale1.png", "Ochroma_pyramidale2.png", "Ochroma_pyramidale3.png"], ["Guadua_angustifolia1.png",
"Guadua_angustifolia2.png", "Guadua_angustifolia3.png", "Guadua_angustifolia4.png"], ["Ficus_glabrata1.png"], ["Sabal_mauritiforms1.png", "Sabal_mauritiforms2.png",
"Sabal_mauritiforms3.png", "Sabal_mauritiforms4.png", "Sabal_mauritiforms5.png"], ["Tessaria_integrifolia1.png", "Tessaria_integrifolia2.png", "Tessaria_integrifolia3.png",
"Tessaria_integrifolia4.png", "Tessaria_integrifolia5.png"], ["Cupania_americana1.png", "Cupania_americana2.png", "Cupania_americana3.png", "Cupania_americana4.png",
"Cupania_americana5.png"], ["Erythrina_edulis1.png", "Erythrina_edulis2.png", "Erythrina_edulis2a.png", "Erythrina_edulis3.png", "Erythrina_edulis4.png",
"Erythrina_edulis5.png", "Erythrina_edulis6.png", "Erythrina_edulis7.png"], ["Didymopanax_morototoni1.png", "Didymopanax_morototoni2.png", "Didymopanax_morototoni3.png",
"Didymopanax_morototoni4.png"], ["Crateva_tapia1.png", "Crateva_tapia2.png", "Crateva_tapia3.png", "Crateva_tapia4.png", "Crateva_tapia5.png", "Crateva_tapia6.png",
"Crateva_tapia7.png", "Crateva_tapia8.png", "Crateva_tapia9.png"], ["Xylopia_ligustrifolia1.png", "Xylopia_ligustrifolia2.png"], ["Podacarpus_oleifolius1.png", 
"Podacarpus_oleifolius2.png", "Podacarpus_oleifolius3.png", "Podacarpus_oleifolius4.png", "Podacarpus_oleifolius5.png"], ["Tabebuia_rosea1.png", "Tabebuia_rosea2.png", 
"Tabebuia_rosea3.png", "Tabebuia_rosea4.png"], ["Adonidia_merrillii1.png", "Adonidia_merrillii2.png", "Adonidia_merrillii3.png", "Adonidia_merrillii4.png", 
"Adonidia_merrillii5.png"], ["Roystonea_regia1.png", "Roystonea_regia2.png", "Roystonea_regia3.png", "Roystonea_regia4.png", "Roystonea_regia5.png", "Roystonea_regia6.png"], 
["Spathodea_campanulata1.png", "Spathodea_campanulata2.png", "Spathodea_campanulata3.png", "Spathodea_campanulata4.png", "Spathodea_campanulata5.png"], ["Jacaranda_caucana1.png",
"Jacaranda_caucana2.png", "Jacaranda_caucana3.png", "Jacaranda_caucana4.png", "Jacaranda_caucana5.png", "Jacaranda_caucana6.png", "Jacaranda_caucana7.png", "Jacaranda_caucana8.png",
"Jacaranda_caucana9.png"], ["Clitoria_fairchildiana1.png", "Clitoria_fairchildiana2.png", "Clitoria_fairchildiana3.png", "Clitoria_fairchildiana4.png", "Clitoria_fairchildiana5.png",
"Clitoria_fairchildiana6.png", "Clitoria_fairchildiana7.png"], ["Senna_siamea1.png", "Senna_siamea2.png", "Senna_siamea3.png", "Senna_siamea4.png", "Senna_siamea5.png",
"Senna_siamea6.png"], ["Cananga_odorata1.png", "Cananga_odorata2.png", "Cananga_odorata3.png", "Cananga_odorata4.png", "Cananga_odorata5.png", "Cananga_odorata6.png"]]







