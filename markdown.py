import markdown2
import os
import sys

dossier_sources_MD = sys.argv[1]
dossier_sources_HTML = sys.argv[2]

file_header = open("./header_HTML")
header_HTML = file_header.readlines()
file_header.close()
file_footer = open("./footer_HTML")
footer_HTML = file_footer.readlines()
file_footer.close()

if not os.path.exists(dossier_sources_HTML):
    os.makedirs(dossier_sources_HTML)

liste_nom_fichiers_MD = os.listdir(dossier_sources_MD)

for i in liste_nom_fichiers_MD:

    f = open(dossier_sources_MD + "/" + i, "r")
    page_rendered = markdown2.markdown(f.read())
    i = os.path.splitext(i)[0]

    page_rendered_file = open(dossier_sources_HTML + "/" + i + ".html" ,"w")
    for y in header_HTML:
        if y.find('<title>') != -1:
            y = "<title>" + i + "</title>"
        page_rendered_file.write(y)
    page_rendered_file.close()

    page_rendered_file = open(dossier_sources_HTML + "/" + i + ".html" ,"a")
    page_rendered_file.write(page_rendered)
    for z in footer_HTML:
        page_rendered_file.write(z)
    page_rendered_file.close()




