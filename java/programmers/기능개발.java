import java.io.IOException;
import java.util.*;

public class 기능개발 {
    public static List<Integer> solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList<>();
        int pos = 0;
        int days = 0;
        int cnt = 0;
        while (pos < progresses.length){
            int remain = 100 - progresses[pos];
            if (days*speeds[pos] >= remain ){
                cnt++;
            } else {
                if (pos !=0) {
                    answer.add(cnt);
                    cnt = 0;
                }
                cnt++;
                remain = remain - days*speeds[pos];
                days += remain / speeds[pos];
                if (remain % speeds[pos] > 0) days++;
            }
            pos++;
        }
        answer.add(cnt);
        return answer;
    }

    public static void main(String[] args) throws IOException {
        System.out.println(solution(new int[]{100, 100, 100, 10}, new int[]{10, 10, 10, 20}));
    }
}