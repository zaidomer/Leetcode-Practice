//https://leetcode.com/problems/first-bad-version/

/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        // int start = 1;
        // int end = n;
        // System.out.println("n: " + n);
        // while(!(isBadVersion(start + (end-start)/2) && !isBadVersion(start + (end-start)/2-1))){
        //     System.out.println(start + (end-start)/2);
        //     if(!isBadVersion(start + (end-start)/2)){
        //         start = start + (end-start)/2 + 1;
        //     }else if(isBadVersion(start + (end-start)/2) && isBadVersion(start + (end-start)/2-1)){
        //         end = start + (end-start)/2 - 1;
        //     }
        // }
        // return start + (end-start)/2;

        

        int start = 1; // Start of the search range
        int end = n; // End of the search range
        int mid = 0; // Variable to store the middle version
        
        while (start <= end) {
            mid = start + (end - start) / 2; // Calculate the middle version

            if (isBadVersion(mid)) {
                end = mid - 1; // Adjust the end to search in the left half (lower versions)
            } else {
                // If the middle version is not bad, all versions before it are good
                start = mid + 1; // Adjust the start to search in the right half (higher versions)
            }
        }

        return end + 1; // Return the index of the first bad version
    }
}