"""
Tests for main.py
"""
import pathlib

import main

def test_get_id():
    path = pathlib.Path("./nbs/chapters/00-Introduction-to-the-course.ipynb")
    assert main.get_id(path) == "00"

def test_get_id_with_no_id():
    path = pathlib.Path("./nbs/other/Assessment.ipynb")
    assert main.get_id(path) == "assessment"

def test_get_name():
    path = pathlib.Path("./nbs/chapters/00-Introduction-to-the-course.ipynb")
    assert main.get_name(path) == "Introduction to the course"

def test_get_with_no_id():
    path = pathlib.Path("./nbs/other/Assessment.ipynb")
    assert main.get_name(path) == "Assessment"

def test_convert_html():
    path = pathlib.Path("./nbs/other/Assessment.ipynb")
    html_output = main.convert_html(path)

    assert len(html_output) == 2
    assert type(html_output) is tuple
    assert type(html_output[0]) is str

def test_render_template():
    path = pathlib.Path("./nbs/other/Assessment.ipynb")
    path_id = main.get_id(path)
    nb, _ = main.convert_html(path)
    nb = nb.replace("{{root}}", main.ROOT)
    html = main.render_template("content.html", {"nb": nb,
                                                 "root": main.ROOT,
                                                 "id": path_id,})

    assert type(html) is str
    assert main.ROOT in html
    assert path_id in html
    assert nb in html
