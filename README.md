<h1 align="center">🤖 Vim Codex</h1>

<p align="center">
    An AI plugin that does the work for you.
</p>

<p align="center">
    <a href="https://github.com/tom-doerr/vim_codex/stargazers"
        ><img
            src="https://img.shields.io/github/stars/tom-doerr/vim_codex?colorA=2c2837&colorB=b9c4e3&style=for-the-badge&logo=starship style=flat-square"
            alt="Repository's starts"
    /></a>
    <a href="https://github.com/tom-doerr/vim_codex/issues"
        ><img
            src="https://img.shields.io/github/issues-raw/tom-doerr/vim_codex?colorA=2c2837&&style=for-the-badge&logo=starship style=flat-square"
            alt="Issues"
    /></a>
    <a href="https://github.com/tom-doerr/vim_codex/blob/main/LICENSE"
        ><img
            src="https://img.shields.io/github/license/tom-doerr/vim_codex?colorA=2c2837&colorB=b9c4e3&style=for-the-badge&logo=starship style=flat-square"
            alt="License"
    /><br />
</p>

<p align="center">
    <img src='gifs/render1630418854684.gif'>
</p>

This is a simple plugin for Vim that will allow you to use OpenAI Codex.
To use this plugin you need to get access to OpenAI's [Codex API](https://openai.com/blog/openai-codex/).



## Installation

The easiest way to install the plugin is to install it as a bundle.
For example, using [Pathogen](https://github.com/tpope/vim-pathogen):

1. Get and install [pathogen.vim](https://github.com/tpope/vim-pathogen). You can skip this step
   if you already have it installed.

2. `cd ~/.vim/bundle`

3. `git clone git@github.com:tom-doerr/vim_codex.git`

Bundle installs are known to work fine also when using [Vundle](https://github.com/gmarik/vundle). Other
bundle managers are expected to work as well.



After installing the plugin, you need to install the openai package::
```
pip3 install openai
```

After running `:CreateCompletion` once, the file `~/.config/openaiapirc` is created where you need to enter your OpenAI authentication information.
You can find your authentication information on the [website](https://beta.openai.com/account/api-keys).



## Usage
The plugin provides a `CreateCompletion` command which you can call by default using the mapping 
`<Leader>co`.
You can give the `CreateCompletion` command the number of tokens it should produce as an argument, e.g. `CreateCompletion 1000`.
If you want to just complete the current line, run `CreateCompletionLine`.

To complete the current text from insert and normal mode using Ctrl+x, you can add the following
lines to your .vimrc::
```
nnoremap  <C-x> :CreateCompletion<CR>
inoremap  <C-x> <Esc>li<C-g>u<Esc>l:CreateCompletion<CR>
```


## Updating

### Manually

In order to update the plugin, go to its bundle directory and use
Git to update it:

1. `cd ~/.vim/bundle/vim_codex`

2. `git pull`


### With Vundle

Use the `:BundleUpdate` command provided by Vundle, for example invoking
Vim like this::
```
% vim +BundleUpdate
```



