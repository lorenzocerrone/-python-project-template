# python-project-cookie-cutter
A minimal python project to use as cheatsheet for new projects:
  * Versioning
  * Basic GitHub actions
  * Conda-packaging

## Setup conda
1. Write a `meta.yaml` following the [meta](conda-recipe/meta.yaml) template.
2. If GitHub actions are not installed:
    * Install `conda-build`, by doing `conda install -q conda-build`.
    * Build: `conda build conda-recipe` (add channel here if required).
    * Install: `conda install --use-local package_cool_name`.
    * Upload: [complete guide](https://enterprise-docs.anaconda.com/en/latest/data-science-workflows/packages/upload.html).

## Setup actions
See [workflow](.github/workflows/build-deploy-on-conda.yml) for an example.

## Versioning
1. Make sure that `bumpversion` is installed in your conda env, see 
[bump2version](https://github.com/c4urself/bump2version/) for instructions.
2. Checkout master branch.
3. Run `bumpversion patch` (or `major` or `minor`) - this will bum the version in `.bumpversion.cfg` and `__version__.py` add create a new tag.
4. Run `git push && git push --tags` - this will trigger tagged action build.