class arrayQ3{
    public static void main(String args[]){

        // checking the array is sorted or not 

        int arr[] = {1,2,23,4,5};
        boolean isSorted = true;

        for(int i = 1 ; i < arr.length ; i++ ){

            if(arr[i-1] > arr[i]){
                isSorted = false;
                break;
            }

            
        }
        if(isSorted){
                System.out.println("array is in the sorted order...");
            }
            else{
                System.out.println("array is not in the sorted order...");
            }


    }

}
