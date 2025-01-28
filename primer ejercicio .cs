using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace tarea_1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // En la linea 15 se replica el ToInt32(Console.ReadLine()); para asi tener la misma entrada y no confundir el codigo con faltas 
            Console.WriteLine("ingrese el primer numero:");
            int num1 = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine("ingrese el segundo numero:");
            int num2 = Convert.ToInt32(Console.ReadLine());

            int suma = num1 + num2;
            
            //En la linea 22 le hacia falta al final el punto y coma para poder acabar la intruccion 
            Console.WriteLine($"la suma es: {suma}");

        }
    }
}
