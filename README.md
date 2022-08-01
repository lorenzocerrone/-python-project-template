# python-project-demo
A minimal python project demo to use as template for new projects:
  * Versioning
  * Basic GitHub actions for testing and deployment
  * conda packaging

This is just a small educational sample for me to try different configurations, but keep in mind that probably something like
python [cookiecutter](https://github.com/cookiecutter/cookiecutter) is what you probably need. 

## General TODO list
1. Use this repo as GitHub template or clone the repo locally
2. rename `package_cool_name` and change accordingly all mentions of the name in:
   * [setup.py](https://github.com/lorenzocerrone/basic-python-project-demo/blob/main/setup.py)
   * [tests](https://github.com/lorenzocerrone/basic-python-project-demo/blob/main/tests/)
   * [GitHub Workflow](https://github.com/lorenzocerrone/basic-python-project-demo/blob/main/.github/workflows/build-deploy-on-conda.yml)
   * [.bumpversion.cfg](https://github.com/lorenzocerrone/basic-python-project-demo/blob/main/.bumpversion.cfg) 
   * [conda meta.yaml](https://github.com/lorenzocerrone/basic-python-project-demo/blob/main/conda-recipe/meta.yaml)
3. reset the current `versioning` by changing [__version__.py](https://github.com/lorenzocerrone/basic-python-project-demo/blob/main/package_cool_name/__version__.py)

## Setup conda
1. Write a `meta.yaml` following the [meta](conda-recipe/meta.yaml) template.
2. If GitHub actions are not installed:
    * Install `conda-build`, by doing `conda install -q conda-build`.
    * Build: `conda build conda-recipe` (add channel here if required).
    * Install: `conda install --use-local package_cool_name`.
    * Upload: [complete guide](https://enterprise-docs.anaconda.com/en/latest/data-science-workflows/packages/upload.html).

## Versioning
1. Make sure that `bumpversion` is installed in your conda env, see 
[bump2version](https://github.com/c4urself/bump2version/) for instructions.
2. Checkout master branch.
3. Run `bumpversion patch` (or `major` or `minor`) - this will bum the version in `.bumpversion.cfg` and `__version__.py` add create a new tag.
4. Run `git push && git push --tags` - this will trigger tagged action build.
