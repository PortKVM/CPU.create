# CPU Creator

## Overview

The CPU Creator is a Python package for creating random CPU objects. It can be used to generate realistic CPU specifications for use in simulations, benchmarks, or other applications.

## Installation and Usage

To install the CPU Creator package, Download the cpu.py file from this repo and import it like this:
```python
import cpu
```

You can then use the `create_cpu()` function to generate a random CPU object. The `create_cpu()` function takes no arguments and returns a `CPU` object.

The `CPU` object has the following attributes:

* `name`: The name of the CPU.
* `cores`: The number of cores in the CPU.
* `speed`: The speed of the CPU in GHz.

You can access these attributes using dot notation. For example, to get the name of a CPU object, you would use the following code:

```python
cpu_name = cpu.name
```

You can also use the `print_cpu_info()` method to print the CPU's information to the console.

## Example

The following code shows how to use the CPU Creator package to generate and print information about three random CPUs:

```python
import cpu_creator

cpu1 = cpu_creator.create_cpu()
cpu2 = cpu_creator.create_cpu()
cpu3 = cpu_creator.create_cpu()

cpu1.print_cpu_info()
cpu2.print_cpu_info()
cpu3.print_cpu_info()
```

Output:

```
CPU Name: CPU-123
CPU Cores: 4
CPU Speed: 3.2 GHz
CPU Name: CPU-456
CPU Cores: 8
CPU Speed: 2.8 GHz
CPU Name: CPU-789
CPU Cores: 2
CPU Speed: 1.6 GHz
```
