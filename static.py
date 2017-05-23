"""
A script to generate index.html
"""
import pathlib
import shutil
from nbconvert import HTMLExporter, PDFExporter
import nbformat

nb_dir = pathlib.Path('nbs')
nb_paths = nb_dir.glob('*ipynb')

def get_id(path):
    """
    Return the id of a file
    """
    stem = path.stem
    return stem[:stem.index('-')]

def get_name(path):
    """
    Return the name of a file
    """
    stem = path.stem
    return stem[stem.index('-'):].replace('-', ' ')

def convert_html(nb_path):
    """
    Convert a notebook to html
    """
    html_exporter = HTMLExporter()
    return html_exporter.from_file(str(nb_path))[0]

def convert_pdf(nb_path):
    """
    Convert a notebook to pdf
    """
    pdf_exporter = PDFExporter()
    return pdf_exporter.from_file(str(nb_path))[0]


def make_dir(path):
    """
    Create a directory for the name of the file
    """
    p = pathlib.Path(f"./{get_id(path)}")
    p.mkdir(exist_ok=True)
    html = convert_html(path)
    pdf = convert_pdf(path)
    (p / 'index.html').write_text(html)
    (p / 'index.pdf').write_bytes(pdf)

if __name__ == "__main__":
    index = "<h2>Content</h2>\n"
    index += "<ul>"
    for path in nb_paths:
        make_dir(path)

        index += f"<li>{get_id(path)}: "

        # index.html
        index += f"<a href=./{get_id(path)}/>{get_name(path)}</a> "

        # index.pdf
        index += f"(<a href=./{get_id(path)}/index.pdf>pdf</a>, "

        # *ipynb
        index += f"<a href={path}>ipynb</a>)"

        index += "</li>"

    index += "</ul>"
    p = pathlib.Path("./index.html")
    p.write_text(index)
