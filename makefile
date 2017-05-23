all: index.html

index.html: nbs/*.ipynb static.py
	python static.py
