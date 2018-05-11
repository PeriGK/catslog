# catslog

## About
A python package which, as implied by it's name, does two things. Logs(function execution along with the arguments passed) and catch(es) a potential exception. It is a name combination of two things people love. [(Chocolate)logs](https://www.bbcgoodfood.com/recipes/8767/yummy-chocolate-log) and [cats](https://www.youtube.com/watch?v=5dsGWM5XGdg).

## Why are you occupying bits from the internetz(original goal)?
The original goal, was to get rid of some boilerplate code, because I noticed "too many functions" in my statistical sample, follow the pattern:

- Enter function body
- Log stuff
- Catch potential exceptions

Also, this could help prettifying your code, as a result

## I love it, how do I install it?

`pip install catslog`
You might need to use `pip3` and/or `sudo`, depending on your setup.
I.e
`sudo pip3 install catslog`

## How do I use it
```
# First import the package
from catslog import catslog
# Then, decorate a target function
@catslog
def cats_me_if_you_can(*args, **kwargs):
 # Moar code
```

## I have python 1.3, will it work?
Unfortunately no. I have developed it and tested it, using python3. But if you have done it, please check the next section. I am more than happy to hear from you.

## I have forked your repository and extended it a bit. Do you want to take a look?
Thats great,feel free to raise a pull request and I will have a look asap.

## How to build from source
Pretty simple.
First build the package:
```
python setup.py bdist_wheel
```
and then install the local build
```
pip install -e .
```
