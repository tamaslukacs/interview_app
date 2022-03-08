# InterviewApp - A BluePrism Interview Project

An interview project to showcase [Tamás'] python skills.

##Project Architecture

Reflecting on the application description, 
the following architectural decisions
and feature requirements are identified:
___

- **General Considerations**  

    - The latest Python distribution is used for development(3.10.2)
in order to maximise time before End-of-Life support.

    - However, backward-compatibility is maintained until python 3.7 by avoiding
new syntax only introducted in newer versions. (3.6 already reached EoL)

    - In terms of distribution, the easiest method for the end user is chosen, whereby
the the app is packaged and can be installed using **_setuptools_**.

    - There is a separate requirements_dev.txt for developer packages, e.g. for testing.

    - There are some extra logic included in the effort to show thinking out of the box,
i.e. providing logic for a not yet implemented GUI interface or different parsing mechanism
based on file extension. Best practice would be to separate these out in their own function and tests
but it is beyond the scope of this exercise.

    - In case there is no solution found, the app does not create a results file,
it would be illogical.

    - The original capitalisation of the words are not retained as it was not a strict requirement.
By default all words written to the result file will be capitalised.
___
- **Console Application**  

The app needs to accept and deal with user inputs using CLI.

The following packages are considered:

|  Package |                    Pro ✔                 |                 Contra ❌               |
|:--------:|:----------------------------------------:|:--------------------------------------:|
| argparse | built-in, most popular                   | basic, weak in nested parsing          |
|   click  | lazily composable, useful common helpers | has a learning curve to it             |
|  docopt  | relies on good documentation             | docopt is restricted to basic parsing. |
  
✅ **_click_** is chosen because its simplicity to use
and because there is no restriction on reliance on external modules.

The _options_ category of user input is chosen because it enforces
the user to pair up input choice and parameter, whereas an _argument_ could be without mentioning
parameter name and out of order user input would need to be handled.

The CLI part of the application should ensure correct input arguments are provided at the start.    
___

- **Input File Handling**

The app needs to deal with:

  - [x] basic file handling (existance check,read)
    - **_os_** library to check
    - ensure future extensibility in case different file types will be needed
  - [x] parsing,cleaning and verifying file contents
    - enable different formats for parsing
    - ensure encoding compatibility
  - [x] store data in memory optimally while it is being processed
    - huge dataset, lookup should be fast
  - [x] basic checks as to there is a possible solution to the problem
    - start and end word present in the data

The input file handling should load, parse, verify and clean data
such that the business logic already deals with an optimal data set.

___

- **Business Logic**

The app needs to deal with:

  - [x] deal with data(4 letter words) efficiently in the range of thousands
    - data should be in the format of !X! 
  - [x] should be easily expandable should the requirements change
    - ability to provide longest path
    - ability to provide all viable path
  - [x] should find shortest result -> iterate through all possibilities but find most optimal result -> chance to early terminate 
  - [x] multiple choices for routes to take
    - perfect for recursion
    - breath-first search approach will generally be able to terminate earlier with the shortest path

The core of the business logic should be a recursive breath-fist search algorithm which is highly customisable.
Early termination conditions should be set to optimise performance.

___

##**Results Handling**

The app needs to deal with:

- [x] basic file handling (permission checks,write)
- future expandability
- format and encoding

___

##**Testing**

Should provide unittest test cases with high coverage.

- [x] **_unittest_** built-in library is the simpliest way to write unittests (**_nose_** was also considered, but its not as well documented)
- [x] **_pytest_** has built in coverage check support and works well with unittest package
- [x] for compatibility check across different python distributions and OS' **_tox_** and 
**_tox_gh_** for gitlab actions integration is used.

___

##**Future Extensions / Improvements**

- [x] Multiprocessing can be explored as there can be as many separate processes
as the number of starting positions, that is any letter of the valid word i.e. 4.
I would also make use of shared memory (https://docs.python.org/3/library/multiprocessing.shared_memory.html)
between processes to tell each other in case one has reached a shorter solution that the
ongoing search. I would not use multithreading because of the GIL Lock. This
would however enforce a minimum python version of 3.8. Before this feature, sharing 

- [x] The performance can be significantly improved if there can be an agreement as to
what characters are valid i.e. only ascii letters without special characters (+-=).

- [x] Valid charlist can be obtained directly from the input file.

- [x] charset can be expanded upon to support Chinese characters

- [x] typehinting should be added to the project's functions.

- [x] Tests could be more visibly separated out i.e. separate forder under tests unit & integration

- [x] Instead of relying on static external resources for testing, 
**_tempfile_** can be used to generate test files dynamically

- [x] could use a logger instead of print statements in the future

- [x] can easily expand business logic
to work with different length words by exapanding
the user inputs in the CLI.

- [x] can implement different methods of output representation 
of the result, i.e. can return the list as a json for the web.

- [x] user might ask for longest possible path instead of shortest

- [x] user might ask for all possible path instead of just the shortest

___

##Project's structure

```
│   .gitignore                                  -> git ignore files
│   Makefile                                    -> makefile for make
│   pyproject.toml                              -> config file
│   README.md                                   -> documentation
│   requirements.txt                            -> requirements for normal user
│   requirements_dev.txt                        -> requirements for developer who wants to run tests too (default for now)
│   setup.cfg                                   -> more config for setuptools
│   setup.py                                    -> setup for setuptools
│   tox.ini                                     -> tox config
│
├───.github
│   └───workflows
│           tests.yml                           -> for gitlab actions 
│
├───src                                         -> package location
│   └───interview_app                           -> package name
│           cli.py                              -> CLI implementation
│           config.py                           -> contains global config vars
│           find_shortest_path_logic.py         -> business logic
│           input_parser.py                     -> deals with input IO
│           main.py                             -> contains main flow
│           output_writer.py                    -> deals with output IO
│           py.typed                            -> flag for typed
│           __init__.py                         
│
└───tests
    │   conftest.py                             -> enable loading helpers for tests
    │
    ├───helpers
    │       fixtures.py                         ->fixtures
    │       tutils.py                           ->helper utils for tests
    │
    ├───integration
    │       test_integ_main.py                  -> integration tests
    │       __init__.py
    │
    ├───resources                               -> resources for testing
    │       commas.csv
    │       empty.txt
    │       random_dll_file
    │       small_5_valid_5_invalid.txt
    │       small_5_valid_5_invalid_no_ext
    │       words-english.txt
    │
    └───unit                                    ->unittests
            test_cli.py
            test_find_shortest_path_logic.py
            test_input_parser.py
            test_main.py
            test_output_writer.py
            __init__.py
```

___
![Tests](https://github.com/tamaslukacs/interview_app/actions/workflows/tests.yml/badge.svg)
[Tamás']: https://tamaslukacs.github.io/