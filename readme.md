# Python Parallel Programming

# (**1**) Introduction

## (**1.1**) [The Parallel Computing Memory Architecture](1.1-TheParallelComputingMemoryArchitecture.md)
## (**1.2**) Memory Organization

### Memory Organization - An Introduction
- Memory organization - The way in which the data is access
- The main problem - Making the response time of the memory compatible with the speed of the processor
- When the processor starts transferring data, the memory will remain occupied for the entire time of the **memory cycle**
- Memory cycle time is defined as the time elapsed bewteen two successive operations
- During data transferring, no device, I/O driver, processor or even processor itself may request the use of memory.
Because the memory is commited to response to the original request.

### The Memory Organization in MIMD Architecture

    [ MIMD ]
        ├───────────────────────────────────────────────┐
    [ Distributed Memory ]                      [ Shared Memory ]
        ├──────────────────┐                            ├──────────┬────────────┬──────────┐
    [ MPP ]     [ Cluster of Workstation]           [ UMA ]     [ NUMA ]    [ NORMA ]   [ COMA ]

### Shared Versus Distributed Memory
- If a processor were to execute the instruction [load R0, i], which means load in the R0 register the contents of the memory location i, the question now is what should happen

|Shared Memory|Distributed Memory|
|:-|:-|
|The **'i'** index is a global address and the memory location **'i'** is the same for each processor| i is a local address|

**(To be continue ... )**

# Reference:

1. **Python Parallel Programming Solutions**
by Giancarlo Zaccone, Packt Publishing, 2016

2. **Python High Performance - Second Edition**
by Gabriele Lanaro, Packt Publishing, May 2017
