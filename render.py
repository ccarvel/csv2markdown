from jinja2 import Environment, FileSystemLoader
import csv

template_loader = FileSystemLoader('templates')
env = Environment(loader=template_loader)
template = env.get_template('markdown_template.md')

# CSV format
# title/name, pluralized name, type

with open('source/data.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    for row in csvreader:
        md_filename = row[0] + '.md' #for md filename, choose column with desired filename a=0 b=1 c=2...z=25...etc
        rendered_data = template.render(data=row)
        md_file = open('output/'+md_filename, "w")
        md_file.write(rendered_data)
        md_file.close()
