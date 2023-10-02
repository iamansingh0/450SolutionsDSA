// code
/*package whatever //do not write package name here */

import java.io.*;

class GFG {

	public static double getMedian(int[] nums1, int[] nums2,
								int n)
	{
		// according to given constraints all numbers are in
		// this range
		int low = (int)-1e9, high = (int)1e9;

		int pos = n;
		double ans = 0.0;
		// binary search to find the element which will be
		// present at pos = totalLen/2 after merging two
		// arrays in sorted order
		while (low <= high) {
			int mid = low + ((high - low) >> 1);

			// total number of elements in arrays which are
			// less than mid
			int ub = upperBound(nums1, mid)
					+ upperBound(nums2, mid);

			if (ub <= pos)
				low = mid + 1;
			else
				high = mid - 1;
		}

		ans = low;

		// As there are even number of elements, we will
		// also have to find element at pos = totalLen/2 - 1
		pos--;
		low = (int)-1e9;
		high = (int)1e9;
		while (low <= high) {
			int mid = low + ((high - low) >> 1);
			int ub = upperBound(nums1, mid)
					+ upperBound(nums2, mid);

			if (ub <= pos)
				low = mid + 1;
			else
				high = mid - 1;
		}

		// average of two elements in case of even
		// number of elements
		ans = (ans + low * 1.0) / 2;

		return ans;
	}

	// a function which returns the index of smallest
	// element which is strictly greater than key (i.e. it
	// returns number of elements which are less than or
	// equal to key)
	public static int upperBound(int[] arr, int key)
	{
		int low = 0, high = arr.length;

		while (low < high) {
			int mid = low + ((high - low) >> 1);

			if (arr[mid] <= key)
				low = mid + 1;
			else
				high = mid;
		}

		return low;
	}

	public static void main(String[] args)
	{
		int[] arr = { 1, 4, 5, 6, 10 };
		int[] brr = { 2, 3, 4, 5, 7 };

		double median = getMedian(arr, brr, arr.length);

		System.out.println("Median is " + median);
	}
}


// question link
// https://www.geeksforgeeks.org/median-of-two-sorted-arrays/