float[][] invertMatrix(float[][] matrix) {
  int n = matrix.length;

  // Augment the matrix with the identity matrix
  float[][] augmentedMatrix = new float[n][2 * n];
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      augmentedMatrix[i][j] = matrix[i][j];
      augmentedMatrix[i][j + n] = (i == j) ? 1 : 0;
    }
  }

  // Perform Gaussian elimination
  for (int i = 0; i < n; i++) {
    float pivot = augmentedMatrix[i][i];

    if (pivot == 0) {
      return null; // Matrix is not invertible
    }

    // Scale the current row to make the pivot 1
    for (int j = 0; j < 2 * n; j++) {
      augmentedMatrix[i][j] /= pivot;
    }

    // Eliminate other rows
    for (int k = 0; k < n; k++) {
      if (k != i) {
        float factor = augmentedMatrix[k][i];
        for (int j = 0; j < 2 * n; j++) {
          augmentedMatrix[k][j] -= factor * augmentedMatrix[i][j];
        }
      }
    }
  }

  // Extract the inverted matrix
  float[][] invertedMatrix = new float[n][n];
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      invertedMatrix[i][j] = augmentedMatrix[i][j + n];
    }
  }

  return invertedMatrix;
}

float[][] multiplyMatrices(float[][] matrixA, float[][] matrixB) {
  int rowsA = matrixA.length;
  int colsA = matrixA[0].length;
  int rowsB = matrixB.length;
  int colsB = matrixB[0].length;

  // Check if matrices can be multiplied
  if (colsA != rowsB) {
    return null; // Matrix multiplication is not possible
  }

  // Initialize the result matrix
  float[][] resultMatrix = new float[rowsA][colsB];

  // Perform matrix multiplication
  for (int i = 0; i < rowsA; i++) {
    for (int j = 0; j < colsB; j++) {
      float sum = 0;
      for (int k = 0; k < colsA; k++) {
        sum += matrixA[i][k] * matrixB[k][j];
      }
      resultMatrix[i][j] = sum;
    }
  }

  return resultMatrix;
}
