About the materials
===================

Overview
--------

The course content is all written using `Jupyter <http://jupyter.org/>`_
notebooks which you can find here:
`<https://github.com/drvinceknight/gt/tree/master/nbs>`_.

This is done using a combination of `Python <https://www.python.org/>`_ and
`Markdown <https://en.wikipedia.org/wiki/Markdown>`_ (as well as `LaTeX
<https://www.latex-project.org/>`_ for the mathematics).

The Jupyter notebooks are then converted in to html which is served using
`Github pages <https://pages.github.com/>`_ and can be seen here:
`<https://vknight.org/gt/>`_.

How this is done
----------------

Using `git <https://git-scm.com/>`_ you can clone the repository locally::

    git clone https://github.com/drvinceknight/gt.git

This will create a copy of all the source files on to a directory on your
computer called :code:`gt`.

To view the notebooks locally you will need to have Python and Jupyter installed
on your computer. I recommend using the `Anaconda <https://anaconda.org/>`_
distribution of Python which not only includes Jupyter but also a number of
tools to ensure portability and reproducibility of scientific computing.

In the :code:`gt` directory you will see an :code:`environment.yml` file. This
is used to define a specific set of Python libraries. To create this
environment on your computer you will need to use a command line application:

- On Mac OSX or linux: search for :code:`terminal`.
- On Windows, assuming you have installed the Anaconda distribution: search for
  :code:`Anaconda Prompt`.

Open this and navigate to the :code:`gt` directory, this is done using the
:code:`cd` command. For more information about using the command line, take a
look at `<https://vknight.org/rsd/chapters/01/>`_.

Once there, type::

    conda env create -f environment.yml

This will create a Python environment on your machine with all the required
software called :code:`gt`. To activate this environment, type::

    source activate gt

You can now start a Jupyter server by typing (still in the command line
application)::

    jupyter notebook

This will open a tab in your browser (**note that you do not need to be online
for this**) that you can browse and use the notebooks with.

**Finally** if you want to convert the notebooks in to the html. In your command
line application, making sure you have activated the :code:`gt` environment
type::

    python main.py

Testing all the code
--------------------

One important advantage of writing the course notes in this way is that all code
snippets (which are often used to confirm calculations carried out) can be
tested. This helps ensure that there are no errors in the notes.

To test the code, in your command line application type::

    sh run_tests.sh

**Note** the above is a command that will only work on Mac OSX or linux. On
windows you should type the specific command in that file which is::

    pytest --nbval --current-env --doctest-glob="*.rst"
