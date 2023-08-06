/*
https://www.hackerrank.com/contests/hope-70-days-challenge/challenges/java-string-reverse
*/



import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        String b="";
        for(int i=A.length()-1;i>=0;i--)
        {
            b+=A.charAt(i);
        }
        if(A.equals(b))
            System.out.print("Yes");
        else
            System.out.print("No");
    }
}