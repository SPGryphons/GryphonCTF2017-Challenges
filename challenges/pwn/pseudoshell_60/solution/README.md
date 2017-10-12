# PseudoShell
Aprils' Fool! It's not actually CIA servers. Disclaimer, `// Add one more to fgets for null byte` is not a real thing, you should always use the exact size minus 1 when using `fgets`.

For this challenge, it tests on the concept of stack following the structure of the code. Particularly, we want to focus on the `login()` function, with the variables `access` and `password`. When compiled, this is how they would behave like.

    [ PASSWORD - 16 bytes ]
    [ ACCESS - 4 byte ]

As you see, by writing 17 bytes, you would be enroaching onto the `access` variable. By simply overwriting that byte containing the initial `0xff`, you easily break the system.
