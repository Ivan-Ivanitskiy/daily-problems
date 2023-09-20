def num_connected_components(edges):
    regions = []
    
    for edge in edges:
        connected_to_existing_region = False

        for region in regions:
            if edge[0] in region or edge[1] in region:
                region.add(edge[0])
                region.add(edge[1])
                connected_to_existing_region = True
                break
        
        if not connected_to_existing_region:
            new_region = {edge[0], edge[1]}
            regions.append(new_region)

    # Merge regions if they have any common vertices
    i = 0
    while i < len(regions):
        j = i + 1
        while j < len(regions):
            if regions[i].intersection(regions[j]):
                regions[i].update(regions[j])
                regions.pop(j)
            else:
                j += 1
        i += 1
            
    return len(regions)

print(num_connected_components([(1, 2), (2, 3), (4, 1), (5, 6), (7, 8), (8, 9), (10, 3)]))
# Output: 3
