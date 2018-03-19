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
        stem = stem.replace(",", "")
        return stem

def get_name(path):
    """
    Return the name of a file
    """
    stem = path.stem
    try:
        return stem[stem.index('-'):].replace('-', ' ')
    except ValueError:
        return stem

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

def make_dir(path, directory, previous_url=None, next_url=None):
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
        "id": path_id,
        "previous_url": previous_url,
        "next_url": next_url})
    (p / 'index.html').write_text(html)

Chapter = collections.namedtuple("chapter", ["dir", "title", "nb"])

if __name__ == "__main__":

    nb_dir = pathlib.Path('nbs')
    chapter_paths = sorted(nb_dir.glob('./chapters/*ipynb'))
    exercise_paths = sorted(nb_dir.glob('./exercises/*ipynb'))
    solution_paths = sorted(nb_dir.glob('./solutions/*ipynb'))
    other_paths = list(nb_dir.glob('./other/*ipynb'))

    number_of_chapters = len(chapter_paths)
    for index, filename in enumerate(chapter_paths):
        previous_path = chapter_paths[(index - 1) % number_of_chapters]
        previous_id = get_id(previous_path)
        next_path = chapter_paths[(index + 1) % number_of_chapters]
        next_id = get_id(next_path)

        make_dir(pathlib.Path(filename), directory="chapters", 
                 previous_url=previous_id,
                 next_url=next_id)

    number_of_exercises = len(exercise_paths)
    for index, filename in enumerate(exercise_paths):
        previous_path = exercise_paths[(index - 1) % number_of_exercises]
        previous_id = get_id(previous_path)
        next_path = exercise_paths[(index + 1) % number_of_exercises]
        next_id = get_id(next_path)

        make_dir(pathlib.Path(filename), directory="exercises",
                 previous_url=previous_id,
                 next_url=next_id)


    number_of_solutions = len(solution_paths)
    for index, filename in enumerate(solution_paths):
        previous_path = solution_paths[(index - 1) % number_of_solutions]
        previous_id = get_id(previous_path)
        next_path = solution_paths[(index + 1) % number_of_solutions]
        next_id = get_id(next_path)

        make_dir(pathlib.Path(filename), directory="solutions",
                 previous_url=previous_id,
                 next_url=next_id)

    for filename in other_paths:
        make_dir(pathlib.Path(filename), directory="other")

    chapters = []
    for path in tqdm.tqdm(sorted(chapter_paths)):
        chapters.append(Chapter(f"{get_id(path)}",
                                get_name(path), str(path)))
    exercises = []
    for path in tqdm.tqdm(sorted(exercise_paths)):
        exercises.append(Chapter(f"{get_id(path)}",
                                get_name(path), str(path)))

    html = render_template("home.html", {"chapters": chapters,
                                         "root": ROOT,
                                         "exercises": exercises})
    with open('index.html', 'w') as f:
        f.write(html)

    html = render_template("chapters.html", {"chapters": chapters, "root": ROOT})
    with open('./chapters/index.html', 'w') as f:
        f.write(html)

    html = render_template("exercises.html", {"exercises": exercises, "root": ROOT})
    with open('./exercises/index.html', 'w') as f:
        f.write(html)
