import markdown2
import os
import sys

repo_sources_MD = sys.argv[1]
repo_sources_HTML = sys.argv[2]

header_html = open("./header_HTML")
header_html_lines = header_html.readlines()
header_html.close()
footer_html = open("./footer_HTML")
footer_html_lines = footer_html.readlines()
footer_html.close()

if not os.path.exists(repo_sources_HTML):
    os.makedirs(repo_sources_HTML)

list_file_name_md = os.listdir(repo_sources_MD)

for file_name in list_file_name_md:

    file_md = open(repo_sources_MD + "/" + file_name, "r")
    html_content = markdown2.markdown(file_md.read())
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




