# Structure and Clustering Logic

## System Overview

This system is designed for analyzing and clustering three-dimensional objects (boxes):

1. **StructureObjects.py** - base class for working with geometric objects
2. **ClusteringAndFiltering.py** - clustering and filtering algorithms

## StructureObjects.py Module

### Structure Class

Main class for working with three-dimensional objects (boxes).

#### Constructor
```python
def __init__(self, geometry):
```
Accepts a geometric object (box) and initializes all properties:
- `geometry` - original geometry
- `corners` - box corners (8 points)
- `center` - object center
- `longest_edge` - longest edge
- `normalized_vector` - normalized direction vector
- `centered_longest_edge` - longest edge moved to center
- `volume` - volume
- `dimensions` - dimensions (length, width, height)
- `surface_area` - surface area

#### Geometry Analysis Methods

##### `_get_longest_edge()`
Finds the longest edge of the box among 12 possible edges:
- 4 bottom face edges: `(0,1), (1,2), (2,3), (3,0)`
- 4 top face edges: `(4,5), (5,6), (6,7), (7,4)`
- 4 vertical edges: `(0,4), (1,5), (2,6), (3,7)`

##### `_get_normalized_vector()`
Computes the normalized direction vector of the longest edge (length = 1).

##### `_get_centered_longest_edge()`
Moves the longest edge so that its center coincides with the object center.

##### `_get_center()`
Computes the box center as the arithmetic mean of all 8 corners.

##### `_get_dimensions()`
Computes box dimensions:
- Length: distance between corners 0 and 1
- Width: distance between corners 0 and 3
- Height: distance between corners 0 and 4

##### `_get_surface_area()`
Computes surface area using the formula: `2 * (length*width + length*height + width*height)`

##### `get_all_edges()`
Returns all box edges with their lengths and indices.

## ClusteringAndFiltering.py Module

### Alignment Filtering

#### `filter_structures_by_z_alignment()`
Filters structures based on perpendicularity to the Z axis:
- Computes dot product between `normalized_vector` and Z vector `(0,0,1)`
- Keeps only structures with dot product ≤ tolerance (default 0.1)
- This means only horizontally oriented structures remain

### Spatial Optimization

#### `create_spatial_grid()`
Creates a three-dimensional grid for fast neighbor search:
- Divides space into cells of size `grid_size`
- Each structure is placed in a cell based on the center of its `centered_longest_edge`
- Returns a dictionary with cell coordinates and lists of structure indices

#### `get_neighboring_cells()`
Returns coordinates of neighboring cells within a given radius.

#### `get_candidate_neighbors_from_grid()`
Gets a list of neighbor candidates for a given structure from the spatial grid.

### DBSCAN Clustering Algorithm

#### `dbscan_structures_by_centered_edges()`
Implements the DBSCAN algorithm for structure clustering:

**Parameters:**
- `eps` - neighbor search radius
- `min_pts` - minimum number of neighbors for a core point
- `grid_size` - spatial grid cell size

**Algorithm:**
1. Creates a spatial grid for optimization
2. For each structure, finds neighbors through `region_query()`
3. If number of neighbors ≥ `min_pts`, creates a new cluster
4. Expands cluster through breadth-first search
5. Structures without sufficient neighbors are marked as noise (-1)

**Distance Function:**
```python
def structure_distance(structA, structB):
```
Computes the minimum distance between `centered_longest_edge` of two structures through:
- Distances from points of one line to the other line
- Distances from points of the other line to the first line
- Returns the minimum of all distances

### Cluster Filtering

#### `filter_clusters_by_properties()`
Filters clusters based on object properties:

**Filtering Criteria:**
- `volume`: volume range (min, max)
- `surface_area`: surface area range (min, max)
- `dimensions`: dimension ranges (length, width, height)
- `longest_edge_length`: longest edge length range
- `min_cluster_size`: minimum number of objects in cluster
- `max_cluster_size`: maximum number of objects in cluster

#### `filter_clusters_by_z_height()`
Filters objects in clusters by Z coordinate height:
- Finds the highest Z coordinate in the cluster
- Removes objects that differ significantly in minimum height
- Uses percentage deviation from the highest point

### Analysis and Statistics

#### `get_cluster_statistics()`
Computes detailed statistics for clusters:
- Cluster size
- Minimum, maximum, and average values:
  - Volume
  - Surface area
  - Dimensions (length, width, height)
  - Longest edge length
- Returns result in JSON format

### Grasshopper Export

#### `create_structure_clusters_tree()`
Creates a Grasshopper tree from object geometry, grouped by clusters.

#### `create_centered_edges_tree()`
Creates a Grasshopper tree from `centered_longest_edge` objects, grouped by clusters.

## Main Execution Logic

1. **Creating Structure objects** from input boxes
2. **Alignment filtering** - only horizontally oriented structures remain
3. **DBSCAN clustering** - grouping structures by spatial proximity
4. **Cluster filtering** by properties (size, surface area, etc.)
5. **Height filtering** - removing objects with significantly different heights
6. **Exporting results** as Grasshopper trees

## Configuration Parameters

- `Z_TOLERANCE` - acceptable deviation for Z alignment filtering
- `DBSCAN_EPS` - neighbor search radius for DBSCAN
- `DBSCAN_MIN_PTS` - minimum number of neighbors for a core point
- `GRID_SIZE` - spatial grid cell size
- `MAX_HEIGHT_DIFFERENCE_PERCENT` - maximum height difference in percentage

## Output Data

- `out_structure_clusters_box` - tree with cluster geometry
- `out_structure_clusters_line` - tree with centered_longest_edge clusters
- `cluster_statistics` - JSON statistics for clusters (optional)
