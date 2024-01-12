When testing with smaller maps, the results I got were
expected. See output for lava_map2.
For the BFS algorithm, its logical, that the iteration count is the highest.
Also the paths are likely to be all the same, as the map is small.
The time spent is theoretically also higher for BFS, as the iteration count is bigger, because BFS explores all the nodes.

As can see the BFS outputs only 1 path.
But the greedy and A* output 2 paths, because heuristically the paths
are equal.

But when I tested on the bigger mazes, the iterations did not 
match with the expected theoretical results. A* and Greedy BFS
should ideally visit less nodes to find the path, therefore the iteration
count should be lower. Although the BFS search is ended as soon as the goal
is found. So the A* and Greedy BFS might take longer in complex mazes.

Path costs match up with the ones that are posted on Moodle.
But on greedy search the path costs is almost double on bigger mazes.
The reason for that is unknown for me at the moment.

Overall the exercise was fun, in terms of learning Python, getting more
experience with data strcutures and algorithms.

Also it was very satisfying to see the final algorithms visually showing the paths from start to goal.

!!! When ran, printSolution() should create new files with printed visuals of !!!

OUTPUTS:

    LAVA_MAP2:

    Path cost bfs: 16
    Time spent BFS: 0.000 ms, Iterations:113

    Path cost greedy: 16
    Time spent Greedy: 0.000 ms, Iterations:43

    Path cost astar: 16
    Time spent A*: 0.000 ms, Iterations:54

MAP OUTPUT LAVA_MAP2:

    BFS:

    |      **             .......   |
    |     ***             .***  D   |
    |     ***             .  ***** *|
    |                     .   **** *|
    |                s.....         |

    Greedy/A*:

    |      **        ............   |
    |     ***        .    .***  D   |
    |     ***        .    .  ***** *|
    |                .    .   **** *|
    |                s.....         |

OUTPUTS:

    Cave300x300:

    Path cost bfs: 554
    Time spent BFS: 222.405 ms, Iterations:47264

    Path cost greedy: 1068
    Time spent Greedy: 271.274 ms, Iterations:48599

    Path cost astar: 554
    Time spent A*: 573.467 ms, Iterations:88579

    cave600x600:

    Path cost bfs: 1247
    Time spent BFS: 921.537 ms, Iterations:197806

    Path cost greedy: 2173
    Time spent Greedy: 1154.912 ms, Iterations:197825

    Path cost astar: 1247
    Time spent A*: 2784.556 ms, Iterations:406667

    cave900x900: 

    Path cost bfs: 1843
    Time spent BFS: 2094.401 ms, Iterations:450448

    Path cost greedy: 3937
    Time spent Greedy: 2659.889 ms, Iterations:455325

    Path cost astar: 1843
    Time spent A*: 7887.913 ms, Iterations:1111982

