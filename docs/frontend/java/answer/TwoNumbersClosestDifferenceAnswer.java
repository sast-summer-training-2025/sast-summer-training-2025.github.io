package Answer;

import java.util.Arrays;
import java.util.Scanner;

public class TwoNumbersClosestDifferenceAnswer {
    public static int[] findClosestPair(int[] nums, int target) {
        // TODO begin
        Arrays.sort(nums);
        int left = 0, right = nums.length - 1;
        int minDiff = Integer.MAX_VALUE;
        int[] result = new int[2];

        while (left < right) {
            int diff = nums[right] - nums[left];
            int gap = Math.abs(diff - target);
            if (gap < minDiff) {
                minDiff = gap;
                result[0] = nums[left];
                result[1] = nums[right];
            }
            if (diff < target) {
                left++;
            } else {
                right--;
            }
        }
        return result;
        // TODO end
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter array length: ");
        int n = sc.nextInt();
        int[] nums = new int[n];

        System.out.println("Enter array elements (space-separated):");
        for (int i = 0; i < n; i++) {
            nums[i] = sc.nextInt();
        }

        System.out.print("Enter target difference: ");
        int target = sc.nextInt();

        int[] ans = findClosestPair(nums, target);

        System.out.println(ans[0] + " " + ans[1]);

        sc.close();
    }
}
