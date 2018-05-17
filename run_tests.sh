# Test the notebooks and the documentation.
# Using nbval-lax to only test that they pass.
pytest --nbval --current-env --doctest-glob="*.rst"
