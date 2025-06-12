# C Compiler
This is a C Compiler I made in Python, it translates from C to x86 assembly language, I made it on Ubuntu Linux. I used GCC to assembly and preprocess the C File, then I compile it with my compiler and pass it to GAS for assembly.

These are the compiler passes I made for the compiler:

<img width="242" alt="compiler_passes" src="https://github.com/user-attachments/assets/58b2c401-b813-4a6c-a456-e6a39018c0b2" />

How to build from source:

You need to build with pyinstaller and build cd.py:


## Output

These is the ouput for an expression:

![Screenshot 2025-04-25 140518](https://github.com/user-attachments/assets/f782684a-2dda-487f-b897-01ce3d2f0be2)


## Debugging

This is the debugging of the assembly code with GDB:

![Screenshot 2025-04-22 155730](https://github.com/user-attachments/assets/b7737258-d355-4292-8990-f4cb6abb2c18)
