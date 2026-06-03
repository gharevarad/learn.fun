// learning full java and data structure in java 

import java.util.*;
import java.io.*;

class index {
    public static void main(String arfs[]) throws IOException{
        
        // printing an fibonacci series 

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        System.out.println("enter how much numbers you wanted in fibonacci series : ");
        int n = Integer.parseInt(br.readLine());
        int num1 = 0;
        int num2 = 1;

        System.out.println(num1);
        System.out.println(num2);
        for(int i = 1;i<=n-2;i++)
        {
            int next = num1 + num2;
            System.out.println(next);
            int temp = num1;
            num1 = num2;
            num2 = next;

        }


         

    }
}
    
    
