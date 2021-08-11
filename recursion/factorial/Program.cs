/* 
Write a recursive implementation of the factorial function. Recall that n! = 1 × 2 × ... × n,
with the special case that 0! = 1.
*/
using System;

namespace factorial
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter positive integer: ");
            int positiveInt = int.Parse(Console.ReadLine());

            int factorial = Factorial(positiveInt);
            Console.WriteLine($"Factorial of {positiveInt} is {factorial}");

        }

        static int Factorial (int num)
        {
            if (num == 0 || num == 1)
                return 1;
            return num * Factorial(num - 1);
        }
    }
}
