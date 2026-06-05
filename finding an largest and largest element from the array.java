class demo{
    public static void main(String args[]){

         // finding the largest and the second largest element from an array...

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
