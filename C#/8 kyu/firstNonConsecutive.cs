//Find the first non-consecutive number

public class Kata
{
  public static object FirstNonConsecutive(int[] arr)
  {
    int? res = null;
    int first = arr[0];
    for (int i = 0; i < arr.Length; i++)
    {
      if (arr[i] == first + i)
      {
        continue;
      }
      else
      {
        res = arr[i];
        break;
      }
    }
    return res;
  }
}