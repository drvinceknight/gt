import itertools
import nbformat
import pathlib
import shutil
import sys
import tqdm
import collections
import jinja2

from nbconvert import HTMLExporter, PDFExporter

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

def render_template(template_file, template_vars):
    """
    Render a jinja2 template
    """
    templateLoader = jinja2.FileSystemLoader(searchpath="./templates/")
    template_env = jinja2.Environment(loader=templateLoader)
    template = template_env.get_template(template_file)
    return template.render( template_vars )

def make_dir(path):
    """
    Create a directory for the name of the file
    """
    p = pathlib.Path(f"./{get_id(path)}")
    p.mkdir(exist_ok=True)
    nb = convert_html(path)
    html = render_template("chapter.html", {"nb": nb})
    (p / 'index.html').write_text(html)

Chapter = collections.namedtuple("chapter", ["dir", "title", "nb"])

if __name__ == "__main__":

    nb_dir = pathlib.Path('nbs')
    nb_paths = nb_dir.glob('*ipynb')

    changed_nb_paths = sys.argv[1:]
    if changed_nb_paths == []:
        changed_nb_paths, nb_paths = itertools.tee(nb_paths)

    for filename in changed_nb_paths:
        make_dir(pathlib.Path(filename))

    chapters = []
    for path in tqdm.tqdm(nb_paths):
        chapters.append(Chapter(get_id(path), get_name(path), str(path)))

    html = render_template("home.html", {"chapters": chapters})
    with open('index.html', 'w') as f:
        f.write(html)
