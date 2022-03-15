# python-project-cookie-cutter
A minimal python project to use as cheatsheet for new projects:
  * Versioning
  * Basic GitHub actions
  * Conda-packaging

## Setup conda


## Setup actions

## Versioning
1. Make sure that `bumpversion` is installed in your conda env, see 
[bump2version](https://github.com/c4urself/bump2version/) for instructions
2. Checkout master branch
3. Run `bumpversion patch` (or `major` or `minor`) - this will bum the version in `.bumpversion.cfg` and `__version__.py` add create a new tag.
4. Run `git push && git push --tags` - this will trigger tagged action build