# Fat-Tree Network Generator

A Python implementation of a three-tier fat-tree network topology, based on Al-Fares, Loukissas, and Vahdat (2008).

Developed for the course “Communication Networks for AI Data Centers.”

## Current Features

- Generate core, aggregation, and edge switches, and hosts.
- Generate undirected links between the network components.
- Check that every host has one link and every switch has exactly `k` links in the topology before failures.
- Print the number of components and links.

Link-failure modeling, experiments, and result visualization are planned for the next stage.

## Topology

The parameter `k` is the number of ports per switch. It must be an even integer greater than or equal to 2.

The network contains:

- `k` pods.
- `k / 2` edge switches and `k / 2` aggregation switches per pod.
- `k / 2` hosts per edge switch.
- `(k / 2)^2` core switches.

Each edge switch connects to every aggregation switch in its pod. Aggregation switch `a` in each pod connects to every core switch in core group `a`.

The total number of hosts is `k^3 / 4`, and the total number of links, including host links, is `3k^3 / 4`.

Nodes are represented by unique names, and each undirected link is stored once as a pair of node names.

## Requirements

The current implementation uses only the Python standard library. It has been run with Python 3.8.10.

## How to Run

From the project directory:

```bash
python fat_tree.py
```

On Windows, if using a virtual environment named `.venv`:

```powershell
.\.venv\Scripts\python.exe fat_tree.py
```

To change the network size, edit the value of `k` in the `if __name__ == "__main__":` block at the bottom of `fat_tree.py`.

For example:

```python
k = 6
```

## Initial Validation

The following component and link counts were checked:

| k | Core switches | Edge switches | Aggregation switches | Hosts | Links |
| - | ------------: | ------------: | -------------------: | ----: | ----: |
| 4 |             4 |             8 |                    8 |    16 |    48 |
| 6 |             9 |            18 |                   18 |    54 |   162 |

The degree check passed for both configurations. Removing one link intentionally caused the check to report that both endpoints had one fewer connection than expected.

These checks verify component counts and node degrees. They do not yet independently verify all neighbor relationships or network connectivity.

## Reference

M. Al-Fares, A. Loukissas, and A. Vahdat, “A scalable, commodity data center network architecture,” SIGCOMM Computer Communication Review, vol. 38, no. 4, pp. 63–74, 2008.

DOI: [https://doi.org/10.1145/1402946.1402967](https://doi.org/10.1145/1402946.1402967)

## AI Assistance

OpenAI ChatGPT was used to explain the topology, assist with implementation and validation, troubleshoot Git setup, and draft this README.
