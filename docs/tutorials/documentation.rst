Documentation Tutorial
======================
This tutorial shows how to generate the documentation you are seeing right now using sphinx and its extensions.

Building the base docs
----------------------
To create the base of the docs you need to create the ``docs`` folder and run ``sphinx-quickstart`` in it.

**NOTE**: During the process, you will be asked if you want to have separate ``/docs/source`` and ``/docs/build``
folders. In my case I did **not** use separate folders. I wanted to have all the files directly in the ``/docs``
folder and have the builded html files in the ``/build`` folder **outside** of ``/docs``. (I'm considering as ``/`` the
root of this project).

Basic configuration
-------------------

Makefile
`````````
In order to build the docs in the ``build`` folder as I specified before, modify the ``Makefile`` with the following::

    BUILDDIR      = ../build/docs

**TIP**: In some cases, I have noticed that the docs were not updated correctly so I also added an ``rm`` to the make first::

    %: Makefile
    	if [ -d "$(BUILDDIR)" ]; then rm -R "$(BUILDDIR)"; fi
    	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

Now, you will be able to run ``make html`` in the ``docs`` folder and get your docs in ``build/html```. Congratulations!
(Open the file ``build/html/index.html`` to see them).

conf.py
```````
Edit the ``docs/conf.py`` and configure the following that you are interested in.

To be able to get the ``__author__``, ``__version__``, etc. directly from the package, add::

    import os
    import sys

    sys.path.insert(0, os.path.abspath('..'))

**NOTE**: notice that depending on where your package sources are located, you might need to point to a different place instead of ``'..'``.

This way you will be able to do something like this (after those lines)::

    from helloworld import __author__, __version__

    author = __author__
    version = __version__

In order to change the theme to the ReadTheDocs theme, add the line::

    html_theme = 'sphinx_rtd_theme'

TOC tree and adding a page
--------------------------
To create a table of contents referencing the pages ``docs/api/module1.rst`` and ``docs/api/module1.rst`` use::

    .. toctree::
        :maxdepth: 1
        :caption: API

        api/module1
        api/module2

The ``toctree``-s you define in ``index.rst`` will fill up the left sidebar. But, if you don't want them to be shown in
the ``index``'s content, you can addthe option ``:hidden:``.

**TIP**: if you want to automatically include all `.rst` files in a folder, do:

    .. toctree::
        :maxdepth: 1
        :caption: API
        :glob:

        api/*
Autodocumentation
-----------------
In order to create the automatic documentation using the ``docstrings`` from the code, you will need to add some extensions to sphinx. I have based my structure on ``pytorch`` and ``pytorch-lightning``'s docs. But, I hope that the notions written here allow customizing your docs in any way you want.

Configuration
`````````````
Edit the ``docs/conf.py`` with the following changes.

Add the following extensions::

    extensions = [
        'sphinx.ext.autodoc',
        'sphinx.ext.autosummary',
        'sphinx.ext.viewcode',
        'sphinx.ext.napoleon'
    ]

Brief explanation:
 - ``sphinx.ext.autodoc``: allows creating the docs based on the docstrings from the code.
 - ``sphinx.ext.autosummary``: allows creating concise content summary tables and link them to automatically generated `.rst` files for the modules, classes, functions etc.
 - ``sphinx.ext.viewcode``: creates a link to a view of the code.
 - ``sphinx.ext.napoleon``: allows using `Google Style <https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings>`_ docstrings.

**Autodoc configuration**: add these configurations to generate the automatic documentation as in this docs::

    autodoc_default_options = {
        'members': True,
        'undoc-members': True,
        'methods': True,
        'special-members': '__call__',
        'exclude-members': '_abc_impl',
        'show-inheritance': True,
    }

You can play around with the options.
Find the rest of the options `here <https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#confval-autodoc_default_options>`_.

**Autosummary configuration**: add the following lines to generate the ``autosummary`` files automatically and not overwrite them in each build (I
personally want the last one disabled in case I add some extra explanations)::

    autosummary_generate = True
    autosummary_generate_overwrite = False

Documenting the code
````````````````````
Now you will have to document your code using Google Style docstrings. However, as we have set
``'undoc-members': True`` in the ``autodoc`` options, you will be able to see changes even if you skip this step
for now.

Creating the .rst files
```````````````````````
Now you will have to tell ``autodoc`` and ``autosummary`` where and how to work. This exact documentation is organized
with ``.rst`` pages for each of the main modules and packages following ``pytorch``'s documentation's structure idea.
Feel free to explore this documentation's code or any other one you like. In this section, you will find the basics of
how they work.

If you would like to create them automatically, you can run (in the ``/docs`` folder):

.. code-block:: bash

   sphinx-apidoc -o api/ ../helloworld

This will generate the base API ``.rst`` files in ``/docs/api`` using the docstrings in the sources found in ``/helloworld``.
You can safely run this command even if some of the ``.rst`` have been created, because they will not be overwritten.

However, I personally prefer to write them manually using the following directives. Check this package's api ``.rst`` files to see an example.

**Autodoc**: writing a directive like::

    .. automodule:: helloworld

will generate all the automatic documentation of the referenced module, package, function, etc. like:

.. raw:: html

    <dl class="py function">
    <dt id="helloworld.say_hello">
    <code class="sig-prename descclassname">helloworld.</code><code class="sig-name descname">say_hello</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="reference internal" href="../_modules/helloworld.html#say_hello"><span class="viewcode-link">[source]</span></a><a class="headerlink" href="#helloworld.say_hello" title="Permalink to this definition">¶</a></dt>
    <dd><p>Say hello to the world or someone.</p>
    <dl class="field-list simple">
    <dt class="field-odd">Parameters</dt>
    <dd class="field-odd"><p><strong>name</strong> (<em>str</em>) – who you want to greet. If None it will greet the world.</p>
    </dd>
    <dt class="field-even">Returns</dt>
    <dd class="field-even"><p>A string with the greeting.</p>
    </dd>
    </dl>
    </dd></dl>


**Autosummary**: writing a directive like::

    \.. autosummary::
        :toctree: ./generated

        module1
        module2

    # NOTE: do not write the directive with \, I had to write it to escape it for this tutorial.

.. todo:: fix this.

will:

 - Generate a summary table like the following:

    .. raw:: html

        <table class="longtable docutils align-default">
        <colgroup>
        <col style="width: 10%">
        <col style="width: 90%">
        </colgroup>
        <tbody>
        <tr class="row-odd"><td><p><code class="xref py py-obj docutils literal notranslate"><span class="pre">module1</span></code></p></td>
        <td><p>Module 1.</p></td>
        </tr>
        <tr class="row-odd"><td><p><code class="xref py py-obj docutils literal notranslate"><span class="pre">module2</span></code></p></td>
        <td><p>Module 2.</p></td>
        </tr>
        </tbody>
        </table>

 - Will generate ``.rst`` pages for each of them in the folder``./generated``.
 - The generated pages will have another ``autosummary`` and ``automodule`` directives.
 - And will link them from the summary table.

Extras
------
Some extra possibilities you might find interesting to explore:

 - You can modify the templates used for generating the ``autosummary`` based files. Find the originals in the
   `sphinx repo <https://github.com/sphinx-doc/sphinx/tree/3.x/sphinx/ext/autosummary/templates/autosummary>`_ and
   place your modificated ones in ``docs/_templates/autosummary/`` with the same name than originals.


References
----------
- Autodocumenting your Python code with Sphinx (Roman Miroshnychenko): `part1 <https://romanvm.pythonanywhere.com/post/autodocumenting-your-python-code-sphinx-part-i-5/>`_ `part2 <https://romanvm.pythonanywhere.com/post/autodocumenting-your-python-code-sphinx-part-ii-6/>`_
- `Read The Docs <https://docs.readthedocs.io/en/stable/index.html>`_
- Sphinx Docs: `restructuredtext <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_
- Sphinx Docs: `autosummary <https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html>`_
- Sphinx Docs: `autodoc <https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`_
- `PyTorch <https://github.com/pytorch/pytorch/tree/master/docs>`_
- `PyTorch Lightning <https://github.com/PyTorchLightning/pytorch-lightning/tree/master/docs>`_
