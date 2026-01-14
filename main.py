import pandas as pd

df_arb    = pd.read_csv("./src/les-arbres.csv", sep=";")
df_arbRmq = pd.read_csv("./src/arbres-remarquables.csv", sep=";")

arb_prep = pd.DataFrame(
    {
        "Communes"  : df_arb["ARRONDISSEMENT"],
        "Nom_fr"    : df_arb["LIBELLE FRANCAIS"],
        "Nom_lt"    : df_arb["ESPECE"],
        "Hauteur_m" : df_arb["HAUTEUR (m)"],
        "Circ_cm"   : df_arb["CIRCONFERENCE (cm)"],
        "Rmq"       : 1,
        "geo_pt_2d" : df_arb["geo_point_2d"],
    }
)
arb_prep = arb_prep[arb_prep["Rmq"] == "OUI"]

arbRmq_prep = pd.DataFrame(
    {
        "Communes"  : df_arbRmq["COMMUNE"],
        "Nom_fr"    : df_arbRmq["NOM_FRANCAIS"],
        "Nom_lt"    : df_arbRmq["NOM_LATIN"],
        "Hauteur_m" : df_arbRmq["HAUTEUR"],
        "Circ_cm"   : df_arbRmq["CIRCONFERENCE"]*100,
        "Rmq"       : 1,
        "geo_pt_2d" : df_arbRmq["geo_point_2d"],
    }
)

cols_prep = ["Communes", "Nom_fr", "Nom_lt", "Hauteur_m", "Circ_cm", "Rmq", "geo_pt_2d"]
df_fusioned = pd.concat([arb_prep[cols_prep], arbRmq_prep[cols_prep]], ignore_index=True)

df_fusioned.to_json("arbres_fusioned.json", index=False)
df_fusioned.to_csv("arbres_fusioned_lisible.csv", index=False)
