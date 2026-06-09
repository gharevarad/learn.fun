class arrayQ5{
    public static void main(String args[]){

        // finding an missing value from an array

        int arr[] = {1,2,3,5,7,10};
        int n = 10;
        boolean matched = false;
        int numbers = 0;
        System.out.print("missing number is : ");
        for(int num = 1 ; num <= n ; num ++){
            matched = false;
        

            for(int i = 0 ; i < arr.length; i++){
                if(arr[i] == num){
                    matched = true;
                    break;
                }
            }

                if(!matched){
                    System.out.print( num + " ");
                }             
        } 
    }
}
