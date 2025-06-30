# Documentation for suspension.py

![](Pic/ViewCapture20250627_101409.jpg)

## General Description

The `suspension.py` file contains an algorithm for creating a suspension system from linear elements in Grasshopper/Rhino. The algorithm is designed for automatic generation of suspension structure taking into account geometric constraints and parameters.

**Version:** v0.06

## Main Functions

### 1. `sort_lines_perpendicular(lines, reference_direction)`
Sorts lines perpendicular to a given direction.

**Parameters:**
- `lines` - list of lines to sort
- `reference_direction` - reference direction (Vector3d)

**Returns:** sorted list of lines

### 2. `line_same_direction(lines)`
Aligns all lines in the same direction and sorts them perpendicularly.

**Parameters:**
- `lines` - list of lines

**Returns:** tuple (sorted lines, reference direction)

### 3. `suspension_corners(lines, dir, round, min_val, is_start)`
Generates suspension corner points taking into account rounding and minimum distance.

**Parameters:**
- `lines` - list of lines
- `dir` - direction
- `round` - rounding radius
- `min_val` - minimum distance
- `is_start` - whether these are starting points (True/False)

**Returns:** list of corner points

### 4. `strict_cluster_points(points, direction, max_distance, is_start=True)`
Groups points into clusters based on projection onto a given direction.

**Parameters:**
- `points` - list of points
- `direction` - direction for projection
- `max_distance` - maximum distance between points in a cluster
- `is_start` - whether these are starting points

**Returns:** tuple (group indices, representative points)

### 5. `project_points_to_group_scalar(points, group_ids, representative_points, direction)`
Projects points to their group representative points along a given direction.

**Parameters:**
- `points` - list of points
- `group_ids` - group indices for each point
- `representative_points` - representative points of groups
- `direction` - projection direction

**Returns:** list of aligned points

### 6. `grouped_polylines_by_index(points, group_indices)`
Creates polylines from points based on their group indices.

**Parameters:**
- `points` - list of points
- `group_indices` - group indices

**Returns:** tuple (polylines, individual points, one point for each group)

### 7. `connect_point_pairs(start_points, end_points)`
Creates lines between pairs of starting and ending points.

**Parameters:**
- `start_points` - starting points
- `end_points` - ending points

**Returns:** list of lines

### 8. `generate_crossbars_points(lines, max_step, group_points=None)`
Generates points for cross elements with uniform step. Supports two operation modes: using group points to determine projection range or classic mode.

**Parameters:**
- `lines` - list of lines
- `max_step` - maximum step between cross elements
- `group_points` - optional list of group points to determine projection range

**Returns:** list of point lists for cross elements

### 9. `remove_duplicate_points(points, min_distance=GLOBAL_TOL)`
Removes duplicate points that are closer than `min_distance`.

**Parameters:**
- `points` - list of points
- `min_distance` - minimum distance between points (default GLOBAL_TOL)

**Returns:** list of unique points

### 10. `build_segmented_lines(crossbars_points, max_distance)`
Creates segmented lines from cross element points.

**Parameters:**
- `crossbars_points` - cross element points
- `max_distance` - maximum distance between points in a segment

**Returns:** tuple (segmented lines, individual points)

### 11. `polylines_to_lines(poly_curves)`
Converts polylines to simple lines.

**Parameters:**
- `poly_curves` - list of polylines

**Returns:** list of lines

### 12. `match_support_to_boundary(support_lines, boundary_lines, direction, threshold)`
Matches support lines with boundary lines based on projection.

**Parameters:**
- `support_lines` - support lines
- `boundary_lines` - boundary lines
- `direction` - direction for projection
- `threshold` - distance threshold for matching

**Returns:** list of group indices for support lines

### 13. `move_line_to_match_projection(source_line, target_line, direction)`
Moves a line to match the projection of the target line.

**Parameters:**
- `source_line` - source line
- `target_line` - target line
- `direction` - projection direction

**Returns:** moved line

### 14. `filter_and_align_lines(boundary_lines, support_lines, support_indices, direction)`
Filters and aligns lines based on their matching. Selects the longest line in each group and aligns support lines with boundary lines.

**Parameters:**
- `boundary_lines` - boundary lines
- `support_lines` - support lines
- `support_indices` - matching indices
- `direction` - alignment direction

**Returns:** tuple (filtered boundary lines, filtered support lines)

### 15. `generate_points_on_lines(lines, step)`
Creates points on lines with a given step.

**Parameters:**
- `lines` - list of lines
- `step` - step between points

**Returns:** list of points on lines

### 16. `merge_lines_by_distance(lines, max_distance, length_tolerance=GLOBAL_TOL)`
Combines lines that are within a given distance and have the same length.

**Algorithm:**
1. Finds center points of all lines
2. Groups lines by distance between centers and length
3. For each group, leaves one line positioned at the center of the group

**Parameters:**
- `lines` - list of lines to combine
- `max_distance` - maximum distance for combination
- `length_tolerance` - allowable difference in line length for combination (default GLOBAL_TOL)

**Returns:** list of combined lines

**Note:** The function combines only those lines that are within `max_distance` of each other and have the same length (with tolerance `length_tolerance`). This helps reduce the number of duplicate elements in the suspension system.

## Global Constants

- `GLOBAL_TOL = 0.01` - global tolerance for distance comparisons

## Input Variables (for Grasshopper)

- `LINES` - input lines for processing
- `ROUNDING` - corner rounding radius
- `MIN_DISTANCE_CORNER` - minimum distance for corners
- `MAX_DISTANCE_CORNER` - maximum distance for grouping corners (intersection points)
- `SUSPENSION_STEP` - step between cross elements
- `MAX_DIST_B_PT_CENTER` - maximum distance between points in the center when building suspension lines
- `THRESHOLD_FILTER` - threshold for filtering lines (two types: those at corners and in the center)
- `RODS_STEP` - step between points for rods
- `DISTANCE_JOINING_START_END_LINES` - maximum distance for combining starting and ending lines

**Note:** `ROUNDING` + `MIN_DISTANCE_CORNER` = equals the offset from corners

## Output Variables

### Lines:
- `unistrut_lines` - all suspension lines (boundary + support)
- `boundary_lines_filtered` - filtered boundary lines
- `safe_support_lines_filtered` - filtered support lines

### Points:
- `rods_points` - points for rods on all suspension lines
- `single_rods_points` - individual points that do not form lines:
  - `start_lonely` - points at the beginning of a line
  - `end_lonely` - points at the end of a line
  - `orphaned_points` - points in the middle of lines

## Algorithm Operation

1. **Line Preparation:** Aligning all lines in the same direction
2. **Corner Generation:** Creating corner points taking into account rounding
3. **Clustering:** Grouping corner points by distance
4. **Alignment:** Projecting points to group representative points
5. **Polyline Creation:** Forming polylines from aligned points
6. **Boundary Line Combination:** Combining starting and ending lines that are within `DISTANCE_JOINING_START_END_LINES` and have the same length
7. **Cross Element Generation:** Creating cross elements with uniform step (with group point support)
8. **Segmentation:** Breaking cross elements into segments with duplicate removal
9. **Matching:** Matching support lines with boundary lines
10. **Filtering:** Selecting the longest lines in groups and aligning support lines
11. **Point Generation:** Creating points for rods on all lines

## New Features v0.06

- Improved `generate_crossbars_points` function with group point support
- Added `remove_duplicate_points` function for duplicate removal
- Improved filtering and line alignment logic
- Added `generate_points_on_lines` function for creating rod points
- Added `merge_lines_by_distance` function for combining lines by distance and length
- Extended output variables for more detailed control

