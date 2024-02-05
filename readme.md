# Counting Chord Intersections

This Python script calculates the number of intersections between chords in a circle, given their starting and ending points on the unit circle, denoted by radians, and their identifiers.

## Problem Statement

Given a series of chords on a unit circle, identified by their starting and ending radians, the task is to compute the total number of intersecting pairs of chords.

## Input Format

The input is provided as a tuple of two lists:
- A list of radians marking the positions on the unit circle.
- A list of identifiers indicating the start ('sX') or end ('eX') of a chord, where X is the chord's identifier.

Example input:
```python
input1 = [
    (0.78, 0.8, 0.9, 1.0, 1.2, 1.47, 1.77, 1.8, 3.0, 3.92),
    ('s1', 's5', 's3', 's4', 'e5', 's2', 'e1', 'e4', 'e3', 'e2')
]

## Approach

The algorithm executes in several steps:

### Chord Organization
- Map each chord's start and end radians using the provided identifiers.

### Sorting
- Sort the radians for each chord to ensure they are in ascending order.

### Intersection Counting
- For each chord, compare it against others to find intersecting pairs, incrementing the count accordingly.

## Implementation Details

The implementation involves creating a dictionary to track the start and end points of each chord, then iterating over each pair of chords to check for intersections. The intersection logic checks if one chord starts or ends within the span of another chord but does not lie entirely within it.

## Complexity Analysis

The algorithm has a time complexity of O(n^2), primarily due to the nested loop used to compare each chord against all others for potential intersections. This quadratic complexity arises from:

- An outer loop iterating through each chord.
- An inner loop comparing each selected chord with the rest.

Due to this, the algorithm's performance may degrade with large input sizes, making it less practical for scenarios with a high number of chords.

## Conclusion

While effective for calculating the number of intersecting chords in a circle, this implementation is best suited for smaller datasets due to its O(n^2) complexity. For larger datasets, alternative algorithms with better time complexity should be considered.
