import java.io.IOException;
import java.util.*;
class 완주하지못한선수 {
    public static String solution(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String, Integer> map = new HashMap<>();
        for (String com : completion) {
            int temp = map.get(com) != null ? map.get(com) + 1 : 1;
            map.put(com, temp);
        }
        for (String part : participant) {
            if (map.get(part) == null ||  map.get(part) == 0) {
                answer = part ;
            }
            else {
                map.put(part,  map.get(part)-1);
            }
        }
        return answer;
    }

    // public static void main(String[] args) throws IOException {
    //     System.out.println(solution(new String[]{"leo", "kiki", "eden"}, new String[]{"eden", "kiki"}));
    // }
}