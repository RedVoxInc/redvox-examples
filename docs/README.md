# How to contribute to the RedVox Examples Docs

### Python libraries required
- m2r2, to reference docs outside the `source` folder
- sphinx
- furo, the sphinx theme used
- myst-parser, to parse markdown (.md) files to sphinx

Get going with:
```shell
pip install m2r2
pip install sphinx
pip install furo
pip install myst-parser
```
### Editing the docs

The meat of the documentation is in redvox-examples/docs/source. The `.md` files are the base of the documentation.

If you add new `.md` files, make sure that `index.rst` inside the `source` folder points to the new file using
`.. toctree::`.

Please do not modify the following files (unless you really know what you are doing):
- `.nojekyll` - used for hosting the docs in Github Pages
- `make.bat` and `Makefile` - used by sphinx to clean and build the documentation
- `index.html` inside the `docs` folder (okay to modify the `index.html` inside the `source` folder) - used for hosting 
the docs in Github pages

### Viewing the docs locally

Once you are done with your changes, open a terminal with a python environment, cd to redvox-examples/docs, and type `make clean` and `make html`.
`make clean` will eliminate everything in the `build` folder and `make html` will (re)build the documentation.

```shell
(venv3910) meritxell@ISLA-11 docs % 
(venv3910) meritxell@ISLA-11 docs % make clean 
(venv3910) meritxell@ISLA-11 docs % make html 
```

To view the docs in a browser, go to redvox-examples/docs/build/html and open `index.html` in a browser.

