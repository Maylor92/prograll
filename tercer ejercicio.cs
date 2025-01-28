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
            Console.WriteLine("ingrese el numero entero:");
            int numero = Convert.ToInt32(Console.ReadLine());

            if (numero % 3 == 0|| numero % 5 ==0)
            {
                Console.WriteLine("El numero es multiplo de 3 y 5.");

            }
            else
            // se elimina la llave extra ya que estaba esperando un cierre y hace que el codigo falle 
                Console.WriteLine("El numero no es multiplo de 3 o 5.");

        }
    }
}
