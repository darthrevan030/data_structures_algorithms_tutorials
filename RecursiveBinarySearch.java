public class RecursiveBinarySearch {
    public static int binarySearch(int[] input, int target, int start, int end) {
        if (start >= end) {
            return -1;
        } else {
            int mid = start + (end - start) / 2;

            if (target < input[mid]) {
                return binarySearch(input, target, start, mid-1);
            } else if (target > input[mid]) {
                return binarySearch(input, target, mid+1, end);
            } else {
                return mid;
            }
        }
    }
}