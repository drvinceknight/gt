import itertools
import nbformat
import pathlib
import shutil
import sys
import tqdm
import collections
import jinja2

from nbconvert import HTMLExporter, PDFExporter, MarkdownExporter

ROOT = "gt"
BINDERROOT = "https://mybinder.org/v2/gh/drvinceknight/gt/master?filepath=nbs"
TITLE = "Game Theory"

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
        stem = stem.replace(",", "")
        return stem

def get_name(path):
    """
    Return the name of a file
    """
    stem = path.stem
    try:
        return stem[stem.index('-'):].replace('-', ' ').lstrip()
    except ValueError:
        return stem

def convert_markdown(nb_path):
    """
    Convert a notebook to markdown
    """
    markdown_exporter = MarkdownExporter()
    return markdown_exporter.from_file(str(nb_path))

def convert_html(nb_path):
    """
    Convert a notebook to html
    """
    html_exporter = HTMLExporter()
    html_exporter.template_file = "basic"
    return html_exporter.from_file(str(nb_path))

def render_template(template_file, template_vars, searchpath="./templates/"):
    """
    Render a jinja2 template
    """
    templateLoader = jinja2.FileSystemLoader(searchpath=searchpath)
    template_env = jinja2.Environment(loader=templateLoader)
    template = template_env.get_template(template_file)
    return template.render(template_vars)

def make_dir(path, directory, previous_url=None, next_url=None, chapters=None):
    """
    Create a directory for the name of the file
    """
    path_id = get_id(path)
    p = pathlib.Path(f"./{directory}/{path_id}")
    p.mkdir(exist_ok=True)
    nb, _ = convert_html(path)
    check = False
    nb = nb.replace("{{root}}", ROOT)
    html = render_template("content.html", {"nb": nb,
        "root": ROOT,
        "title": TITLE,
        "id": path_id,
        "chapters": chapters,
        "previous_url": previous_url,
        "next_url": next_url})
    (p / 'index.html').write_text(html)

def make_collection(paths, directory,
                    make_previous_url=True,
                    make_next_url=True,
                    chapters=None):

    number_of_paths = len(paths)
    for index, filename in enumerate(paths):
        previous_path = paths[(index - 1) % number_of_paths]
        previous_id = get_id(previous_path)

        next_path = paths[(index + 1) % number_of_paths]
        next_id = get_id(next_path)

        make_dir(pathlib.Path(filename), directory=directory,
                 previous_url=previous_id,
                 next_url=next_id,
                 chapters=chapters)

Chapter = collections.namedtuple("chapter", ["dir", "title", "nb", "filename"])

if __name__ == "__main__":

    nb_dir = pathlib.Path('nbs')
    chapter_paths = sorted(nb_dir.glob('./chapters/*ipynb'))
    exercise_paths = sorted(nb_dir.glob('./exercises/*ipynb'))
    solution_paths = sorted(nb_dir.glob('./solutions/*ipynb'))
    solution_paths.append(pathlib.Path("./assets/assessment/mock/ind/mock.ipynb"))
    other_paths = list(nb_dir.glob('./other/*ipynb'))
    extra_paths = []


    chapters = []
    for path in tqdm.tqdm(sorted(chapter_paths)):
        chapters.append(Chapter(f"{get_id(path)}",
                                get_name(path),
                                str(path),
                                path.name))
    exercises = []
    for path in tqdm.tqdm(sorted(exercise_paths)):
        exercises.append(Chapter(f"{get_id(path)}",
                                 get_name(path), 
                                 str(path),
                                 path.name))

    for paths, directory in [(chapter_paths, "chapters"),
                             (exercise_paths, "exercises"),
                             (solution_paths, "solutions"),
                             (other_paths, "other")]:
        make_collection(paths=paths, directory=directory, chapters=chapters)
        if directory == "chapters":
            md = "---\ntitle: Game Theory\n---\n"
            for path in paths:
                chapter_md, _ = convert_markdown(path)
                md += chapter_md
            path = pathlib.Path("./assets/main.md")
            path.write_text(md)


    html = render_template("home.html", {"chapters": chapters,
                                         "root": ROOT,
                                         "title": TITLE,
                                         "binderoot": BINDERROOT,
                                         "exercises": exercises})
    with open('index.html', 'w') as f:
        f.write(html)

    html = render_template("chapters.html", {"chapters": chapters, "root": ROOT,
                                             "title": TITLE,
                                             "binderoot": BINDERROOT})
    with open('./chapters/index.html', 'w') as f:
        f.write(html)

    html = render_template("exercises.html", {"exercises": exercises, "root": ROOT,
                                              "title": TITLE,
                                              "binderoot": BINDERROOT})
    with open('./exercises/index.html', 'w') as f:
        f.write(html)

