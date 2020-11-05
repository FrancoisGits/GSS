import markdown2
import os
import sys
import shutil

repo_sources_MD = sys.argv[1]
repo_sources_HTML = sys.argv[2]

header_html = open("./header_HTML")
header_html_lines = header_html.readlines()
header_html.close()
footer_html = open("./footer_HTML")
footer_html_lines = footer_html.readlines()
footer_html.close()



if os.path.exists(repo_sources_HTML):
    shutil.rmtree(repo_sources_HTML)

if not os.path.exists(repo_sources_HTML):
    os.makedirs(repo_sources_HTML)

list_file_name_md = os.listdir(repo_sources_MD)

with open("./index.html", "r") as old_index_content:
    buf = old_index_content.readlines()


with open("./index.html", "w") as new_index_content:
    for line in buf:
        if line.find('class="article"') != -1:
            line = ""
        new_index_content.write(line)


for file_name in list_file_name_md:


    file_md = open(repo_sources_MD + "/" + file_name, "r")
    html_content = markdown2.markdown(file_md.read(), extras=["code-friendly", "fenced-code-blocks"])
    file_name = os.path.splitext(file_name)[0]

    file_html = open(repo_sources_HTML + "/" + file_name + ".html" ,"w")
    for line1 in header_html_lines:
        if line1.find('<title>') != -1:
            line1 = "<title>" + file_name + "</title>"
        file_html.write(line1)
    file_html.close()

    file_html = open(repo_sources_HTML + "/" + file_name + ".html" ,"a")
    file_html.write(html_content)
    for line2 in footer_html_lines:
        file_html.write(line2)
    file_html.close()

    with open("./index.html", "r") as old_index_content:
        buf = old_index_content.readlines()

    with open("./index.html", "w") as new_index_content:
        for line in buf:
            if line.find('id="liste_article">') != -1:
                line = line + '<div class="article"><a href="./sources_HTML/' + file_name + '.html">' + file_name + '</div>\n'
            new_index_content.write(line)       
