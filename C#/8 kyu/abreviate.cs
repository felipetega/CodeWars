public class Kata
{
  public static string AbbrevName(string name)
  {
    string[] names = name.Split(" ");
    return (names[0][0] + "." + names[1][0]).ToUpper();
  }
}