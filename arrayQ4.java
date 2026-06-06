class arrayQ4{
    public static void main(String args[]){

        // get a dublicate element from an array

        int arr[] = {12,2,3,34,4,7};
        boolean dublicateValue = false;
        int i;

        for( i = 0;i < arr.length;i++){

            for(int j = i+1;j < arr.length;j++){

                if((arr[i] ^ arr[j]) == 0){
                    System.out.println(arr[i] + " the number is dublicate");
                    dublicateValue = true;
                    break;
                }
                
                
            }

            

        }
        if(!dublicateValue){ 
            System.out.println("array doesnt have a dublicate value...");
        }

    }
}
