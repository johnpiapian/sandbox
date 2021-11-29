using System;
using System.Collections.Generic;
using System.Linq;

namespace practice
{
    public class SpareArrays
    {
        public SpareArrays()
        {
            List<string> strings = new List<string>
            {
                "aba",
                "baba",
                "aba",
                "xzxb"
            };

            List<string> queries = new List<string>
            {
                "aba",
                "xzxb",
                "ab"
            };


            foreach(var line in matchingStrings(strings, queries))
            {
                Console.WriteLine(line);
            }
        }

        public List<int> matchingStrings(List<string> strings, List<string> queries)
        {
            List<int> result = new List<int>();
            Dictionary<string, int> dict = new Dictionary<string, int>();

            foreach (string str in strings)
            {
                if (dict.ContainsKey(str))
                {
                    dict[str] = dict[str] + 1;
                }
                else
                {
                    dict.Add(str, 1);
                }
            }

            for (int i = 0; i < queries.Count; i++)
            {
                string str = queries[i];
                if (dict.ContainsKey(str))
                {
                    result.Add(dict[str]);
                }
                else
                {
                    result.Add(0);
                }
            }


            return result;
        }
    }
}
