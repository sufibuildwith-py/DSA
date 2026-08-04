class Solution {
public:
    vector<vector<int>> generate(int numRows) {

        vector<vector<int>> triangle;

        // If no rows are requested, return an empty triangle.
        if (numRows == 0) {
            return triangle;
        }

        // Generate one row at a time.
        for (int row = 0; row < numRows; row++) {

            // Every row contains (row + 1) elements.
            vector<int> currentRow(row + 1);

            // The first and last element of every row is always 1.
            currentRow[0] = 1;
            currentRow[row] = 1;

            // Fill the middle elements.
            // Each value is the sum of the two values directly above it.
            if (row > 1) {
                for (int col = 1; col < row; col++) {
                    currentRow[col] =
                        triangle[row - 1][col - 1] +
                        triangle[row - 1][col];
                }
            }

            // Store the completed row.
            triangle.push_back(currentRow);
        }

        return triangle;
    }
};