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

    # print("vim.current.buffer:", vim.current.buffer)
    # input_prompt = ''
    # for i in range(5):
        # input_prompt += vim.current.buffer[i] + '\n'
    # print("input_prompt:", input_prompt)
        # vim.current.buffer[row-1+row_i] = new_lines[row_i]
        # if row_i == 0:
            # existing_text = vim.current.buffer[row-1]
        # else:
            # existing_text = ''
        # if row_i == 0:
            # vim.current.buffer[row] = existing_text + new_lines[row_i]
        # else:
            # vim.current.buffer[row-1:row-1] = [existing_text + new_lines[row_i]]

    # existing_text = current_line[:col]
def create_completion(): 
    vim_buf = vim.current.buffer
    vim_win = vim.current.window
    input_prompt = '\n'.join(vim_buf[:])
    # print(len(input_prompt.split('\n')))
    # for e in vim.current.buffer.range(0, 3):
        # print(e)
    
    row, col = vim.current.window.cursor
    input_prompt = '\n'.join(vim_buf[row:])
    input_prompt += '\n'.join(vim_buf[:row-2])
    input_prompt += '\n' + vim_buf[row-1][:col]
    # print("input_prompt:", input_prompt)

    response = openai.Completion.create(engine='davinci-codex', prompt=input_prompt, best_of=1, temperature=0.1, max_tokens=64)
    completion = response['choices'][0]['text']
    # print("completion:", completion)
    # print(len(buffer))
    current_line = vim.current.buffer[row-1]
    new_line = current_line[:col] + completion + current_line[col:]
    if new_line[-1] == '\n':
        new_line = new_line[:-1]
    # print("current_line[col:]:", current_line[col:])
    # vim.current.buffer[row-1] = new_line
    new_lines = new_line.split('\n')
    new_lines.reverse()
    # for row_i in range(row-1, row-1 + len(new_lines)):
        # vim.current.buffer[row_i-1] = new_lines[row_i - ]
    vim_buf[row-1] = None
    cursor_pos_base = tuple(vim_win.cursor)
    for row_i in range(len(new_lines)):
        vim.current.buffer[row-1:row-1] = [new_lines[row_i]]

    # print("cursor_pos_base[0] + row_i:", cursor_pos_base[0] + row_i)
    # print("len(new_lines[row_i]):", len(new_lines[row_i]))
    if new_line[-1] != '\n':
        cursor_target_col = len(new_lines[0])
    else:
        cursor_target_col = 0
    vim_win.cursor = (cursor_pos_base[0] + row_i + 1, cursor_target_col)


