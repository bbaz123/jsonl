import tkinter as tk
from tkinter import filedialog
import json
import glob
import os

def merge_jsonl_files(input_dir, output_file):
    """合并指定目录下的所有 jsonl 文件。"""
    try:
        with open(output_file, 'w') as outfile:
            for filename in glob.glob(os.path.join(input_dir, '*.jsonl')):
                with open(filename, 'r') as infile:
                    for line in infile:
                        try:
                            data = json.loads(line)
                            json.dump(data, outfile)
                            outfile.write('\n')
                        except json.JSONDecodeError as e:
                            print(f"Skipping invalid JSON line in {filename}: {e}")
                            print(f"Invalid line: {line.strip()}")
        status_label.config(text="合并完成！")
    except Exception as e:
        status_label.config(text=f"发生错误: {e}")


def browse_input_folder():
    input_directory = filedialog.askdirectory()
    input_folder_entry.delete(0, tk.END)
    input_folder_entry.insert(0, input_directory)

def browse_output_file():
    output_filename = filedialog.asksaveasfilename(defaultextension=".jsonl")
    output_file_entry.delete(0, tk.END)
    output_file_entry.insert(0, output_filename)

def start_merge():
    input_dir = input_folder_entry.get()
    output_file = output_file_entry.get()
    if input_dir and output_file:
        merge_jsonl_files(input_dir, output_file)
    else:
        status_label.config(text="请选择输入文件夹和输出文件！")


root = tk.Tk()
root.title("JSONL 文件合并工具")

input_folder_label = tk.Label(root, text="输入文件夹:")
input_folder_label.grid(row=0, column=0, padx=5, pady=5)

input_folder_entry = tk.Entry(root, width=40)
input_folder_entry.grid(row=0, column=1, padx=5, pady=5)

input_folder_button = tk.Button(root, text="浏览", command=browse_input_folder)
input_folder_button.grid(row=0, column=2, padx=5, pady=5)

output_file_label = tk.Label(root, text="输出文件:")
output_file_label.grid(row=1, column=0, padx=5, pady=5)

output_file_entry = tk.Entry(root, width=40)
output_file_entry.grid(row=1, column=1, padx=5, pady=5)

output_file_button = tk.Button(root, text="浏览", command=browse_output_file)
output_file_button.grid(row=1, column=2, padx=5, pady=5)


merge_button = tk.Button(root, text="开始合并", command=start_merge)
merge_button.grid(row=2, column=1, pady=10)

status_label = tk.Label(root, text="")
status_label.grid(row=3, column=0, columnspan=3, pady=5)


root.mainloop()

