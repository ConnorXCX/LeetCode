# Pacific Atlantic Water Flow

There is an `m x n` rectangular island that borders both the **Pacific Ocean** and **Atlantic Ocean**. The **Pacific Ocean** touches the island's left and top edges, and the **Atlantic Ocean** touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an `m x n` integer matrix `heights` where `heights[r][c]` represents the **height above sea level** of the cell at coordinate `(r, c)`.

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is **less than or equal to** the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return _a **2D list** of grid coordinates_ `result` _where_ <code>result[i] = [r<sub>i</sub>, c<sub>i</sub>]</code> _denotes that rain water can flow from cell_ <code>(r<sub>i</sub>, c<sub>i</sub>)</code> _to **both** the Pacific and Atlantic oceans_.

---

##### Example 1 Visualization

![Example 1 Visualization](waterflow-grid.jpg "Example 1 Visualization")
