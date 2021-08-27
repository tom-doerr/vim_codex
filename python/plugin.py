import urllib, urllib.request
import json

try:
  import vim
except:
  print("No vim module available outside vim")
  pass


import openai
from AUTH import *

openai.organization = ORGANIZATION_ID
openai.api_key = SECRET_KEY
MAX_SUPPORTED_INPUT_LENGTH = 4096

def create_completion(): 
    vim_buf = vim.current.buffer
    vim_win = vim.current.window
    input_prompt = '\n'.join(vim_buf[:])
    
    row, col = vim.current.window.cursor
    input_prompt = '\n'.join(vim_buf[row:])
    input_prompt += '\n'.join(vim_buf[:row-2])
    input_prompt += '\n' + vim_buf[row-1][:col]
    input_prompt = input_prompt[-MAX_SUPPORTED_INPUT_LENGTH:]

    response = openai.Completion.create(engine='davinci-codex', prompt=input_prompt, best_of=1, temperature=0.1, max_tokens=64)
    completion = response['choices'][0]['text']
    current_line = vim.current.buffer[row-1]
    new_line = current_line[:col] + completion + current_line[col:]
    if new_line[-1] == '\n':
        new_line = new_line[:-1]
    new_lines = new_line.split('\n')
    new_lines.reverse()
    vim_buf[row-1] = None
    cursor_pos_base = tuple(vim_win.cursor)
    for row_i in range(len(new_lines)):
        vim.current.buffer[row-1:row-1] = [new_lines[row_i]]

    if new_line[-1] != '\n':
        cursor_target_col = len(new_lines[0])
    else:
        cursor_target_col = 0
    vim_win.cursor = (cursor_pos_base[0] + row_i + 1, cursor_target_col)


