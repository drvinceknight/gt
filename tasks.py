from invoke import task

@task
def test(c):
    c.run("pytest --nbval --current-env --doctest-glob='*.rst'")

@task
def main(c):
    c.run("python main.py")
