# Linux C Compiler
This is a Linux C Compiler I made from scratch in Python, it generates assembly code from C source code.

## Prerequisites:
You need GCC installed in your system and Python and Pyinstaller.

## How to build from source:

You need to build with pyinstaller and build cd.py:

```
pyinstaller path/to/cd.py
```

This will build the compiler driver with the compiler inside for your architecture host.

## Testing

I tested the compiler against a Test Suite of many test cases. So it works.

![Screenshot 2025-06-11 174118](https://github.com/user-attachments/assets/2dd0346a-8c94-4f6c-bcb6-278d7856f37a)


## How to use the compiler 
```
./path/to/cd --lastStage --noLink -lLibraryName path/to/cFile.c 
```

## Compiler Design
These are the compiler passes I made for the compiler:

<img width="242" alt="compiler_passes" src="https://github.com/user-attachments/assets/58b2c401-b813-4a6c-a456-e6a39018c0b2" />
