using System;
namespace practice
{
    public class First
    {
        public First()
        {
            int cp = 0;
            string[] names = { "Name", "Address", "Phone" };

            foreach (var name in names)
            {
                if (cp == 0)
                {
                    Console.WriteLine("What is your name: ");
                    Console.ReadLine();
                    cp++;
                }
                else if (cp == 1)
                {
                    Console.WriteLine("What is your Address: ");
                    Console.ReadLine();
                }
            }
        }
    }
}
