/*
https://www.codewars.com/kata/5259b20d6021e9e14c0010d4

Complete the function that accepts a string parameter, and reverses each word in the string.
 All spaces in the string should be retained.
*/

public class Kata{

  public static String reverseWords(final String original){

    String output = "";
    String ans = "";
    for(int i = original.length()-1; i>=0; i--){
      output += original.charAt(i);
    }

    String s[] = output.split(" ");
    if(s.length == 0){
      return original;
    }
    for(int i = s.length-1; i>=0; i--){
      ans += s[i];
      if (i!=0){
        ans += " ";
      }
    }
    return ans;
  }
}