from jinja2 import Environment, FileSystemLoader
import csv, uuid

template_loader = FileSystemLoader('templates')
env = Environment(loader=template_loader)
template = env.get_template('markdown_template.md')

# CSV format
# title/name, pluralized name, type

with open('source/data.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    for row in csvreader:
        md_filename = str(uuid.uuid4()) + '.md'
        rendered_data = template.render(data=row)
        md_file = open('output/'+md_filename, "w")
        md_file.write(rendered_data)
        md_file.close()