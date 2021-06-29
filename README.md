## Write the Docs website

This is the code that powers [www.writethedocs.org](http://www.writethedocs.org). It contains information about the Write the Docs group, as well as information about writing documentation.

To contribute to the Write the Docs website, it's helpful to familiarize yourself with the [Sphinx site generator](https://www.sphinx-doc.org/), as well as [reStructuredText markup syntax](https://www.sphinx-doc.org/en/stable/rest.html).

### Code Architecture

All of the generated website lives inside the `docs` directory, but many files outside the `conf/` directory are just static RST, as in any other Sphinx project.

All RST files are rendered with [Jinja](https://jinja.palletsprojects.com/), which allows the use of Jinja tags in all of them. A few custom Jinja filters are available for things like generating photo paths for speakers.

### Conference pages

For conferences, see [the conference site documentation](https://www.writethedocs.org/organizer-guide/confs/website/).

### Videos

An even more fragile process that needs documenting and fixing.

WIP (Work In Progress) Docs on how to do this:

1. In `_data/<year>.<city>.speakers.yaml`, add a `youtubeId: 12345678901` key value pair to each talk.

2. Make sure the directory `videos/<city>/<year>` is included in the Video Archive `toctree` in `docs/videos/index.rst`.

3. In the [virtual environment](#prerequisites-for-generating-the-docs-locally), switch to the `docs` directory and run `BUILD_VIDEOS=True make html`.

4. Commit the *relevant* changed files:

   * `docs/videos/index.rst`
   * `_data/<year>.<city>.speakers.yaml`
   * `docs/videos/<city>/<year>/*`

5. If you want to preview locally:

    1. Run `BUILD_VIDEOS=True make livehtml` and browse the new video pages at `http://127.0.0.1:8888`.

#### Troubleshooting

If you run into trouble with broken links to video files, have a look at `_ext/fix_video_yaml.py`:

1. Add a line at the end with the relevant places and dates.

2. Change to the `_ext` directory and run it:

   `python fix_video_yaml.py`

3. Commit the fixed `_data/<year>.<city>.speakers.yaml` file.

### Prerequisites for generating the docs locally

1. Install `python 3.6.x` using your package manager, if not installed already. You'll probably need `root` privileges to do this.

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

1. In the `docs` directory, run `make livehtml` to view the docs on <http://127.0.0.1:8888/>.

If you're not seeing new content in the local preview, run `make clean` to delete the generated files, then `make livehtml` to regenerate them.

The Write the Docs website is hosted on [Read the Docs](https://readthedocs.org/projects/writethedocs-www).

### Previewing changes on Netlify

You can preview changes you've made on a pull request by clicking "Show all checks" at the bottom of the pull request page, and then clicking "Details" on the Netflify line, and navigating to the page you're making changes to.

### Updating the theme or CSS

If you need to update the theme, the original source is in

https://github.com/writethedocs/website-theme/

and instructions on how to update it are in the [`README.md`](https://github.com/writethedocs/website-theme/pull/3).

### Updating CSS for the 2018 Theme

The website for 2018 uses SASS to compile all the assets it has. To modify the theme, you must first install the dependencies of
`gulp`. In the main directory, run:

`npm install`

With that you will install all the requirements to minify your CSS;
after that you only need to run:

```
# Generate everything and serve site
gulp

# Only generate assets
gulp styles
```

This has to be used alongside the sphinx server and it will
automatically minify all the content in your `.scss` files to the
`main.min.css` file. Also, `gulp` will be running browserify, allowing you
to see the CSS changes immediately in the browser.

### Deactivating venv

After your work is complete, you can save resources by deactivating the
virtual Python environment with the following command on Linux:

`deactivate`

If you have verified this command on MacOS or Windows, we invite you to submit a PR to include that information here.

[![Greenkeeper badge](https://badges.greenkeeper.io/writethedocs/www.svg)](https://greenkeeper.io/)

## Style guide

* Use `Wi-Fi` not `wifi` or `Wifi`
