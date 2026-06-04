// learning full java and data structure in java 

import java.util.*;
import java.io.*;

class index {
    public static void main(String arfs[]) throws IOException{
        
        // printing an fibonacci series 


        // BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // System.out.println("enter how much numbers you wanted in fibonacci series : ");
        // int n = Integer.parseInt(br.readLine());
        // int num1 = 0;
        // int num2 = 1;
        // System.out.println(num1);
        // System.out.println(num2);
        // for(int i = 1;i<=n-2;i++)
        // {
        //     int next = num1 + num2;
        //     System.out.println(next);
        //     int temp = num1;
        //     num1 = num2;
        //     num2 = next;

        // }


        // take a input of string and reverse it without an built in function in  java
        
        
        // BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // System.out.println("enter the string which you wanted to be reversed : ");
        // String name = br.readLine();
        // String reversed = "";
        
        // for(int i = name.length() -1; i >= 0; i-- ){
        //     reversed = reversed + name.charAt(i);
            
        // }
        //     System.out.println(reversed);


    // check wether the number is palindrome or not  121 reverse should be same


        // BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // System.out.println("enter the number : ");
        // int num = Integer.parseInt(br.readLine());
        // int original = num;
        // int reverse = 0;

        // if(num < 0){
        //     System.out.println("enter a positive number ");
        // }
        // else{

        //     while(num > 0){
        //         int digit = num % 10; 
        //         reverse = reverse * 10 + digit;
        //         num = num / 10;
        //     }
        //     System.out.println(reverse);
           

        // }
        // if(reverse == original){
        //     System.out.println("the is a palindrome... ");
        // }
        // else{
        //     System.out.println("numer is not an palindrome... ");
        // }



    // finding the largest and the second largest element from an array 



        int arr[] =  {12,24,34,32,45,23};
        int secondLargest = Integer.MIN_VALUE;
        int largest = Integer.MIN_VALUE;

        for(int i = 0;i<=arr.length-1;i++){

            if(arr[i] > largest){
                secondLargest = largest;
                largest = arr[i];
            }
            else if(arr[i] > secondLargest && secondLargest != largest){
                secondLargest = arr[i];
            }


        }
        System.out.println("secondlargest element us : " + secondLargest);
        System.out.println("largest element us : " + largest);

         

    }
}
    
    
