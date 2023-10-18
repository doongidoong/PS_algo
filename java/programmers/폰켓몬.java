import java.util.*;
import java.io.*;

public class 폰켓몬 {
    public static int solution(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int num : nums) {
            int temp = map.get(num) != null ? map.get(num) + 1 : 1;
            map.put(num, temp);
        }
        int answer = nums.length / 2;
        if (answer > map.size()) answer = map.size();
        return answer;
    }

    public static void main(String[] args) throws IOException {
        System.out.println(solution(new int[]{3, 1, 2, 3}));
    }
}
