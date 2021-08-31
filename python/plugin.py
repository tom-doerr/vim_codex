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
USE_STREAM_FEATURE = True

def complete_input_max_length(input_prompt, max_input_length=MAX_SUPPORTED_INPUT_LENGTH):
    input_prompt = input_prompt[-max_input_length:]

    response = openai.Completion.create(engine='davinci-codex', prompt=input_prompt, best_of=1, temperature=0.5, max_tokens=128, stream=USE_STREAM_FEATURE)
    return response

def complete_input(input_prompt):
    try:
        response = complete_input_max_length(input_prompt, int(2.5 * MAX_SUPPORTED_INPUT_LENGTH))
    except openai.error.InvalidRequestError:
        response = complete_input_max_length(input_prompt, MAX_SUPPORTED_INPUT_LENGTH)
        # print('Using shorter input.')

    return response


def create_completion(): 
    vim_buf = vim.current.buffer
    input_prompt = '\n'.join(vim_buf[:])
    
    row, col = vim.current.window.cursor
    input_prompt = '\n'.join(vim_buf[row:])
    input_prompt += '\n'.join(vim_buf[:row-1])
    input_prompt += '\n' + vim_buf[row-1][:col]
    response = complete_input(input_prompt)
    write_response(response)

def write_response(response):
    vim_buf = vim.current.buffer
    vim_win = vim.current.window
    while True:
        if USE_STREAM_FEATURE:
            single_response = next(response)
        else:
            single_response = response
        completion = single_response['choices'][0]['text']
        row, col = vim.current.window.cursor
        current_line = vim.current.buffer[row-1]
        new_line = current_line[:col] + completion + current_line[col:]
        if not USE_STREAM_FEATURE:
            if new_line == '':
                new_line = new_line
            elif new_line[-1] == '\n':
                new_line = new_line[:-1]
        new_lines = new_line.split('\n')
        new_lines.reverse()
        if len(vim_buf) == row:
            vim_buf.append('')
               
        vim_buf[row-1] = None
        cursor_pos_base = tuple(vim_win.cursor)
        for row_i in range(len(new_lines)):
            vim.current.buffer[row-1:row-1] = [new_lines[row_i]]

        if new_line == '':
            cursor_target_col = 0
        elif new_line[-1] != '\n':
            cursor_target_col = len(new_lines[0])
        else:
            cursor_target_col = 0
        vim_win.cursor = (cursor_pos_base[0] + row_i, cursor_target_col)

        if not USE_STREAM_FEATURE:
            break

        # Flush the vim buffer.
        vim.command("redraw")
        if USE_STREAM_FEATURE:
            if single_response['choices'][0]['finish_reason'] != None: break


