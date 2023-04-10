# Render markdown from CSV 

> Render Jekyll compatible markdown pages from CSV row entries

## Usage
### Update data.csv
1. Update `source/data.csv`

### Edit markdown_template.md to mirror expected layout
2. Edit the `templates/markdown_template.md` template to reflect the data source entries

### run render.py to create .md files based on CSV (create column for specific filename and replace in render.py)
3. Run `$ python3 render.py`

Rendered markdown files are located in `output`

## License

MIT © [Tom Claessens](https://tomclaessens.be)
