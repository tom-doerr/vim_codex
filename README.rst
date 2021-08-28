=============================
 Vim Codex 
=============================

.. image:: gifs/render1630099906410.gif

This is a simple plugin for Vim that will allow you to use OpenAI Codex.
To use this plugin you need to have access to OpenAIs Codex models.


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




After installing the plugin, you need to install the openai package::

  pip3 install openai

Finally add your OpenAI access information in 
``~/.vim/bundle/vim_codex/python/AUTH.py``.
You can find your authentication information on the website__.

__ https://beta.openai.com/account/api-keys

Usage
=====
The plugin provides a ``CreateCompletion`` command which you can call by default using the mapping 
``<Leader>co``.

To complete the current text from insert and normal mode using Ctrl+x, you can add the following
lines to your .vimrc::

  nmap  <C-x> :CreateCompletion<CR>
  imap  <C-x> <Esc>:CreateCompletion<CR>i



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
