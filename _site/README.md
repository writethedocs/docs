## Write the Docs website

This is the code that powers [www.writethedocs.org](http://www.writethedocs.org). It contains information
about the Write the Docs group, as well as information about writing documentation.

To contribute to the Write the Docs website, it's helpful to familiarize yourself with the [Sphinx site generator](https://www.sphinx-doc.org/), as well as [reStructuredText markup syntax](https://www.sphinx-doc.org/en/stable/rest.html).

### Code Architecture

All of the generated website lives inside the `docs` directory, but many files outside the `conf/` directory are just static RST.
We are trying to move towards a more data driven approach,
which allows for easier maintenance and reuse of content between events.

#### Conference pages

We have a few important directories and files:

* `_data/config-portland-2019.yaml` - This file contains the data for rendering a specific conference.
* `_templates/2019/` - Contains the HTML templates for all conferences that year, including common pages and separate navigation menus.
* `conf/portland/2019/` - Contains the RST files that we use for rendering the conference. Copy these over from the *previous* conference chronologically, not the previous conference in the same location.
* `include/conf/` Contains the text snippets which are *mostly* the same between all conferences, mostly describing what our events are (eg. lightning talks and unconference). They are included via the RST files for each event. Now we've merged #738 we can add content that is conditional to each conference using Jinja.
* `_ext/core.py` Contains the Sphinx extensions that manage injecting custom variables into our RST and Jinja templates. Specifically the `rstjinja` and `load_page_yaml_data` functions do a lot of the work.

All files that live under the `conf` directory are rendered so as to have access to
 the data inside the `_data/config-<location>-<year>.yaml` file in the Jinja context for the RST files.
This allows us to say `{{ year }}` in the RST files,
and have it be rendered properly at `2019`.

### Videos

An even more fragile process which needs documenting and fixing.
### Prerequisites for generating the docs locally

You'll probably need `root` privileges to install the prerequisites.

1. Install `python 3.6.x` using your package manager.

2. Generate a virtual environment for the WTD repo in the `venv` directory:

    `virtualenv --python=/usr/bin/python3.6 venv`

### Installing the project requirements

1. Activate the virtual environment according to your operating system:

    * On Linux-based systems, run `source venv/bin/activate`.
    * On Windows using the Command Prompt, run `venv\Scripts\activate.bat`.
    * On Windows using PowerShell, run `. venv\Scripts\activate.ps1`.
    * On Windows using Git Bash, run `source venv\Scripts\activate`.

    You'll need to do this every time you come back to the project.

2. In the repository root directory (`www` by default), run `pip install -r requirements.txt` to install sphinx and other requirements.

### Previewing the docs locally

> Remember to activate the virtual environment using the appropriate command for your OS and Shell before running the following commands.

1. In the `docs` directory, run `make livehtml` to view the docs on [http://127.0.0.1:8888/](http://127.0.0.1:8888/).

If you're not seeing new content in the local preview, run `make clean` to delete the generated files, then `make livehtml` to regenerate them.

The Write the Docs website is hosted on [Read the Docs](https://readthedocs.org/projects/writethedocs-www).

### Previewing changes on Netlify

You can preview changes you've made on a pull request by clicking "Show all checks" at the bottom of the pull request page, and then clicking "Details" on the Netflify line, and navigating to the page you're making changes to.

### Updating the theme or css

If you need to update the theme, the original source is in

https://github.com/writethedocs/website-theme/

and instructions on how to update it are in the [`README.md`](https://github.com/writethedocs/website-theme/pull/3)

### Updating CSS for the 2018 Theme

The website for 2018 uses SASS to compile all the assets it has. To modify the theme, you must first install the dependencies of
`gulp`. In the main directory, run:

```
npm install
```

With that you will install all the requirements to minify your CSS;
after that you only need to run:

```
gulp
```

This has to be used alongside the sphinx server and it will
automatically minify all the content in your `.scss` files to the
`main.min.css` file. Also, `gulp` will be running browserify, allowing you
to see the CSS changes immediately in the browser.

### Generating new conf pages

#### Copy and Create

There are a few places you need to copy files from when spinning up a new conference site:

1. The *YAML config file*. For example, copy `docs/_data/config-portland-2018.yaml` to `docs/_data/config-prague-2018.yaml`.
   Edit the file as necessary.
2. The *conference directory*. For example `docs/conf/portland/2018` to `docs/conf/prague/2018`.
3. The *templates*. For example `docs/_templates/2018/base_na.html` **and** `docs/_templates/2018/na` to `docs/_templates/2018/base_eu.html` **and** `docs/_templates/2018/eu`.
4. You might need some local content in `docs/includes/conf` and `_static`. Sphinx will probably warn you if you do.

#### Search and replace

Search and replace any year specific stuff (CAREFUL)
```
portland/2018
```

Manually update any FIXME comments
```
.. FIXME
```

For this whole thing to work we still need to implement these

```
.. TODO
```
