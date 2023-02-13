import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner scan =new Scanner(System.in);
        int i=1;
        while(scan.hasNext()){ 
          System.out.println(i+" "+scan.nextLine());  
          i++;
        }
    }
} /*hasNext() - Return boolean value, return true if the iterationhas more elements
next()        - return next element in iteration 
nextLine()    - return next line in eteration
*/
