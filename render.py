import itertools
import nbformat
import pathlib
import shutil
import sys
import tqdm
import collections
import jinja2

from nbconvert import HTMLExporter, PDFExporter

ROOT = "gt"

def get_id(path):
    """
    Return the id of a file
    """
    stem = path.stem
    try:
        return stem[:stem.index('-')]
    except ValueError:
        stem = stem.lower()
        stem = stem.replace(" ", "-")
        return stem

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
    html_exporter.template_file = "basic"
    return html_exporter.from_file(str(nb_path))

def render_template(template_file, template_vars):
    """
    Render a jinja2 template
    """
    templateLoader = jinja2.FileSystemLoader(searchpath="./templates/")
    template_env = jinja2.Environment(loader=templateLoader)
    template = template_env.get_template(template_file)
    return template.render( template_vars )

def make_dir(path, directory):
    """
    Create a directory for the name of the file
    """
    path_id = get_id(path)
    p = pathlib.Path(f"./{directory}/{path_id}")
    p.mkdir(exist_ok=True)
    nb, resources = convert_html(path)
    css = resources["inlining"]["css"]
    html = render_template("content.html", {"nb": nb, "css": css[1] + css[2],
                                            "root": ROOT,
                                            "id": path_id})
    (p / 'index.html').write_text(html)

Chapter = collections.namedtuple("chapter", ["dir", "title", "nb"])

if __name__ == "__main__":

    nb_dir = pathlib.Path('nbs')
    chapter_paths = list(nb_dir.glob('./chapters/*ipynb'))
    other_paths = list(nb_dir.glob('./other/*ipynb'))

    for filename in chapter_paths:
        make_dir(pathlib.Path(filename), directory="chapters")

    for filename in other_paths:
        make_dir(pathlib.Path(filename), directory="other")

    chapters = []
    for path in tqdm.tqdm(sorted(chapter_paths)):
        chapters.append(Chapter(f"{get_id(path)}",
                                get_name(path), str(path)))

    html = render_template("home.html", {"chapters": chapters, "root": ROOT})
    with open('index.html', 'w') as f:
        f.write(html)

    html = render_template("chapters.html", {"chapters": chapters, "root": ROOT})
    with open('./chapters/index.html', 'w') as f:
        f.write(html)


