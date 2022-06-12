/*
https://www.codewars.com/kata/555bfd6f9f9f52680f0000c5

Given a number, write a function to output its reverse digits. (e.g. given 123 the answer is 321)

Numbers should preserve their sign; i.e. a negative number should still be negative when reversed.
*/


public class ReverseNumber {

  public static int reverse(int number) {
    String strNumber = Integer.toString(number);
    String[] s;
    String output = "";
    if(number >= 0){
      s = strNumber.split("");
        for(int i=s.length-1; i>=0; i--){
          output += s[i];
        }
      return Integer.parseInt(output);
    }
    else{
      s = strNumber.split("");
      for(int i=s.length-1; i>0; i--){
          output += s[i];
        }
      return (Integer.parseInt(output))*(-1);

    }
  }

}