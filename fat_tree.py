def create_core_switches(k):
    if k < 2 or k % 2 != 0:
        raise ValueError("k must be an even integer >= 2")

    core_switches = []

    for group in range(k // 2):
        for switch in range(k // 2):
            name = f"core_{group}_{switch}"
            core_switches.append(name)

    return core_switches

def create_pod_nodes(k):
    if k < 2 or k % 2 != 0:
        raise ValueError("k must be an even integer >= 2")

    edges = []
    aggregations = []
    hosts = []

    for pod in range(k):
        for switch in range(k // 2):
            edges.append(f"edge_{pod}_{switch}")
            aggregations.append(f"agg_{pod}_{switch}")

            for host in range(k // 2):
                hosts.append(f"host_{pod}_{switch}_{host}")

    return edges, aggregations, hosts

def create_links(k):
    if k < 2 or k % 2 != 0:
        raise ValueError("k must be an even integer >= 2")

    links = []
    half = k // 2

    for pod in range(k):
        # Connect each host to its edge switch
        for edge in range(half):
            edge_name = f"edge_{pod}_{edge}"

            for host in range(half):
                host_name = f"host_{pod}_{edge}_{host}"
                links.append((host_name, edge_name))

        # Connect every edge to every aggregation in this pod
        for edge in range(half):
            for agg in range(half):
                edge_name = f"edge_{pod}_{edge}"
                agg_name = f"agg_{pod}_{agg}"
                links.append((edge_name, agg_name))

        # Connect each aggregation to its core group
        for agg in range(half):
            for core in range(half):
                agg_name = f"agg_{pod}_{agg}"
                core_name = f"core_{agg}_{core}"
                links.append((agg_name, core_name))

    return links


def check_degrees(k, cores, edges, aggregations, hosts, links):
    nodes = cores + edges + aggregations + hosts
    degrees = {node: 0 for node in nodes}

    for first, second in links:
        degrees[first] += 1
        degrees[second] += 1

    errors = []

    for host in hosts:
        if degrees[host] != 1:
            errors.append(f"{host}: expected 1, got {degrees[host]}")

    for switch in cores + edges + aggregations:
        if degrees[switch] != k:
            errors.append(
                f"{switch}: expected {k}, got {degrees[switch]}"
            )

    if errors:
        raise ValueError("\n".join(errors))

    print("Degree check passed.")


# tests

if __name__ == "__main__":
    k = 6

    cores = create_core_switches(k)
    edges, aggregations, hosts = create_pod_nodes(k)

    print("Core switches:", len(cores))
    print("Edge switches:", len(edges))
    print("Aggregation switches:", len(aggregations))
    print("Hosts:", len(hosts))

    links = create_links(k)
    links.pop()
    check_degrees(k, cores, edges, aggregations, hosts, links)
    print("Links:", len(links))
    print("First links:", links[:5])