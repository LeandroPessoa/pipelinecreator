# pipelinecreator - Plumber for the Luigi Framework
Graphical pipeline creator for luigi framework using NetworkX.


Let's be a plumber for the Luigi Framework pipelines (https://github.com/spotify/luigi).

The Luigi Framework gives a dependency graph as the graphical representation of pipeline designed directly in code (on web interface), however this graph is just to see the acomplishement and status of tasks that lies in pipeline.

Why not develop the graph in the beginning of the project to specify the sketch of pipeline that will be run rather than develop directly in code?

## #1 Goal
- Use networkX to define tasks and dependencies from it.
- Generate a graphical representation of a graph to give an overview of pipeline.
- Generate Luigi code of graph specified.
