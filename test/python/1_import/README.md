# Road-Monitoring-Device

## `1_import`

This test focuses on how `from`, `import`, and `as` keywords interact with the program and concerns 3 points: 

1. how to call functions from imported modules,
2. what conflicts (causes runtime error) and what doesn't conflict,
3. and a bit about the program flow of importing.

### Process

First part of the program (first few lines) import the modules `imported.py` and `subfolder/imported.py`. This naming is okay because the latter module is referred to as `subfolder.imported` (e.g. `imported.func1()` vs. `subfolder.imported.func1()`). A conflict can occur if `subfolder/imported.py` is imported via `import subfolder.imported as imported`. This conflict does not cause runtime error but simply overwrites the previously-imported `imported.py` module.

Like the vast majority of programming languages, Python executes from top to bottom. From a C/C++ perspective, `import` is not equivalent to `#include` due to it not being a direct transclusion. This is shown upon execution of the program as `__name__` is different for each imported module. Although not precisely technically correct, Python modules can be thought of as translation units in C/C++.

`func1()` from `imported.py` is executed using `imported.func1()`. `func2()` is executed the same way, but can also be executed via `func2()` directly due to the line `from imported import func2`. `func3()` cannot be executed directly via `func3()` because there is no `from imported import func3`.

Previously, `from` and `import` is tested. By doing `from imported import func4 as f`, the function `func4()` from the `imported` module can be executed directly via `f()`. 

When further subfolders are concerned, for example importing another module of the same name `imported.py` within `subfolder` subfolder, the line `import subfolder.imported` is used and functions are called using `subfolder.imported.func1()` for example.