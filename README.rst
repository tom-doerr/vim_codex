=============================
 Simple Vim Codex plugin
=============================

This is a simple plugin for Vim that will allow you to use OpenAI Codex.


Installation
============

The easiest way to install the plugin is to install it as a bundle.
For example, using Pathogen__:

1. Get and install `pathogen.vim <https://github.com/tpope/vim-pathogen>`_. You can skip this step
   if you already have it installed.

2. ``cd ~/.vim/bundle``

3. ``git clone git@github.com:tom-doerr/vim_codex.git``

__ https://github.com/tpope/vim-pathogen

Bundle installs are known to work fine also when using Vundle__. Other
bundle managers are expected to work as well.

__ https://github.com/gmarik/vundle



Updating
========

Manually
--------

In order to update the plugin, go to its bundle directory and use
Git to update it:

1. ``cd ~/.vim/bundle/vim_codex``

2. ``git pull``


With Vundle
-----------

Use the ``:BundleUpdate`` command provided by Vundle, for example invoking
Vim like this::

  % vim +BundleUpdate
