//Invert values

using System.Linq;
namespace Solution
{
  public static class ArraysInversion
  {
    public static int[] InvertValues(int[] input)
    {
      int[] res = new int[input.Length];
      for (int i = 0; i < input.Length; i++)
      {
        res[i] = -input[i];
      }
      return res;
    }
  }
}