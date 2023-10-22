//https://leetcode.com/problems/k-closest-points-to-origin/description/

class Solution {

    public double distance(int[] point) {
        return Math.sqrt(point[0] * point[0] + point[1] * point[1]);
    }

    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<int[]> q = new PriorityQueue<>(new Comparator<int[]>() {
            public int compare(int[] a, int[] b) {
                if (distance(a) < distance(b)) {
                    return -1;
                }
                return 1;
            }
        });

        for (int i = 0; i < points.length; i++) {
            q.offer(points[i]);
        }

        int[][] result = new int[k][];
        for (int j = 0; j < k; j++) {
            result[j] = q.poll();
        }
        return result;
    }

}