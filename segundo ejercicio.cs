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
            Console.WriteLine("ingrese el primer numero:");
            int n = Convert.ToInt32(Console.ReadLine());

            for (int i = 1; i <= n; i++)
                // se elimina la llave ya que el compilador esta esperando una llave de cierre y hace que el codigo de un error 
            Console.WriteLine("numero actual:" + i);
 
        }
    }
}
