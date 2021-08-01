package newpro;
//Creating a MergeSort class with 3 methods 
public class MergeSort{
  // Method 1 to print the array elements 
  public static void printArrays(int[] array){
      for(int i=0;i<array.length;i++){
          System.out.print(array[i]+" ");
      }
      System.out.println();
  }
  //Method to split the array into single elements by continuos recusrion until the length is 1
  public static int[] splitArray(int[] array){
      if(array.length<=1){
          return array;
      }
      else{
          int mid = (array.length)/2;
          int[] left = new int[mid];
          int[] right = new int[array.length-mid];
          for(int i=0;i<left.length;i++){
              left[i] = array[i];
          }
          for(int j=0;j<right.length;j++){
              right[j] = array[mid+j];
          }
          int[] result = new int[array.length];
          left = splitArray(left);
          right = splitArray(right);
          result = mergeArray(left,right);
          return result;
      }
  }
  // Comparing the element of the left and the right array and adding as per sort in the result array and returning it back
  public static int[] mergeArray(int[] left,int[] right){
      int[] result = new int[left.length+right.length];
      int leftp = 0;
      int rightp = 0;
      int resultp = 0;
      while(leftp<left.length || rightp<right.length){
          if(leftp<left.length && rightp<right.length){
              if(left[leftp]<right[rightp]){
                  result[resultp++] = left[leftp++];
              }
              else {
                  result[resultp++] = right[rightp++];
              }
          }
          else if(leftp<left.length){
              result[resultp++] = left[leftp++];
          }
          else if(rightp<right.length){
              result[resultp++] = right[rightp++];
          }
      }
      return result;
  }
  // Final main method taking input and calling all the methods required to mergeSort a given array
  public static void main(String[] args){
      int[] array = new int[]{5,4,3,2,1};
      System.out.printf("The input array is : ");
      printArrays(array);
      System.out.printf("The sorted array is : ");
      printArrays(splitArray(array));
  }
}
