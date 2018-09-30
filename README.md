# Pocket Dictionary

[![Build Status](https://travis-ci.org/sunghyunzz/pocket-dictionary.svg?branch=master)](https://travis-ci.org/sunghyunzz/pocket-dictionary) 
[![PyPI](https://img.shields.io/pypi/v/pocket-dictionary.svg)](https://pypi.org/project/pocket-dictionary/) 
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pocket-dictionary.svg)](https://pypi.org/project/pocket-dictionary/) 
[![PyPI - License](https://img.shields.io/pypi/l/pocket-dictionary.svg)](https://pypi.org/project/pocket-dictionary/)

Your handy `dict` for Python. Do not manually (de)serialize your Python classes. Just do it by calling `.dict` or `.json`.

## Getting Started

```python3
from pocket import dictionary


@dictionary
class Topping:
    name: str


@dictionary
class PizzaSlice:
    toppings: List[Topping]


p = PizzaSlice([Topping('pepperoni'), Topping('cheese')]
p.dict  # {'toppings': [{'name': 'pepperoni'}, {'name': 'cheese'}]}
p.json  # '{"toppings": [{"name": "pepperoni"}, {"name": "cheese"}]}'
```

## Installation

```bash
pip install pocket-dictionary
```
