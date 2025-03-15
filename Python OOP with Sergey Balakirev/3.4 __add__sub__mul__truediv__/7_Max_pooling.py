class MaxPooling:
    def __init__(self, step=(2, 2), size=(2, 2)):
        self.step = step
        self.size = size

    def __call__(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0
        if rows == 0:
            return [[]]

        if not all(map(lambda x: len(x) == cols, matrix)) or not all(
            map(lambda row: all(map(lambda x: type(x) in (int, float), row)), matrix)
        ):
            raise ValueError("Неверный формат для первого параметра matrix.")

        sh, sw = self.step
        h, w = self.size

        rows_range = (rows - h) // sh + 1
        cols_range = (cols - w) // sw + 1

        res = [[0] * cols_range for _ in range(rows_range)]

        for i in range(rows_range):
            for j in range(cols_range):
                s = (
                    x
                    for r in matrix[i * sh : i * sh + h]
                    for x in r[j * sw : j * sw + w]
                )
                res[i][j] = max(s)

        return res
