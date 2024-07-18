# Ongoing-Project-Software-Modularization-for-Better-Code-Understanding
This repository contains the ongoing development of our software modularization project aimed at improving code understanding. The code and documentation provided here are part of an active research project conducted by the Software Maintenance Laboratory at the University of Tabriz.
Software Modularization Project

Project Overview

This project aims to facilitate the modularization (clustering) of software systems to enhance code comprehension. Below are the main steps involved in the software modularization process:

Steps for Software Modularization

1- Extracting Dependency Graphs:

Use tools such as Understand or NDepend to analyze the source code and extract the dependency graph of the software system.
These tools will generate a visual representation of how different parts of the code are interrelated.

2- Clustering the Dependency Graph:

Input the extracted dependency graph into a clustering algorithm.
The algorithm will process the graph and group related code artifacts into clusters (modules).

3- Evaluating the Clusters:

Evaluate the generated clusters using internal and external clustering metrics.
Internal metrics assess the cohesiveness within clusters and the separation between clusters.
External metrics compare the generated clusters to a known ground truth or expert modularizations.

4- Visualizing the Clusters:

Use graph visualization tools to display the resulting clusters for developers.
These visualizations help developers understand the modular structure and dependencies within the code.

How to Use

Prerequisites

Install Understand or NDepend for dependency graph extraction.

Ensure you have Python installed for running the clustering algorithms and evaluation metrics.

Install graph visualization tools such as Gephi or Cytoscape.

Instructions

Extract Dependency Graphs:

Analyze your software code using Understand or NDepend.
Export the dependency graph in a suitable format (e.g., GraphML, GML).

Run Clustering Algorithm:

Evaluate Clusters:

Evaluate the generated clusters using internal and external metrics:

Load the clustered graph into a graph visualization tool (e.g., Gephi).

Analyze the visual representation of the clusters.

Contribution

We welcome contributions from the community. If you're interested in contributing, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

Contact

For any questions or further information, please contact the Software Maintenance Laboratory at the University of Tabriz.
