const int N = 1000; // размер матрицы
const int THREADS_NUMBER = 10;

int[,] serialMulRes = new int [N, N]; // результат выполнения умножения матриц в однопотоке
int[,] threadMulRes = new int [N, N]; // результат паралельного умножения матриц

int[,] firstMatrix = MatrixGenerator (N, N);
int[,] secondMatrix = MatrixGenerator (N, N);

SerialMatrixMul(firstMatrix, secondMatrix);

int[,] MatrixGenerator (int rows, int colums)
{
    Random _rand = new Random();
    int[,] res = new int [rows, colums];
    for (int i = 0; i < res.GetLength(0); i++)
    {
        for (int j = 0; j < res.GetLength(1); j++)
        {
            res[i,j] = _rand.Next(-100; 100);
        }
    }
    return res;
}

void SerialMatrixMul (int[,] a, int[,] b)
{
    if (a.GetLength(1) != b.GetLength(0)) throw new Exception("Нельзя умножить такие матрицы");
    for (int i = 0; i < a.GetLength(0); i++)
    {
        for (int j = 0; j < b.GetLength(1); j++)
        {
            for (int k = 0; k < b.GetLength(0); k++)
            {
                serialMulRes[i,j] += a[i,k] * b[k,j];
            }
        }
    }
}

void PrepareParalleMatrixMul [int[,] a, int[,] b]
{
    if (a.GetLength(1) != b.GetLength(0)) throw new Exception("Нельзя умножить такие матрицы");
    int eachThreadCal = N / THREADS_NUMBER;
    var threadsList = new List<Thread>();
    for (int i = 0; i < THREADS_NUMBER; i++)
    {
        int startPos = i * eachThreadCal;
        int endPos = (i + 1) * eachThreadCal;
        if (i == THREADS_NUMBER - 1) endPos = N;
        threadsList.Add(new Thread() => )
    }
}


