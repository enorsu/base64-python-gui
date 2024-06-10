import base64lib
import tkinter
import tkinter.ttk

root = tkinter.Tk()
root.title("Base64 Encoder/Decoder")
root.geometry("300x210")
root.resizable(False, False)

def encode():
    if selected_type.get() == 1:
        data_out.set(base64lib.encode1(data_in.get()))
    elif selected_type.get() == 2:
        data_out.set(base64lib.encode2(data_in.get()))

def decode():
    if selected_type.get() == 1:
        data_out.set(base64lib.decode1(data_in.get()))
    elif selected_type.get() == 2:
        data_out.set(base64lib.decode2(data_in.get()))


data_in = tkinter.StringVar()
data_out = tkinter.StringVar()
selected_type = tkinter.IntVar()

data_in_text = tkinter.Label(root, text="Data in")
data_in_text.pack()

data_in_entry = tkinter.Entry(root, textvariable=data_in, width=40)
data_in_entry.pack()



encode_button = tkinter.Button(root, text="Encode", command=encode)
encode_button.pack()

decode_button = tkinter.Button(root, text="Decode", command=decode)
decode_button.pack()

# radio buttons for encoding/decoding type

b64_radio = tkinter.Radiobutton(root, text="b64", variable=selected_type, value=1)
b64_radio.pack()

b32_radio = tkinter.Radiobutton(root, text="b32", variable=selected_type, value=2)
b32_radio.pack()

data_out_text = tkinter.Label(root, text="Data out")
data_out_text.pack()

data_out_text = tkinter.Entry(root, textvariable=data_out, state="readonly", width=40)
data_out_text.pack()


root.mainloop()

