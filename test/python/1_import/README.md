## `1_import`

This test focuses on how `from`, `import`, and `as` keywords interact with the program and concerns 3 points: 

1. how to call functions from imported modules,
2. what conflicts (causes runtime error) and what doesn't conflict,
3. and a bit about the program flow of importing.

### Process

First part of the program (first few lines) import the modules `imported.py` and `subfolder/imported.py`. This naming is okay because the latter module is referred to as `subfolder.imported` (e.g. `imported.func1()` vs. `subfolder.imported.func1()`). A conflict can occur if `subfolder/imported.py` is imported via `import subfolder.imported as imported`. This conflict does not cause runtime error but simply overwrites the previously-imported `imported.py` module.

Like the vast majority of programming languages, Python executes from top to bottom. From a C/C++ perspective, `import` is not equivalent to `#include` due to it not being a direct transclusion. This is shown upon execution of the program as `__name__` is different for each imported module. Although not precisely technically correct, Python modules can be thought of as translation units in C/C++. See the value of `x` to understand that it is not transclusion.

`func1()` from `imported.py` is executed using `imported.func1()`. `func2()` is executed the same way, but can also be executed via `func2()` directly due to the line `from imported import func2`. `func3()` cannot be executed directly via `func3()` because there is no `from imported import func3`.

Previously, `from` and `import` is tested. By doing `from imported import func4 as f`, the function `func4()` from the `imported` module can be executed directly via `f()`. 

When further subfolders are concerned, for example importing another module of the same name `imported.py` within `subfolder` subfolder, the line `import subfolder.imported` is used and functions are called using `subfolder.imported.func1()` for example.

Additionally, dependencies are taken care of when doing `import`. For example: `from subfolder.dependency_test import functionWithDependency` imports only a single function, but that function has a dependency on `funcNotImported()` which isn't mentioned explicitly. Python takes care of this dependency without having to explicitly import `funcNotImported()` too.

### Side Note

The concatenation of `print()` can be done with `,` as in the case with `print("A", "B")` which prints `A B` and `+` as in the case with `print("A" + "B")` which prints `AB`.

The former method is more versatile as the arguments don't have to be the same type (for example `print("A", 1)` which prints `A 1`). The separator is an empty space as default but can be changed via the `sep` parameter within the print function (e.g. `print("A", 1, sep="ba")` which prints `Aba1`).

## `2_list of string`

`myList` is a list of 2 strings. To add 1 more string, use `myList.append(addedString)`. To append the string inside `myList`, you can use `myList[0] += "12"` to append `"12"` for example.

`myList` can be cleared using `myList = []`.

This test is done for the GPS sentence parser.